===========
Preparation
===========

Let's get some Python basics out of the way:

- Printing

- Values

- Types

- Expressions

- Variables

Printing Values
===============

``print()`` is a function that puts stuff on the screen. Let's have it
print a string saying ``Hello World``:

.. code-block:: python

    print('Hello World')

The value is inside the parentheses. Values have *types* -- a string, an
integer, etc. In this case, the value we gave ``print()`` was a *string*.

Let's print an integer:

.. code-block:: python

    print(42)

Finally, a *boolean*. ``True`` and ``False`` are special symbols in Python,
representing what they say:

.. code-block:: python

    print(42)

Learned
-------

- The print function sends a value to the screen

- Values have a type

- Common types: string, integer, boolean

Expressions
===========

Sometimes you need to compute something. Python expressions are a way to
compose a value from multiple values, conditions, or operations.

This expression results in a boolean:

.. code-block:: python

    print(True is False)

This expression does a comparison:

.. code-block:: python

    print('hello' == 42)

This expression combines two strings into a new value:

.. code-block:: python

    print('Hello ' + 'World')

This expression adds two numbers:

.. code-block:: python

    print(1 + 1)

Learned
-------

- **Expressions** make new **values**

- Can have comparisons, string combination, addition, etc.

Variables
=========

We've seen values and expressions that make values. We immediately printed
them. What if we want to store the value, to use it later?

This is a variable: hold a value in a symbol:

.. code-block:: python

    greeting = 'Hello'
    name = 'Paul'
    print(greeting + ' ' + name)

Learned
-------

- A *variable* points to a value