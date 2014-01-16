For the 28th Ludum Dare, Alex and I decided to try our hand at making a web
based game.  The theme for this round was 'You only get one', quickly shortened
to YOGO by the other participants.  We decided that we would do a platformer
with light-based mechanics where you only get one look at the level, ever.
Conveniently, this played to our weaknesses of not being able to draw a level
to save our lives, since you never really look at it.

We ended up making three different items to use and three different monsters
that can make you restart a given level. The items are


 + *Look* - the one look you can use at any time
 + *Light bomb* - illuminate your local area for a short time
 + *Crumb* - leave a light in a particular location

There are three monsters that try to attack you during the game, each having
different attributes,

  + *Sleeper* - runs after you when you are in its near vicinity (proximity monster)
  + *Random* - takes a random walk through the level
  + *Hunter* - uses A-star to find the shortest path to you at all times (slightly slower than you)

Since you can't see very far, we implemented 2d directional sound so that you
can hear how far and in which direction monsters are.  Then, Alemi's ray casting
work to make the shadows and lighting really made it come together.

Check it out here:

{{ biglink('http://mattbierbaum.github.io/onelook/', 'Play Onelook') }}
