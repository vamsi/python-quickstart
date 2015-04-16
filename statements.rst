.. highlight:: python
    :linenothreshold: 0

Statements
==========


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



if python:
----------





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


::

    $ python evenodd.py
    enter any number:7
    The entered number 7 is odd
    $ python evenodd.py
    enter any number:54
    The entered number 54 is even



::

    a,b = input("Enter a,b values:")
    if(a>b):
        print "The largest number is",a
    else:
        print "The largest number is",b

::

    $ greaterlesser.py
    Enter a,b values:54 7
    The largest number is 54
    $ greaterlesser.py
    Enter a,b values:6 27
    The largest number is 27




for loop in "python":
---------------------


The "for" statement in Python differs a bit from what you may be used to in C.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user
the ability to define both the iteration step and halting condition (as C),the for loop in python works a bit different.


The "for" loop in Python has the ability to iterate over the items of any sequence,such as a list or a string.
As mentioned earlier,the Python for loop is an iterator based for loop.


It steps through the items in any ordered sequence list,i.e. string, lists, tuples, the keys of dictionaries and other iterables.
The Python for loop starts with the keyword "for" followed by an arbitrary variable name, which will hold the values of the
following sequence object, which is stepped through.


The general syntax of a "for" loop in "python" is as follows:


::

    for variable in sequence:
       statements(s)

If a sequence contains an expression list, it is evaluated first.Then, the first item in the sequence is assigned to the iterating variable 'variable'.
Next, the statements block is executed.


Each item in the list is assigned to variable, and the statement(s) block is executed until the entire sequence is exhausted.
The items of the sequence object are assigned one after the other to the loop variable; to be precise the variable points to the items.


For each item the loop body is executed.


::



The range() Function:
^^^^^^^^^^^^^^^^^^^^^

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.


The built-in function range() is the right function to iterate over a sequence of numbers.


It generates an iterator of arithmetic progressions.


range(n) generates an iterator to progress the integer numbers starting with 1 and ending with (n -1).


To produce the list with these numbers, we have to cast rang() with the list().
range() can be called with two arguments:

::

    range(begin,end)

::

    print("Enter any num:")
    num = input()
    fact = 1
    for i in range(1,num):
        fact = fact*i
    print "Factorial of",num,"is:",fact

::

    $ factorial.py
    Enter any num:6
    Factorial of 6 is:720
    $ factorial.py
    Enter any num:7
    Factorial of 7 is:5040

The above call produces the list iterator of numbers starting with begin (inclusive) and ending with one less than the number "end".

while python:
-------------

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.
While loops, like the ForLoop, are used for repeating sections of code - but unlike a for loop, the while
loop will not run n times, but until a defined condition is met.

The syntax of a while loop in Python programming language is:

::

    while expression:
    statement(s)



Here, statement(s) may be a single statement or a block of statements.


The condition may be any expression, and true is any non-zero value.


The loop iterates while the condition is true.
When the condition becomes false, program control passes to the line immediately following the loop.

In Python, all the statements indented by the same number of character spaces after a programming construct
are considered to be part of a single block of code.


Python uses indentation as its method of grouping statements.


Here, key point of the while loop is that the loop might not ever run.
When the condition is tested and the result is false, the loop body will be skipped and the first statement
after the while loop will be executed.

::

    a = input("Enter a number")
    i = fact = 1
    while i<=a:
        fact = fact*i
        i = i+1
    print(fact)


::

    $ python while-factorial.py
    Enter a Number
    5
    125



The Infinite Loop:


A loop becomes infinite loop if a condition never becomes false.
You must use caution when using while loops because of the possibility that this condition never resolves to a false value.
This results in a loop that never ends.
Such a loop is called an infinite loop.

An infinite loop might be useful in client/server programming where the server needs to run continuously
so that client programs can communicate with it as and when required.


pass
----

break, continue
---------------
