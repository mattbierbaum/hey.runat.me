Clicky, formerly Prof. Dottington / Henry Hoopula / Senor Circle, is an online
social experiment in which anyone who visits the site is greeted by a red dot
on a square grid.  The user can move this dot using the arrow keys and by
clicking the buttons, leaving a trail behind the dot as it moves.  The catch is
that there is only dot - everyone sees and interacts with the same dot, Clicky.
When someone across the world makes him move up, he moves up for everybody.

{{ figure('/img/snaps/clicky-512.png', 'Example screen from Clicky, saying hi.', 400, 'center') }}

We've quite a few iterations of Clicky as it turns out that realtime, massively
interactive apps on the web are sort of tricky.  The first time, we started
with a polling framework which asked for all points that needed to be drawn to
the screen from a MySQL database.  We used 10GB of bandwidth in less than a
week with this method, not to mention the lag problems.  In the second
iteration, we tried to be smart about repeating data since lines need to only
be drawn once.  This lasted a long time but too got slow due to database
issues.  Finally, we switched to WebSockets and an in-memory location hash
structure meaning meaning fast lookups and minimal data transfer.  

Between the second and third iterations, we made a poster of the entire travels
of Clicky.  You can purchase one from me for \$60.  I wish I were kidding, but
I'd do that.

Well, what are you waiting for? Go visit Clicky

{{ biglink('http://mattbierbaum.com', 'Clicky') }}

