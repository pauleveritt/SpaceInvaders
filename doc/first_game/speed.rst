=====
Speed
=====

Our ball moves in a hard-wired speed of one pixel per frame update.
Let's parameterize that to see how velocity is stored.

.. literalinclude:: speed.py
    :linenos:
    :emphasize-lines: 6, 24

Analysis
========

#. We add a constant to dictate the speed of movement.

#. We change the ``update`` method -- remember, this is called on
   **every frame update** -- to change the x position.

Test
====

#. Why does the ball move on the screen? Explain the process of what is
   happening as the program runs

#. Print the ``delta_time`` to see how the value changes on each frame
   update.
