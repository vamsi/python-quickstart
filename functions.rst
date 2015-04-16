.. highlight:: python
    :linenothreshold: 0


Functions
=========

Simple Functions
----------------



Illustrations
-------------

::

    # Function Adding Numbers and Concatination of Strings


    def add(x,y):
        print(x+y)

    add("hello","world") # Add Function is called with Two Strings

    add(3,5) # Add Function is Two Numbers Here

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

::

    # Function to say hello on call the function


    def hello():
        print("Hello")

    hello() # calling the function hello

::

    # Function calculating the square of a number


    def square(x):
        print (x*x)

    square(24) # Here the Square Function is called
