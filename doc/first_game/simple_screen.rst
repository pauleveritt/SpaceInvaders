=============
Simple Screen
=============

That was still boring. No screen! Let's make some changes to have our
*module* pop up a window:

- Height and width

- Window title

- Background color

.. literalinclude:: game02.py
    :linenos:
    :emphasize-lines: 3-4, 8-12

Analysis
========

*Lines 3-4*. We define some *constants* to make it easy to customize
the game. Constants are variables that aren't meant to change during
the program.

*Line 8*. We call a function in the ``arcade`` library to open a
window. We provide this function 3 *function arguments*.

Test
====

#. Use PyCharm to see what other arguments can go to open window. Put
   cursor in between parentheses and do Ctrl-Q.