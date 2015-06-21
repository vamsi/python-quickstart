.. highlight:: python
    :linenothreshold: 0


Functions
=========

Function is small unit of computation which may take arguments and may return values. Function body should be **indented** like if statement. Python has lot of builtin functions.


The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.


We use def keyword to define a function. General syntax is like

::

    def functionname(params):
        statement1
        statement2
        .....


Simple Python Functions Illustrations
-------------------------------------


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


Let us write a Function to add two strings and add two numbers


::

    # Function Adding Numbers and Concatination of Strings
    def add(x,y):
        print(x+y)

    add("hello","world") # Add Function is called with Two Strings

    add(3,5) # Add Function is Two Numbers Here

Output

.. code-block:: python

    helloworld
    8

Function with Default Arguments
--------------------------------

Example (save it as func-default.py)

::

    pass




.. code-block:: python

    pass


Functions Returning Values
--------------------------

This illustration shows how various function in the Python script and how returned objects are assigned to variable

Example (save it as func-return.py)

::

    def add(a, b):
        print "ADDING %d + %d" % (a, b)
        return a + b

    def subtract(a, b):
        print "SUBTRACTING %d - %d" % (a, b)
        return a - b

    def multiply(a, b):
        print "MULTIPLYING %d * %d" % (a, b)
        return a * b

    def divide(a, b):
        print "DIVIDING %d / %d" % (a, b)
        return a / b


    print "Let's do some math with just functions!"

    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

.. code-block:: python

    $ python func-return.py
    Let's do some math with just functions!
    ADDING 30 + 5
    SUBTRACTING 78 - 4
    MULTIPLYING 90 * 2
    DIVIDING 100 / 2
    Age: 35, Height: 74, Weight: 180, IQ: 50


Main Function
~~~~~~~~~~~~~

Example (save it as quadratic.py)

::

    import math

    def main():
        print "This program finds the real solutions to a quadratic\n"
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        discrim = b * b - 4 * a * c
        if discrim < 0:
            print "\nThe equation has no real roots!"
        elif discrim == 0:
            root = -b / (2 * a)
            print "\nThere is a double root at", root
        else:
            discRoot = math.sqrt(b * b - 4 * a * c) root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print "\nThe solutions are:", root1, root2

    if __name__ == "__main__":
        main()


Output

.. code-block:: python

    $ python quadratic.py
    This program finds the real solutions to a quadratic

    Please enter the coefficients (a, b, c): 5,6,4

    The equation has no real roots!



Recursion
----------

One of the finest example to illustrate Recursion in any language is Fibonacci.

Example (save it as fibonacci.py)

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
