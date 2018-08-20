========================
Dictionaries and Classes
========================

Our games will have richer types of data. Let's look at two of the
most common variable types:

- A *dictionary* is like a phone book...get the value of some name

- A *class* models a *thing* you're designing...with data and logic

Dictionary
==========

We did a little phonebook before, with phone numbers in a list. But it
isn't convenient to get a phone number by index position:

.. code-block:: python

    phone_numbers = ['368-2222', '429-3333', '429-4444']
    paul = phone_numbers[1]

With a real phone book, you look up a *name* to get a number. In Python,
this is called a *dictionary*. It uses ``{}`` instead of ``[]``.

.. code-block:: python

    phone_book = {
        'home': '368-2222',
        'dad': '429-3333',
        'mom': '429-4444'
    }

    # Or, on on line
    phone_book = {'home': '368-2222', 'dad': '429-3333', 'mom': '429-4444'}

If you want a value, you can now use the dictionary *key* to get the
*value* for that key:

.. code-block:: python

    phone_book = {
        'home': '368-2222',
        'dad': '429-3333',
        'mom': '429-4444'
    }

    # Or, on on line
    phone_book = {'home': '368-2222', 'dad': '429-3333', 'mom': '429-4444'}
    print(phone_book['home'])

Once the dictionary is created, you can add a new item using an assignment.
You can also delete an item. If you try to get a non-existing item, Python
will raise an error.

.. code-block:: python

    phone_book['mobile'] = '429-5555'
    print(phone_book['mobile'])
    del phone_book['mobile']
    print(phone_book['mobile'])


Learned
-------

- Use a dictionary to lookup a *value* using a *key*

- Created with curly braces instead of square braces

- Access/add/delete an item to a dictionary using square braces

Classes
=======

Strings are very focused: one little value. Lists and dictionaries are
bigger: a collection of values. A function is like a collection of lines
of code.

Sometimes we want something bigger. A collection of values *and* a
collection of code, with a clear name, representing a *thing* we want
to work with.

This is called a *class*. You write a class, then make *instances* of
that class to work on. It's like the cookie template that makes a a bunch
of similar cookies.

Let's make a phone book for people, then use that in our dictionary.

.. code-block:: python

    class Person:
        pass

    mom = Person()
    dad = Person()
    me = Person()
    phone_book = {'me': me, 'mom': mom, 'dad': dad}
    print(phone_book['me'].name)

Works, but...BORING! ``Person`` is empty. Let's give each person a name.

.. code-block:: python

    class Person:
        pass

    mom = Person()
    mom.name = 'Mom'
    dad = Person()
    dad.name = 'Dad'
    me = Person()
    me.name = 'Me'
    phone_book = {'me': me, 'mom': mom, 'dad': dad}
    print(phone_book['me'].name)

We can now get the name of the person from the phone book, as we showed.
But ``name`` wasn't part of the class. We did it ad-hoc, on each instance.
There's no *contract* saying a ``Person`` instance must have a name.

Let's make that contract. Classes have a special function called a
*constructor* which governs how they are..well, constructed. A function
that is part of a class is called a *method* because the function is
part of the class.

Let's use the special ``__init__`` method (pronounced *dunder init*) which
acts as the constructor:

.. code-block:: python

    class Person:
        def __init__(self, name):
            self.name = name

    mom = Person('mom')
    dad = Person('dad')
    me = Person('me')
    phone_book = {'me': me, 'mom': mom, 'dad': dad}
    print(phone_book['me'].name)

Thanks to the constructor, you can't "construct" an instance without
a name:

.. code-block::

    sister = Person()

The data on an class are called *attributes*. ``name`` is an attribute
of the class (or, once constructed, an attribute on the instance.)

Our class has data (``name``) but not much logic. Let's make a greeting:

.. code-block:: python

    class Person:
        def __init__(self, name):
            self.name = name

        def greeting(self, msg):
            return msg + ' ' + self.name

    mom = Person('mom')
    dad = Person('dad')
    me = Person('me')
    phone_book = {'me': me, 'mom': mom, 'dad': dad}
    print(phone_book['me'].greeting('Hello'))

Learned
-------

- Classes model a thing that has data and logic

- Classes construct instances, like a cookie template makes cookies

- Class data are called *attributes* and logic are called *methods*

- A class stamps out new instances using a *constructor*

- In Python, the constructor is the special method ``__init__``

- You pass arguments to dunder-init to store attributes on the instance
  during construction

- A method is a function that is bound to the class, and always has
  ``self`` as the first argument

- ``self`` refers to the instance of the class

The Main Block
==============

One last bit of housekeeping. You've been running a Python file, aka
a *module*. We also saw how you can re-use modules via import.

If you import your current module from another module, all the lines
would immediately execute. Probably not what you want. The "main block"
is a way to tell if your module is being run directly, or imported.

.. code-block:: python

    class Person:
        def __init__(self, name):
            self.name = name

        def greeting(self, msg):
            return msg + ' ' + self.name

    def main():
        mom = Person('mom')
        dad = Person('dad')
        me = Person('me')
        phone_book = {'me': me, 'mom': mom, 'dad': dad}
        print(phone_book['me'].greeting('Hello'))

    if __name__ == '__main__':
        main()

This looks for the special built-in variable ``__name__``. If it has
a value of ``__main__``, that means Python is running this module as
the "main" module. I.e. directly executing.

This lets you import ``Person`` from another module. The code in ``main``
is only run when you directly execute this module.

Learned
-------

- Why you might want some code to run on import vs. execution

- How to detect when your module is directly run

