.. highlight:: python
    :linenothreshold: 0


The Basics
===========



Installation Instructions
-------------------------
Python runs mostly on all modern operating systems.

Windows - `http://docs.python-guide.org/en/latest/starting/install/win/
<http://docs.python-guide.org/en/latest/starting/install/win/>`_


GNU/Linux - `http://docs.python-guide.org/en/latest/starting/install/linux/
<http://docs.python-guide.org/en/latest/starting/install/linux/>`_


Mac OSX - `http://docs.python-guide.org/en/latest/starting/install/osx/
<http://docs.python-guide.org/en/latest/starting/install/osx/>`_




Running Python Interpreter
--------------------------

Python comes with an interactive interpreter. When you type ``python`` in your
shell or command prompt, the python interpreter open up with a ``>>>``
prompt and waiting for your instructions.

``>>>`` says that your are inside the python interpreter


.. code-block:: python

    $ python
    Python 2.7.6 (default, Apr 24 2015, 09:38:35)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>



Running Python Scripts
----------------------

Open your text editor, type the following text and save it as ``hello.py``.

.. code-block:: python

    print "hello, world!"

And run this program by calling ``python hello.py``. Make sure you change to
the directory where you saved the file before doing it.

.. code-block:: python

    VamsiVihar:desktop ~$ python hello.py
    hello, world!
    VamsiVihar:desktop ~$




Dynamically Typed
-----------------
Python is a dynamic-typed language. Many other languages are static typed, such as C/C++ and Java.

A static typed language requires the programmer to explicitly tell the computer what type of “thing” each data value is.

For example, in C if you had a variable that was to contain the price of something, you would have to declare the variable as a “float” type.

This tells the compiler that the only data that can be used for that variable must be a floating point number, i.e. a number with a decimal point.

If any other data value was assigned to that variable, the compiler would give an error when trying to compile the program.


Variables
---------
In Python there are no declarations. The existence of a variable begins with a statement that binds the variable, or, in other words, sets a name to hold a reference to some object.

.. note::
    Everything thing is a object in Python


Assignment
----------

Assignment statements can be plain or augmented.

Assignment to a variable ``(e.g.,name=value)`` is how you create a new variable or rebind an existing variable to a new value.


The assignment statement in the simplest form has the syntax:

::

    target = expression


``target`` is your variable to which holds the ``value`` of the ``expression``

Indentation
-----------
Python forces the user to program in a structured format.Code blocks are determined by the amount of indentation used.


As you’ll recall from the comparison of programming languages chapter, brackets and semicolons were used to show code grouping or end-of-line termination for the other languages.


Python doesn’t require those,**indentation** is used to signify where each code block starts and ends.
