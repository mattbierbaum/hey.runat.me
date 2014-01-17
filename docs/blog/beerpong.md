We all know that the game of beer pong is relatively simple in terms of
physics.  What this post presupposes is: maybe it isn't?

{{ figure('/img/beerpong/fractalpreview.png', "A fractal generated with \
beer pong dynamics.  Probs not simple.", 362, 'right') }}

First, I feel like I have to explain what the game beer pong is.  And let me
tell you, it is exactly what it sounds like - a small white ball bouncing
between two paddles on an Atari while two gentlemen sip beverages.  Well, fine,
it's dudes throwing balls into cups full of beer until their girlfriends leave
for another party.

Now, what are typical questions that one may ask when thinking, "hmmm, I'm bored
and want to know about the physics of beer pong"?  If you are asking yourself that 
question, there are likely other things in your life you should question. None the
less, you may arrive at these:

1. What is the precise trajectory I need to make it in a cup?
2. How accurate do I need to be to get the ball in the cup?  Something about angular errors?
3. If I shot randomly at the cups what is the chance that I make it in? 

I have answers for these:

1. Easy, and useless.  You can't duplicate this with your hand. Give up. 
   Practice is better for this calculation.
2. Perform step 1, rinse and repeat.
3. A bit more subtle, but a good idea of its resolution comes from step 2, rinse, and repeat.

Let's ask a completely different question - what happens when we don't quite
make it?  What happens when the ball bounces off the rim?  Now there's
something to make your socks go up and down.

Okay, so everyone who has encountered physics knows that we can describe a ball
flying through air with a quadratic equation (except maybe Michael 'Air'
Jordan who simply has no regard for gravity).  It looks something like this:

$$ y(t) = y_0 + v_{0,y}t - \frac{1}{2}g t^2 $$
$$ x(t) = x_0 + v_{0,x}t $$
$$ z(t) = z_0 + v_{0,z}t $$

where y is up, gravity is down and **there is no air resistance**.  I feel like
I have to bring up this point unncessarily early.  I do physics, not real
things.  Air resistance would make this real. Real hard.  So it's gone, like my
respect for Halle Berry after Catwoman. So, when you throw a ball, you can
determine at any time where it is, where it's going and which dreams it's left
behind along the way.  This is going to be useful to us later, so don't forget
it.

Alright, so I guess we need to make some cups and balls and and then throw them
at one another.  Let's do it.

A cup rim is a torus.  A ball is a sphere. Bill Murray is my hero.  These are
just facts.  What is a little more contentious is that for the rest of this
post, I want to simplify the interaction of the cup rim and ball to a single
torus, leaving the ball to be an infinitessimal speck.  Imagine attaching one
of those awesome spherical neodymium magnets to a metal hoop and swinging it
around until the ball rolls over the entire surface.  The center of that sphere
would trace out the surface of a torus.  I hope that's convincing since I'm not
going to try again.  I tried to make a picture but it didn't turn out great.

{{ figure('/img/beerpong/cup-rim-torus.png', "I honestly don't know how \
<a href='http://hyperboleandahalf.blogspot.com/'>Allie Brosh</a> does it.  \
Must be one of those sketch pads or whatever.", 400, 'left') }}

Finding collisions between this infinitessimal ball and ball-rim torus amounts
to is then finding the intersection of the equation of torus and a parabola. A
torus can be written

$$ ((x_n)^2 + (y_n)^2 + (z_n)^2 + R^2 - r^2)^2 = 4R^2(x_n^2 + y_n^2) $$

where $x_n$, $y_n$, $z_n$ are normalized coordinates, $x_n = x - x_c$ where
$x_c$ is the center of the rim.  And all the rest are normalized too.  We can
then plug our previous equations and get an 8th order polynomial in time.  You
can convince yourself it's 8th order just by starring at the equation or
realizing how many times a cricket wicket could intersect a jelly doughnut.
Well, actually, just a regular doughnut since we need the <a
href='http://en.wikipedia.org/wiki/Doughnut#Holes'>hole</a> gone.


Okay, now that we know every time (literally, the variable is t) the ball
intersects the rim, we have to figure out what happens when it bounces off.
It's just like bouncing on a table, except that table is a torus and so only
flat in a small region.  So, we find the normal of the rim at the collision
point, and reflect the ball about this normal.  Easy, breezy, toroidal
cover girl.

For a quick recap (for science and reproducible and all that...):

 1. Give initial trajectory to a single infinitessimal ball
 2. Find all 8N possible collisions with a torus (technical: 
    <a href="http://en.wikipedia.org/wiki/Bairstow's_method">Bairstow's method</a>)
    , where N is the total number of cups that it could possibly collide with
 3. Determine the closest collision in time, throwing away those in the past
 4. Move to that collision point
 5. Determine the normal vector on that part of the torus and reflect the
    current velocity.
 6. Start again, and continue until the next collision time never occurs
    or it occurs after the ball crosses the zero plane.

Finally, we can start to look at some pictures a.k.a. did I just spew nonsense or 
is there a reason that this post goes on for 3 more pages. Let's drop ten
thousand ping pong balls from straight above a single cup rim and look at the
surface of interaction where they touch.  It looks like this:

{{ figure('/img/beerpong/rim_surface.png', 'I told you so.', 400, 'center') }}
{{ break() }}
{{ figure('/img/beerpong/rim_surface_lots.png', 'An infinite array of cups', 400, 'center') }}

The second picture is for an infinite array of cups, which we will be using
throughout Sections II-MVI.  I think this proves that I'm right so far.  So
let's just go with it.  

Okay, okay.  It's actually a little more subtle 
From here on out, we'll be dealing with various
configurations of these torii, looking at all sorts of pretty pictures.



Physical setup
--------------

I'll start again with ten thousands balls dropped directly overhead a
cup and color the pixel of where it started according to how many times the
ball bounced before it went into a cup.

<iframe scrolling="no" marginwidth="0" marginheight="0" frameborder="0" vspace="0" hspace="0" height=572 width=515 seamless src='/pages_ext/cupgame_zoom.html' style='display: table; margin:auto'></iframe>

