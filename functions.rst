.. highlight:: python
    :linenothreshold: 0


Functions
=========

A Function

Function is small unit of computation which may take arguments and may return values.


Function body should be indented like if statement.


Python has lot of builtin functions.

We use def keyword to define a function. General syntax is like

::

    def functionname(params):
        statement1
        statement2
        .....


A Simple Python Functions

Simple Python Function taking no arguments


::

    # Function to say hello on call the function


    def hello():
        print("Hello")

    hello() # calling the function hello

Simple Python Function taking in arguments


::

    # Function calculating the square of a number


    def square(x):
        print (x*x)

    square(24) # Here the Square Function is called



More Illustrations
------------------

Let us write a Function to add two strings and add two numbers



::

    # Function Adding Numbers and Concatination of Strings


    def add(x,y):
        print(x+y)

    add("hello","world") # Add Function is called with Two Strings

    add(3,5) # Add Function is Two Numbers Here

Output


Functions Returning Values


Recursions
----------


::

    # Functions Illustrating Fibonacci

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2) # Recursive Function Call


    print(fibonacci(7)) # Printing the result by passing the variable 3 to the Function fibonacci
