=============
Control Flows
=============

Programs often move around in code and data:

- If something is true, do this line

- Re-use a section of code

- Step through a series of items

- Bring in some external code

Let's look at these.

Conditionals with ``if``
========================

Maybe we want to print a special greeting if it's you.

.. code-block:: python

    greeting = 'Hello'
    name = 'Malo'

    if name == 'Malo':
        print('Welcome back Malo')
    else:
        print(greeting + ' ' + name)

Remember *expressions* from the previous page? We used the expression
``name == 'Malo'`` as the test. In this case, that expression produces
the value ``True``.

Learned
-------

- ``if/then`` using an if statement

- Provide an expression that has to produce ``True`` for the first branch

Functions
=========

Here we go, one of the most important things for game writing: re-usable
code sections using *functions*. In Python, a function is:

- A series of one more more lines (indented)

- With a name for the function

- And zero or more *arguments* to the function

- The function produces a *return value*

Let's make a function ``greet`` which will produce the string to print.

.. code-block:: python

    greeting = 'Hello'

    def greet(name):
        if name == 'Malo':
            result = 'Welcome back Malo'
        else:
            result = greeting + ' ' + name

        return result

    msg = greet('Malo')
    print(msg)

Let's analyze this:

- Function named ``greet``

- Function has one *argument* that it expects to be given -- ``name``

- 4 lines of code in the function *body*

- A return value

- We *call* the function with an *argument* of ``Malo``

- We store the return value in a *variable* named ``msg``

- We then print the variable ``msg``

Learned
-------

- Functions are re-usable sections of code

- They take arguments and generate return values

Lists
=====

So far our values have been a simple type: a string, an integer.
Sometimes we need a list of things. For example, instead of just
one possible greeting, a list of greeting choices.

Let's make a list of greetings, then select the 3rd greeting.
Remember to change the argument we pass to ``greet``:

.. code-block:: python

    greetings = ['Hello', 'Howdy', 'Wassup']

    def greet(name):
        if name == 'Malo':
            result = 'Welcome back Malo'
        else:
            result = greetings[2] + ' ' + name

        return result

    msg = greet('World')
    print(msg)

``greetings[2]`` is also the last item in the list. We could
grab it using the "count backwards" notation using
``greetings[-1]``.

Learned
-------

- "List" is a variable type that can hold more than one value

- You select an item from the list using the square-bracket notation

- Counting starts from zero

- You can also count backwards

Imports
=======

Your code uses stuff built into Python. But you can also use other code
from a *library*. Python ships with a standard library that you can
use by *importing* code from the standard library.

Let's import the ``choice`` function from the ``random`` module in
the standard library, then select a random greeting.

    from random import choice

    greetings = ['Hello', 'Howdy', 'Wassup']

    def greet(name):
        if name == 'Malo':
            result = 'Welcome back Malo'
        else:
            result = choice(greetings) + ' ' + name

        return result

    msg = greet('World')
    print(msg)


Learned
-------

- A *library* contains *modules* that can be imported

- Modules contain functions and more that can be reused

- You can use the ``import random`` syntax to get the whole module

- Or, ``from random import choice`` to get just one function from
  the module
