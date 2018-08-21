===============
Import and Main
===============

Let's plant the seeds and get the basics in place:

.. literalinclude:: game01.py

Analysis
--------

We've seen this stuff before:

- ``arcade`` is a *library* so we need to *import* it

- At the bottom, we have a conditional using ``if``

- This is the "main block" sniffer. We look for the magic name
  ``__name__`` and see its value

- If the value is ``__main__``, Python is executing your script
  directly

- We have a "call" to a function (``main()``)

- We define the function using ``def main()``

- This function takes no arguments as inputs

- The ``main`` function prints a value...the ``__name__`` attribute of
  the ``arcade`` library

- ``main`` has no ``return`` keyword, so implicitly, the return
  value is ``None``

Test
----

#. What happens if you fail to import the ``arcade`` library?

#. What other magic variables are available besides ``__name__``?
   (Hint: add ``print(dir())`` as the last line, not indented.)

#. The ``if`` has no ``else``. So what happens when the expression
   isn't ``True``?

#. Assign the result of calling main to a variable, then print it.

#. What other attributes are available on ``arcade``? (Hint: use
   ``print`` and ``dir`` again, but pass ``arcade`` as an
   argument to ``dir``.

#. What happens if you pass an argument to ``main`` by mistake?

#. What happens if you ask for an argument in ``main`` but don't
   provide it?