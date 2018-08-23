======
Player
======

No new functionality here, but a big refactoring: let's move the ball
out of the game and have ``MyGame`` and ``Player``. For now, the ``Player``
will simply be a filled circle.

We'll also start putting our ``setup`` method to work.

.. literalinclude:: player.py
    :linenos:
    :emphasize-lines: 7, 10-25, 29, 33, 37-40, 44, 47

Analysis
========

#. We make the player color a constant.

#. We define a new "kind of thing", meaning a new class. The ``Player``
   class controls the data and logic for our "Player".

#. Construct a new ``Player`` by handing it an initial x/y starting
   position, how fast (and which direction) to move, then radius and
   color.

#. *Important* idea...the *Player* now draws and updates itself. The
   ``MyGame`` class doesn't know the details about the ``Player``.

#. *Line 29*. Use the "type hint" notation to declare that ``MyGame``
   will have an attribute ``player`` of type ``Player``.

#. *Lines 38-39*. Get the center of the screen.

#. *Line 40*, we declared ``player`` on line 29, here's where we
   actually create a ``Player`` and store it as ``self.player``.

#. *Line 44, 47*. The game's drawing and animation methods now change
   to tell the player to draw and update itself.

Test
====

#. Use a different policy for the starting position of the player,
   instead of "middle of the screen".

#. What happens if the window is resized? Does the starting position
   change?

#. Make the player move to the left instead of to the right.

#. What happens if you assign ``velocity`` to ``delta_y`` on line 15?

#. You told Python that ``self.player`` was a ``Player``. What happens
   if, on line 40, you assign say an integer? Does Python throw
   an exception?