#!/usr/bin/env python
import os
import glob
import jinja2
import yaml
import markdown2 as md
import shutil
from datetime import datetime
from collections import defaultdict

OUTFOLDER = "./pages"
MDFOLDER = "./docs"
ROOTFOLDER = OUTFOLDER[1:]
DATEFORMAT = "%Y-%m-%d %H:%M:%S"

def time_create():
    return datetime.strftime(DATEFORMAT)

def time_load(st):
    return datetime.strptime(st, DATEFORMAT)

def figure(filename, caption, size, loc='center'):
    template = tmpl.get_template('./figure.html')
    out = template.render(src=filename, caption=caption, size=size, loc=loc)
    return out

def code(code, lang='python'):
    return """
    <code class='%s'><pre>
%s
    </pre></code>
    """ % (lang, code)

def eq(tex):
    pass

def insert_break():
    return "<br style='clear: both;' />"

tmpl = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
    undefined=jinja2.StrictUndefined,
)

tmpl.globals.update({
    "figure": figure,
    "code": code,
    "eq" : eq,
    "break": insert_break,
})

def title_to_url(title):
    temp = title.replace("'", '').replace('"', '').replace('.','').replace('*', '')
    return "_".join(temp.lower().split(' '))

def load_all_docs(folder=MDFOLDER):
    docs = []
    mark = md.Markdown()

    for f in glob.glob(os.path.join(folder, "*")):
        if os.path.isdir(f):
            docs.extend(load_all_docs(f))
        elif f.endswith(".yaml"):
            print "Loading %s" % f
            doc = yaml.load(open(f))
            doc['href'] = ROOTFOLDER+'/'+doc['category']+'/'+title_to_url(doc['quicktitle'])+'.html'
            doc['outfile'] = OUTFOLDER+'/'+doc['category']+'/'+title_to_url(doc['quicktitle'])+'.html'
            doc['bodyfile'] = f.replace(".yaml", ".md")
            docs.append(doc)

    return docs
 
def process_doc(doc, header):
    mark = md.Markdown()
    with open(doc['bodyfile']) as f:
        body = f.read()
        print doc
        doc['body'] = tmpl.from_string(mark.convert(body)).render()
        template = tmpl.get_template("./template_doc.html")
        out = template.render(title=doc['title'], doc=doc, header=header)
 
    with open(doc['outfile'], 'w') as f:
        f.write(out)

def process_snap(snap, filename, header):
    template = tmpl.get_template("./template_snap.html")
    out = template.render(title=snap['name'], snaps=snap, header=header)

    with open(filename, 'w') as f:
        f.write(out)

def process_home(header):
    template = tmpl.get_template('./template_home.html')
    out = template.render(title="", header=header)

    with open('index.html', 'w') as f:
        f.write(out)

def process_site():
    docs = load_all_docs()
    cats = list(set([d['category'] for d in docs]))
    cats.sort()
    
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

    header = [{'name': cat, 'href': ROOTFOLDER+'/'+cat, 'list': tcat[cat][:3]} for cat in cats]
    snaps = [{'name': cat, 'href': cat, 'list': tcat[cat]} for cat in cats]

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


if __name__ == "__main__":
    process_site()
