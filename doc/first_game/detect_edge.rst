===========
Detect Edge
===========

Let's handle 4 keypresses (up, down, left, right) and detect when we are
at the edge. If at an edge, "stop".


.. literalinclude:: detect_edge.py
    :linenos:
    :emphasize-lines: 28-42

Analysis
========

#. *Line 30*. The formula for detecting if we are at the *left*:

   - If the *center* of our circle (``self.x``)...

   - ...is within a *radius-length* of the edge (zero)

#. *Line 31*. What do we do? Reset the circle's x position to be
   a radius-length *to the right* of the left edge.