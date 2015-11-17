.. highlight:: python
    :linenothreshold: 0

Control Flow
============


Table for Quick Glance of Conditional and Control Flow Statements


+--------------------------+-------------------------+
|      Statement           |         Role            |
+==========================+=========================+
|   if/else/elif           |    Selection Actions    |
+--------------------------+-------------------------+
|       for                |    Sequence Iterations  |
+--------------------------+-------------------------+
|      while               |       General Loop      |
+--------------------------+-------------------------+
|   break, continue        |       Loop Jumps        |
+--------------------------+-------------------------+
|       pass               |   Empty Place Holder    |
+--------------------------+-------------------------+



Conditionals
------------

if Tests:
~~~~~~~~~

One of the most common control structures you’ll use, and run into in other programs, is the if conditional block. Simply put, you ask a yes or no question; depending on the answer different things happen.

Let’s start by getting the computer to make a simple decision. For an easy example, we will make a program to find the largest of two numbers


Example (save it as ``greaterlesser.py``)

::

    a,b = input("Enter a,b values:")
    if(a>b):
        print "The largest number is",a
    else:
        print "The largest number is",b


Output

.. code-block:: python

    $ python greaterlesser.py
    Enter a,b values:54 7
    The largest number is 54
    $ python greaterlesser.py
    Enter a,b values:6 27
    The largest number is 27

Example (save it as ``evenodd.py``)

::

    print("enter any number:")
    num = input()
    if(num>0):
        if ((num%2)==0):
            print "The entered number",num,"is even"
        else:
            print "The entered number",num,"is odd"
    else:
        print("Enter positive number")


Output

.. code-block:: python

    $ python evenodd.py
    enter any number:7
    The entered number 7 is odd
    $ python evenodd.py
    enter any number:54
    The entered number 54 is even

Table Illustrating the syntax for all the Decision Making in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+------------------------+------------------------+
|  Simple Decision       |  Two Way Decision      |  Multiway Decision     |
+========================+========================+========================+
|.. code-block:: python  |.. code-block:: python  |.. code-block:: python  |
|                        |                        |                        |
|    if <condition>:     |    if <condition>:     |     if <condition1>:   |
|        <statements>    |        <statements>    |         <stametemts>   |
|                        |    else:               |     elif <condition2>: |
|                        |        <statements>    |         <statements>   |
|                        |                        |     elif <condition3>: |
|                        |                        |          <statements>  |
|                        |                        |     ......             |
|                        |                        |                        |
|                        |                        |     else:              |
|                        |                        |         <statements>   |
|                        |                        |                        |
+------------------------+------------------------+------------------------+

As we already dealt with some Simple decision and Two way decision This example shows the way for the Multiway decision handling in Python


Looping
-------

for loop in "python":
~~~~~~~~~~~~~~~~~~~~~


The `for` statement in Python differs a bit from what you may be used to in C.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user
the ability to define both the iteration step and halting condition (as C),the for loop in python works a bit different.


The "for" loop in Python has the ability to iterate over the items of any sequence,such as a list or a string.
As mentioned earlier,the Python for loop is an iterator based for loop.


It steps through the items in any ordered sequence list,i.e. string, lists, tuples, the keys of dictionaries and other iterables.
The Python for loop starts with the keyword "for" followed by an arbitrary variable name, which will hold the values of the
following sequence object, which is stepped through.


The general syntax of a "for" loop in "python" is as follows:


.. code-block:: python

    for variable in sequence:
        statements(s)

If a sequence contains an expression list, it is evaluated first.Then, the first item in the sequence is assigned to the iterating variable 'variable'.
Next, the statements block is executed.


Each item in the list is assigned to variable, and the statement(s) block is executed until the entire sequence is exhausted.
The items of the sequence object are assigned one after the other to the loop variable; to be precise the variable points to the items.


For each item the loop body is executed.



The range() Function:
~~~~~~~~~~~~~~~~~~~~~

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
The built-in function range() is the right function to iterate over a sequence of numbers.


It generates an iterator of arithmetic progressions.range(n) generates an iterator to progress the integer numbers starting with 1 and ending with (n -1).


To produce the list with these numbers, we have to cast rang() with the list().
range() can be called with two arguments:


.. code-block:: python

    range(begin,end)

Example (save it as ``factorial.py``)

::

    print("Enter any num:")
    num = input()
    fact = 1
    for i in range(1,num):
        fact = fact*i
    print "Factorial of",num,"is:",fact


.. code-block:: python

    $ python factorial.py
    Enter any num:6
    Factorial of 6 is:720
    $ python factorial.py
    Enter any num:7
    Factorial of 7 is:5040

The above call produces the list iterator of numbers starting with begin (inclusive) and ending with one less than the number "end".

while python:
~~~~~~~~~~~~~

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.
While loops, like the ForLoop, are used for repeating sections of code - but unlike a for loop, the while
loop will not run n times, but until a defined condition is met.

The syntax of a while loop in Python programming language is:

.. code-block:: python

    while expression:
        statement(s)



Here, statement(s) may be a single statement or a block of statements.


The condition may be any expression, and true is any non-zero value.


The loop iterates while the condition is true.
When the condition becomes false, program control passes to the line immediately following the loop.

In Python, all the statements indented by the same number of character spaces after a programming construct
are considered to be part of a single block of code.


Python uses ** indentation ** as its method of grouping statements.


Here, key point of the while loop is that the loop might not ever run.
When the condition is tested and the result is false, the loop body will be skipped and the first statement
after the while loop will be executed.

Example (save it as ``while-factorial.py``)

::

    a = input("Enter a number")
    i = fact = 1
    while i<=a:
        fact = fact*i
        i = i+1
    print(fact)


.. code-block:: python

    $ python while-factorial.py
    Enter a Number
    5
    125

break
~~~~~

The break statement is used to break out of a loop statement i.e. stop the execution of a looping statement, even if the loop condition has not become False or the sequence of items has not been completely iterated over.

An important note is that if you break out of a for or while loop, any corresponding loop else block is not executed.

Example (save as ``break.py``):

::

    while True:
        s = raw_input('Enter something : ')
        if s == 'quit':
            break
        print 'Length of the string is', len(s)
    print 'Done'

Output:

.. code-block:: python

    $ python break.py
    Enter something : Programming is fun
    Length of the string is 18
    Enter something : When the work is done
    Length of the string is 21
    Enter something : if you wanna make your work also fun:
    Length of the string is 37
    Enter something : use Python!
    Length of the string is 11
    Enter something : quit
    Done



continue
~~~~~~~~
The continue statement is used to tell Python to skip the rest of the statements in the current loop block and to continue to the next iteration of the loop.

Example (save as ``continue.py``):

::

    while True:
        s = raw_input('Enter something : ')
        if s == 'quit':
            break
    if len(s) < 3:
        print 'Too small'
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here...

Output:

::

    $ python continue.py
    Enter something : a
    Too small
    Enter something : 12
    Too small
    Enter something : abc
    Input is of sufficient length
    Enter something : quit


pass
~~~~

pass is a null operation. when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed,

For example:

::

    def f(arg):    # a function that does nothing (yet exists)
        pass

::

    class C:
        pass       # a class with no methods (yet exists)

    class A(ABSDBASBD,IAUSDBDBD):
        pass
