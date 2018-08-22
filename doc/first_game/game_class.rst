==========
Game Class
==========

Time to switch from simple drawing to using a Python *class* for
writing our game.

.. literalinclude:: game04.py
    :linenos:
    :emphasize-lines: 8-24

This version does exactly the same thing as the previous, function-based
version, but as a class.

Analysis
========

#. We make a class ``MyGame`` and subclass from ``arcade.Window``. This
   let us re-use most of what's needed.

#. We have a ``__init__``, but so does our base class ``arcade.Window``.
   We need to call it, and let it help setup our instances. ``super()``
   lets us do that.

#. ``setup`` is useful for restarting a game. We can ignore it for quite
   a while.

#. Arcade expects our ``MyGame`` class to implement an ``on_draw`` method
   that does the actual drawing on the screen.

Test
====

#. What class does our game inherit from (meaning, its superclass)?

#. Why do we call ``super().__init()`` in our dunder-init?

#. What are the three methods in our ``MyGame`` class?

#. Why does ``update`` have ``self`` as a first argument?

#. What are all the possible arguments you can supply to
   ``arcade.Window.__init__``? (Hint: click on it and hit
   ``Ctrl-Q``.

#. Put the cursor on the ``__init__`` in ``super().__init__``
   and hit ``Ctrl-B``. This navigates you to the code for the
   Arcade Window's constructor.