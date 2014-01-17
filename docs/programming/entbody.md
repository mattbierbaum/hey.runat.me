For a long time I've been interested in many-body / N-body / molecular dynamics
physics.  Along the way, I've been writing code to use the techniques I've read
about.  At the time of its inception, I was learning about neighbor lists, and 
quadtrees, so it was natural that I called the code, 'entbody'.  'Ent' comes
from the tree people in LOTR, so, it's got that going for it, which is nice.

{{ figure('/img/eyeofthestorm.png', "A simulation of 100,000 moshers at a heavy metal concert, in relation to the moshpits project found in the 'Science' heading.", 512, 'center') }}

entbody is now the generic name for the code which I split off into various 
projects as I go.  It can run on multicore CPU as well as NVIDIA GPUs and 
is best at short range forces.  On a Geforce Titan, it can simulate roughly 
one million interacting particles at 30 fps, fast enough to interact with it
through the keyboard.  

A stripped down version for GPU can be found on my github,

{{ biglink('https://github.com/mattbierbaum/entbody.cuda', 'entbody.cuda') }}
