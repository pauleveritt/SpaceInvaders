=========
Move Ball
=========

We now do something our function-based version didn't do: animation.

By implementing a method ``update``, we can work on the data that
drives our drawing in ``on_draw``.

.. literalinclude:: game05.py
    :linenos:
    :emphasize-lines: 13, 20, 22-23

Analysis
========

- Line 13 stores the x position of the circle at startup.

- Line 20 now uses that attribute's value, instead of hardwiring a
  single value.

- As that value changes, the circle moves.

- Line 23 moves the ball by one pixel on every call to ``update``, which
  is approximately 60 times per second.

Test
====

- Our class now has some state (data), with one attribute it is tracking.
  What variable is this?

- ``update`` is passed the "delta time", meaning, the elapsed time since
  the last time update was called. Use ``print`` to see what that value
  looks like.

