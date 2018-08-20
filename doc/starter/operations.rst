==========
Operations
==========

Python has a number of ways to work on values and variables. We saw the
``+`` sign. These are called operations.

Inline Operator
===============

What if we want to operate on a variable *and* assign the result? You can
do this the long way:

.. code-block:: python

    x = 1
    x = x + 1

Python provides an inline operator:

.. code-block:: python

    x = 1
    x += 1

This increases the value of ``x`` by 1, then assigns that value to
``x``. We can do other variations of this:

.. code-block:: python

    x = 1
    x += 1
    x += 5
    x -= 1
    x *= 5

Learned
-------

- The ``+=`` and ``-=`` operators will be very useful in changing
  the position of a sprite

Sequences: Strings and Lists
============================

We looked at lists already:
``greetings = ['Hello', 'Howdy', 'Wassup']``. We also looked at strings:
``greeting = 'Hello'``.

Turns out that these two types -- string and list -- are both types of
the *sequence* type. Sequences have operations:

.. code-block:: python

    greetings = ['Hello', 'Howdy', 'Wassup']
    greeting = 'Hello'
    print(greetings[0])
    print(greeting[0])

You can grab a *slice* of a sequence using the slice operator:

.. code-block:: python

    greeting = 'Hello'
    print(greeting[0:2])

When you take a slice of a sequence, you get a sequence. In this case,
a string. But taking a slice of a list returns a list:

.. code-block:: python

    greetings = ['Hello', 'Howdy', 'Wassup']
    print(greetings[0:2])

You can also do the ``-`` position to count from the end:

.. code-block:: python

    greetings = ['Hello', 'Howdy', 'Wassup']
    print(greetings[-1:-1])

Learned
-------

- Strings and lists are *sequences*

- Sequences can be sliced to extract a portion of the sequence

Walking Through a List with ``for``
===================================

What if we want to operate on a each item in a list. Imagine a
phone book:

.. code-block:: python

    phone_numbers = ['368-2222', '429-3333', '429-4444']

Let's use ``for`` to loop through each phone number and temporarily
assign it to a variable name ``phone_number``:

.. code-block:: python

    phone_numbers = ['368-2222', '429-3333', '429-4444']
    for phone_number in phone_numbers:
        output = 'Number: ' + phone_number
        print(output)

This does several things:

- Using ``phone_numbers`` as the sequence

- Assign each sequence item to ``phone_number``

- Then execute the indented block of code for each
  loop through the sequence

Learned
-------

- The ``for`` operator loops through a sequence

- A variable is created and assigned

- A code block is executed on each loop

Range
=====

Sometimes you need a temporary list created. Let's say you want to do
something 50 times. It would suck to make a list from 0 to 49, just
iterate through it.

Python has the ``range`` function that can generate a list for you.

.. code-block:: python

    for i in range(50):
        print(i)

This starts at zero. Let's start at 10, and also say "count by 2":

.. code-block:: python

    for i in range(10, 50, 2):
        print(i)

Learned
-------

- The ``range`` function will let us make 50 enemy sprites

- Sometimes, like for explosions, we want to skip over some
  using the step parameter

