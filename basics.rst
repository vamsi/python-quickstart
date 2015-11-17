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

    print "Hello, World!"

And run this program by calling ``python hello.py``. Make sure you change to
the directory where you saved the file before doing it.

.. code-block:: python

    VamsiVihar:desktop ~$ python hello.py
    Hello, World!
    VamsiVihar:desktop ~$




Dynamically Typed
-----------------
Python is a dynamic-typed language. Many other languages are static typed, such as C/C++ and Java.

A static typed language requires the programmer to explicitly tell the computer
what type of “thing” each data value is. For example, in C if you had a variable
that was to contain the price of something, you would have to declare the variable
as a “float” type. This tells the compiler that the only data that can be used for
that variable must be a floating point number, i.e. a number with a decimal point.
If any other data value was assigned to that variable, the compiler would give an
error when trying to compile the program.


Variables
---------
In Python there are no declarations.

.. note::

    Everything thing is a object in Python


Assignment
----------


One of the most important kinds of statements in Python is the assignment statement. One of the most important kinds of statements in Python is the assignment statement.Assignment to a variable ``(e.g.,name=value)`` is how you create a new variable or rebind an existing variable to a new value.


The assignment statement in the simplest form has the syntax:

.. code-block:: python

    <variable> = <value>
    <variable> = <expr>

``variable`` is your variable to which holds the ``value`` of the ``expression``



Indentation
-----------

Python forces the user to program in a structured format. Code blocks are determined by the amount of indentation used.


As you’ll recall from the comparison of programming languages brackets and semicolons were used to show code grouping or end-of-line termination for the other languages.


Python doesn’t require those, **indentation** is used to signify where each code block starts and ends.
Whitespace is important in Python. Actually, whitespace at the beginning of the line is important. This is called indentation. Leading whitespace (spaces and tabs) at the beginning of the line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements.


This means that statements which go together must have the same indentation. Each such set of statements is called a block.
One thing you should remember is that wrong indentation can give rise to errors. For example:

Example(``indent.py``)

::

    i = 5
    # Error below! Notice a single space at the start of the line
      print 'Value is ', i
    print 'I repeat, the value is ', i

When you run this, you get the following error:

.. code-block:: python

    File "indent.py", line 5
      print 'Value is ', i
      ^
    IndentationError: unexpected indent

Notice that there is a single space at the beginning of the second line. The error indicated by Python tells us that the syntax of the program is invalid i.e. the program was not properly written. What this means to you is that you cannot arbitrarily start new blocks of statements (except for the default main block which you have been using all along, of course). Cases where you can use new blocks will be detailed in later chapters such as the Control Flow.

How to indent ?
---------------


Use four spaces for indentation. This is the official Python language recommendation. Good editors will automatically do this for you. Make sure you use a correct number of spaces for indentation, otherwise your program will show errors.


Printing Output
~~~~~~~~~~~~~~~~

Let's now output some variables by assigning them some values and with some strings

Example (save it as ``printing.py``)

::

    i = 999
    p = "PyQuick"
    print(i)
    print(p)
    print("Hello World !!!")
    print("Hello !!!")
    print("Hello Python")
    print("Welcome")


Output

.. code-block:: python

    $ python printing.py
    999
    PyQuickMINI
    Hello World !!!
    Hello !!!
    Hello Python
    Welcome


Input and Output
~~~~~~~~~~~~~~~~

There will be situations where your program has to interact with the user. For example, you would want to take input from the user and then print some results back. We can achieve this using the raw_input() function and print statement respectively.


Example (save it as ``input.py``)

::

    a = raw_input("Enter something")
    print("You have entered the below")
    print(a)

Output

.. code-block:: python

    $ python input.py
    Enter something
    Hello I am Your New Programming Language
    You have entered the below
    Hello I am Your New Programming Language
