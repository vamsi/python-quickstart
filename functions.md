# Functions

A function is a small unit of computation which may take arguments and may return values. The function body should be **indented**, like an if statement. Python has a lot of built-in functions.

The keyword ` def ` introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

We use ` def ` keyword to define a function. The general syntax looks like this:

````
def functionname(params):
    statement1
    statement2
    ...
````

The argument, *params*, doesn’t specify a datatype. In Python, variables are never explicitly typed. Python figures out what type a variable is and keeps track of it internally.


## Simple Python Functions Illustrations


#### Simple Python Function taking no arguments
````
    # Function to say hello on calling the function
    def hello():
        print("Hello")

    hello() # calling the function hello
````

#### Simple Python Function taking in arguments

````
# Function calculating the square of a number
    def square(x):
        print (x*x)

    square(24) # Here the Square Function is called
````
Let us write a Function to add two strings and add two numbers
````
    # Function Adding Numbers and Concatination of Strings
    def add(x,y):
        print(x+y)

    add("hello","world") # Add Function is called with Two Strings

    add(3,5) # Add Function is Two Numbers Here
````
###### Output
````
    helloworld
    8
````
#### Function with Default Arguments

Example (save it as `func-default.py`)
````
pass
````
#### Functions Returning Values

This illustration shows various functions in the Python script and how returned objects are assigned to a variable.

Example (save it as `func-return.py`)
````
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

````

###### Output 

````
    $ python func-return.py
    Let's do some math with just functions!
    ADDING 30 + 5
    SUBTRACTING 78 - 4
    MULTIPLYING 90 * 2
    DIVIDING 100 / 2
    Age: 35, Height: 74, Weight: 180, IQ: 50
````
#### Main Function 

Example (save it as `quadratic.py`)

```
import math

def main():
print "This program finds the real solutions to a quadratic\n"
a, b, c = input(
```