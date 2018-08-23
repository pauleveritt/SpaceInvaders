============
Handle Input
============

Our ball moves. Let's get it to respond to user input: when pressing
a key, reverse direction. In fact, let's move left/right/up/down.

After this, the ball will *only* move when pressing a key. Thus, we
need to handle:

- Pressing a key down

- Releasing the key

.. literalinclude:: handle_input.py
    :linenos:
    :emphasize-lines: 11, 14, 22, 26, 41, 50-64

Analysis
========

#. *Line 11*. We are no longer going to hand "velocity" to the
   ``Player``, so remove that argument from the constructor.

#. *Line 14*. The player no longer starts in motion.

#. *Line 22*. No longer pass the velocity when instantiating a
   ``Player``.

#. *Line 26*. Need to handle ``y`` as well as ``x``.

#. *Line 50, 60*. These are *event handlers*. Whenever a key is
   pressed or released, Arcade will call this specially-named
   method on our class. *With* arguments about what is being
   pressed.

#. *Line 51*. Was the ``UP`` key pressed? If so, change the
   player's delta_y by the amount in ``MOVEMENT_SPEED``.

#. *Line 52*. The ``elif`` only executes when the ``if`` is
   ``False``.

#. *Line 62*. When the key is released, reset the appropriate
   ``delta`` to the "not moving" state.

Test
====

#. What if we have a typo in the method name for our key press
   handler?

#. What does "modifiers" do? (Use a ``print()`` or even better,
   the PyCharm debugger, to see.)

Extra Credit
============

#. Let's change it to have ``Shift`` mean, move that direction
   at a much faster speed.

#. Re-type the event handlers, but from memory.