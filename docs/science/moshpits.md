Curious collective behaviors are all around us from the atomic to the
astronomical scale.  For example, how do defects in crystals
({{ref('docs/science/plasticity.yaml')}}) organize themselves into sharp,
wall-like structures when left to their own devices?  How galaxies form the
neat spiral shapes (<a href='http://en.wikipedia.org/wiki/Spiral_galaxy'>Spiral
galaxy</a>) appears to be an open question still (says the wiki). On smaller
scales, flocks of birds create very cool patterns such as those found in
starlings (movie below).  How do they decide which direction to fly?  How is
information transmitted from bird to bird?

<iframe style='display: block; margin: auto; position: relative;' width="480"
height="360" src="//www.youtube.com/embed/iRNqhi2ka9k?vq=hd720&start=61"
frameborder="0" allowfullscreen></iframe>

On the human scale, how do marching bands work?  What is the nature of the
intricate patterns that a marching band makes as they perform a halftime show?
Are they only moving relative to one another and memorized separation vectors,
or have they memorized specific positions on the field and when to move between
them?  Is there a set of measurements that you could perform to determine which
of these methods or combination of methods they use?  I presume that these
positions are determined prior to the performance (otherwise super kudos to
them), meaning that there could be no interactions between the performers and
they could still make these impressive patterns.  What would halftime look like
if they had no prior knowledge and were simply told to make the shape of a
pterodactyl?  I bet that would not go over very well.

It turns out that beautiful collective motions also occur in a very different
scenario: in the crowds at heavy metal concerts.  When these energetic crowds
get together, a whole zoo of collective motions can be seen, including:

 * *Mosh pits* - members of the crowd run around bumping into each other
   chaotically
 * *Cirlce pits* - a portion of the crowd runs in a circle
 * *Fist pumping* - throwing fists in the air to the beat / influenced by
   people around you
 * *Synchronized jumping* - jumping to the beat, with local coupling and global
   forcing
 * *Wall of death* - the crowd separates into two halves which then run at each
   other Braveheart style
 * *Meat grinder* - N concentric circle pits, each moving in the opposite
   direction (very rare)

Many of these collective behaviors are highlighted in this compilation video,
which I highly encourage you to watch.

<iframe style='display: block; margin: auto; position: relative;' width="640"
height="360" src="//www.youtube.com/embed/R2cz8EeIBrQ?vq=hd720"
frameborder="0" allowfullscreen></iframe>

The model
---------

Of these behaviors, <a
href='http://scholar.google.com/citations?user=sdGV09AAAAAJ&hl=en'>Jesse
Silverberg</a> and I thought that the mosh pit, circle pit, and the
relationship between them seemed like an interesting and tractable problem.
Since 1987, starting with Craig Reynolds, a type of model called a flocking
model has been successfully used to describe many collective motions in various
systems including birds, bison, and humans.  Given this success, we adapted the
flocking model to the situation of extreme collective behaviors at heavy metal
concerts, attempting to describe the mosh pit and circle pit.  After some
reasonsing, reading, and testing we discovered that there are 4 aspects that
are important to replicating the behaviors we were after. They are

 1. People are solid bodies, they should not pass through one another
 2. At the events, people are self-propelled - they run around
 3. Individuals don't have perfect information about their surroundings or
    control of themselves
 4. A notion from the flocking science community that individuals like to move
    in the direction of the people around them

For these four aspects, we wrote down a model with four forces on each individual, 
in the same order that they are listed above.  During a simulation, we calculate
the total force on each individual $i$ using the forces below and then integrate
these forces to see how the crowd as a whole behaves.

$$ \vec{F}_{i}^{\rm repulsion} = \epsilon \left(1-\frac{r_{ij}}{2r_0}\right)^{5/2} \hat{r}_{ij} $$
$$ \vec{F}_{i}^{\rm propulsion} = \beta (v_0 - v_i) \hat{v}_i $$
$$ \vec{F}_{i}^{\rm noise} = \vec{\eta}_i $$
$$ \vec{F}_{i}^{\rm flocking} = \alpha \sum_{j=0}^{N_i} \vec{v}_j \Big/ \left|\sum_{j=0}^{N_i} \vec{v}_j \right| $$

These forces are not novel, each as has been used in many situations before.
However, if we split the parameters for these particles into two groups, we
find that the behaviors that are accessible are quite surprising.  In
particular, we can make two groups called active and passive moshers which are
distinguished by $\alpha$ and $\beta$.  Active moshers flock and run around
($\alpha \ne 0$ and $\beta \ne 0$) whereas passive ones don't ($\alpha = \beta
= 0$).

To mimic a concert, we first began with a circle of active moshers surrounded by
a crowd of passive ones (what you often see at a concert).  Doing this and tuning
the parameters, we find that we can produce both a mosh pit and circle from the
same model.  When the flocking strength is low, mosh pits form.  As this strength is
increased, circle pits begin to form instead.  These two behaviors can be seen
in the videos below:

<iframe style='display: block; margin: auto; position: relative;' width="360"
height="360" src="//www.youtube.com/embed/9SVcLg4Oyoc"
frameborder="0" allowfullscreen></iframe>

<iframe style='display: block; margin: auto; position: relative;' width="360"
height="360" src="//www.youtube.com/embed/-58HBzM9w00"
frameborder="0" allowfullscreen></iframe>

You can explore the various behaviors of these equations of motion by visiting
our interactive simulation built for the web at:

{{ break() }}
{{ biglink('http://mattbierbaum.github.io/moshpits.js/',
           'Moshpits.js') }}
{{ break() }}

If you thought that the initial conditions of starting off in a circle were a
bit contrived, then you'd be right.  We did too.  But, it turned out that
started with the populations mixed led to a spontaneous self-segregation! After 
the circle formed, then a mosh pit or circle pit would form anyway.  This hints
that these dynamical structures are actually stable, which was supported by
the fact that even extremely large pits did not dissolve after a very long time.
Below is the largest circle pit we simulated (~100k participants).  The red particles
are active moshers while the black are passive.  The black particles are shaded gray 
according the force that they feel, thus labeling grain boundaries in the crowd.

<iframe style='display: block; margin: auto; position: relative;' width="480"
height="480" src="//www.youtube.com/embed/YLggpXiFJWg?vq=hd720"
frameborder="0" allowfullscreen></iframe>

<iframe style='display: block; margin: auto; position: relative;' width="480"
height="480" src="//www.youtube.com/embed/h46wpNX0N1E?vq=hd720"
frameborder="0" allowfullscreen></iframe>

In the second movie, you can watch the segregation take place in a system of
100k participants.  It's a rather long movie so feel free to fast forward and
look at several different states.

<!--{{ figure("/img/moshpits/phase_diagram.png", "The phase diagram of mosh pits \
and circle pits.  As the noise increases, there is a sweet spot where circle \
pits naturally exist.  The borders of this phase diagram can be understood \
by comparing time scales in the equations of motion.", 420, 'right') }}-->

For more information, you can visit the Cohen lab's page on moshpits:

{{ break() }}
{{ biglink('http://cohengroup.lassp.cornell.edu/research.php?project=10017',
           'Cohen Group Page') }}

Or read the original paper on the ArXiv:

{{ break() }}
{{ biglink('http://arxiv.org/abs/1302.1886', 'ArXiv paper') }}


