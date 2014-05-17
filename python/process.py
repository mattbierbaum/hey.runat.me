#!/usr/bin/env python
import os
import glob
import jinja2
import yaml
import mdx_mathjax
import markdown as md
import shutil
from datetime import datetime
from collections import defaultdict

OUTFOLDER = "./pages"
MDFOLDER = "./docs"
ROOTFOLDER = OUTFOLDER[1:]
DATEFORMAT = "%Y-%m-%d %H:%M:%S"

CATEGORY_PRIORITY = {"science": -1, "media": 4, "about": 5}

def time_create():
    return datetime.strftime(DATEFORMAT)

def time_load(st):
    return datetime.strptime(st, DATEFORMAT)

#=======================================================
def t2u(title): # title to url
    temp = title.replace("'", '').replace('"', '').replace('.','').replace('*', '')
    return "_".join(temp.lower().split(' '))

def d2u(doc): # doc to url
    return ROOTFOLDER+'/'+doc['category']+'/'+t2u(doc['quicktitle'])+'.html'

def s2u(snap): # snap to url
    return ROOTFOLDER+'/'+snap['name']

def c2u(cat): #category to url
    return ROOTFOLDER+'/'+cat

def p2d(path):
    with open(path) as f:
        doc = yaml.load(f)
        return doc

#=========================================================
def tpl_figure(filename, caption, size, loc='center'):
    template = tmpl.get_template('./figure.html')
    out = template.render(src=filename, caption=caption, size=size, loc=loc)
    return out

def tpl_figure_multi(filename, caption, size, loc='center', border=False):
    extrastyle = "bordered" if border else ""
    template = tmpl.get_template('./figure-multi.html')
    out = template.render(src=filename, caption=caption, size=size, loc=loc,
            extrastyle=extrastyle)
    return out

def tpl_code(code, lang='python'):
    return """
    <code class='%s'><pre>
%s
    </pre></code>
    """ % (lang, code)

def tpl_biglink(href, text):
    return """<a style='line-height: 30px; font-weight: bold; text-decoration: none; font-size: 36px; display: table; margin:auto;' href='%s'>%s</a>""" % (href, text)

def tpl_eq(tex):
    pass

def tpl_insert_break():
    return "<br style='clear: both;' />"

def tpl_sizes(arr):
    tp = {1: '98', 2: '48', 3: '31', 4: '23', 5: '18'}
    return 'figsize-'+tp[len(arr)]

def tpl_ref(tag):
    doc = p2d(tag)
    url = d2u(doc)
    return "<a href='%s'>%s</a>" % (url, doc['quicktitle'])

tmpl = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
    undefined=jinja2.StrictUndefined,
)

tmpl.globals.update({
    "figure": tpl_figure,
    "figure_multi": tpl_figure_multi,
    "code": tpl_code,
    "eq" : tpl_eq,
    "break": tpl_insert_break,
    "biglink": tpl_biglink,
    'imsize': tpl_sizes,
    'ref': tpl_ref,
})

#========================================================
def load_all_docs(folder=MDFOLDER):
    docs = []

    for f in glob.glob(os.path.join(folder, "*")):
        if os.path.isdir(f):
            docs.extend(load_all_docs(f))
        elif f.endswith(".yaml"):
            print "Loading %s" % f
            doc = yaml.load(open(f))
            doc['href'] = ROOTFOLDER+'/'+doc['category']+'/'+t2u(doc['quicktitle'])+'.html'
            doc['outfile'] = OUTFOLDER+'/'+doc['category']+'/'+t2u(doc['quicktitle'])+'.html'
            doc['bodyfile'] = f.replace(".yaml", ".md")
            docs.append(doc)

    return docs
 
def process_doc(doc, header):
    mark = md.Markdown(extensions=['mathjax'])
    with open(doc['bodyfile']) as f:
        body = f.read()
        doc['body'] = tmpl.from_string(mark.convert(body)).render()
        template = tmpl.get_template("./template_doc.html")
        out = template.render(title=doc['title'], doc=doc, header=header,
                linklist=[{'href': '/', 'name': '/runat.me/'},
                    {'href': ROOTFOLDER+'/'+doc['category'], 'name': doc['category']+'/'},
                    {'href': doc['href'], 'name': t2u(doc['quicktitle'])}])
 
    with open(doc['outfile'], 'w') as f:
        f.write(out)

def process_snap(snap, filename, header):
    template = tmpl.get_template("./template_snap.html")
    out = template.render(title=snap['name'], snaps=snap, header=header,
            linklist=[{'href': '/', 'name': '/runat.me/'},
                      {'href': snap['href'], 'name': snap['name']}])

    with open(filename, 'w') as f:
        f.write(out)

def process_home(header):
    template = tmpl.get_template('./template_home.html')
    out = template.render(title="", header=header, 
            linklist=[{'href': '/', 'name': '/runat.me/'}])

    with open('index.html', 'w') as f:
        f.write(out)

def process_404(header):
    template = tmpl.get_template('./template_404.html')
    out = template.render(title="", header=header, 
            linklist=[{'href': '/', 'name': '/runat.me/'}])

    with open('404.html', 'w') as f:
        f.write(out)

def process_redirects():
    doc = yaml.load(open("./python/redirects.yaml"))
    template = tmpl.get_template("./template_redirect.html")
    for old, new in doc.iteritems():
        old = os.path.abspath(old)
        dirs = os.path.dirname(old)
        if not os.path.exists(old):
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            with open(old, "w") as f:
                f.write(template.render(url=new))

def process_site():
    docs = load_all_docs()
    cats = list(set([d['category'] for d in docs]))
    cats.sort(key=lambda tup: (CATEGORY_PRIORITY.get(tup, 0), tup))
    
    docs.sort(key=lambda tup: (tup['priority'], tup['date'])) 
    docs.reverse()

    """ 
    categories are sent to the template in the form:
        [
            { 
                'name': 'science', 'href': 'science',
                'list': [ <docs in priority order up to 3> ]
            }
        ]
    """
 
    tcat = defaultdict(list)
    for doc in docs:
        c = doc['category']
        info = {'name': doc['quicktitle']}
        info.update(doc)
        tcat[c].append(info)

    header = [{'name': cat, 'href': ROOTFOLDER+'/'+cat, 'list': tcat[cat][:5]} for cat in cats]
    snaps = [{'name': cat, 'href': ROOTFOLDER+'/'+cat, 'list': tcat[cat]} for cat in cats]

    if os.path.exists(OUTFOLDER):
        shutil.rmtree(OUTFOLDER)
    os.mkdir(OUTFOLDER, 0755)

    for snap in snaps:
        snap_folder = os.path.join(OUTFOLDER, snap['name'])
        os.mkdir(snap_folder, 0755)
        process_snap(snap, os.path.join(snap_folder, 'index.html'), header)

    for doc in docs:
        process_doc(doc, header)

    process_home(header)
    process_404(header)
    process_redirects()

if __name__ == "__main__":
    process_site()
