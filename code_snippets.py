# Basics:
print "Hello, World!"

#1
i = 5
# Error below! Notice a single space at the start of the line
print 'Value is ', i
print 'I repeat, the value is ', i

#2
i = 999
p = "PyQuick"
print(i)
print(p)
print("Hello World !!!")
print("Hello !!!")
print("Hello Python")
print("Welcome")

#3
a = raw_input("Enter something")
print("You have entered the below")
print(a)
#---------------------------------------------------------------------------------------
# Types:

#1.
a = 3    # Taken as Int
b = 4.0  # Taken as Float

#2.
#Using Single Quotes
x='Hello World'

#Using Double Quotes
y="Python Programming"

# Printing The Strings
print(x)

print(y)

#3.
x='Hello World'

#prints only the character at 0th(First) location
print x[0]

#prints only the character at 4th location
print x[4]

#prints the characters from 0th location to (11-1)locations
print x[0:11]

#prints the characters till (6-1)th locations and concats Python to that
print x[:6]+"Python"

#prints only the last character
print x[-1]

#prints the third last character
print x[-3]

#4.
# Let this be our First List
fruits = ['Mango','Apple','Banana','Orange']

# Let this be our Second List
vegetables = ['Brinjal','Potato','Cucumber','Cabbage','Peas']

# Printing Our First List
print(fruits)

# Printing Our Second List
print(vegetables)

#5.
# Let this be our First List
fruits = ['Mango','Apple','Banana','Orange']

# Let this be our Second List
vegetables = ['Brinjal','Potato','Cucumber','Cabbage','Peas']

# Zeroth Index gives us the First Element in Our List
print(vegetables[0])

# Carefully Observe the Output Indexes of the List
print(vegetables[4])
print(friuts[1])
print(friuts[3])

# Using len() on lists
print(len(fruits))
print(len(vegtables))

#6.
a = [98,76,87,45,90,23,65,2,9,20]
a.append(4)
print(a)
a.extend(b)
print(a)

#7.
a = [98,76,87,45,90,23,65,2,9,20]
print(a.index(87))
(a.sort())
print(a)

#8.
# Let This Be Our Tuple
team = ("Sachin", "Dravid", "Dhoni", "Kohli", "Raina")

# It Prints All Elements In The Tuple
print(team)


#9.
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

#---------------------------------------------------------------------------------------

#Control flow:

#1.
a,b = input("Enter a,b values:")
if(a>b):
    print "The largest number is",a
else:
    print "The largest number is",b


#2.
print("enter any number:")
num = input()
if(num>0):
    if ((num%2)==0):
        print "The entered number",num,"is even"
    else:
        print "The entered number",num,"is odd"
else:
    print("Enter positive number")

#3.
print("Enter any num:")
num = input()
fact = 1
for i in range(1,num):
    fact = fact*i
print "Factorial of",num,"is:",fact


#4.
a = input("Enter a number")
i = fact = 1
while i<=a:
    fact = fact*i
    i = i+1
print(fact)

#5.
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
print 'Done'

#6.
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Too small'
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here...

#7.
def f(arg):    # a function that does nothing (yet exists)
    pass

class C:
    pass       # a class with no methods (yet exists)

class A(ABSDBASBD,IAUSDBDBD):
    pass
#---------------------------------------------------------------------------------------

#Functions:

#1.
    # Function to say hello on calling the function
    def hello():
        print("Hello")

    hello() # calling the function hello

#2.
# Function calculating the square of a number
    def square(x):
        print (x*x)

    square(24) # Here the Square Function is called

#3.
    # Function Adding Numbers and Concatination of Strings
    def add(x,y):
        print(x+y)

    add("hello","world") # Add Function is called with Two Strings

    add(3,5) # Add Function is Two Numbers Here

#4.
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

#5.
import math

def main():
print "This program finds the real solutions to a quadratic\n"
a, b, c = input()
#---------------------------------------------------------------------------------------

#Modules:

#1.
import time
print time.asctime()

#2.
from time import asctime
print(asctime())

#3.
def square(x):
    return x * x

def cube(x):
    return x * x * x

#4.
import requests
response = requests.get('https://api.github.com/events')
response.content
#---------------------------------------------------------------------------------------

#Object-Oriented Programming

#1.
class Person():
    def say(self):
        print("Hello")

#2.
class Person():
    def say(self):
        print("Hello")

jackman = Person()
jackman.say()

#3.
class Person():

    def hello(self,name):
        self.name = name
        print("Hello %s How are you ?"(self.name))
    def bye(self,name):
        self.name = name
        print("Nice Meeting You %s"%(self.name))

jackman = Person()
jackman.hello("lee")
jackman.bye("edison")

#4.
class Person():
    def __init__(self,name,year_of_birth):

        self.name = name
        self.year_of_birth = year_of_birth

    def detail(self,name):
        print("Name of the person is %s"%(name))

    def age(self,year_of_birth):
        print("Your are %s Years Old"%(year_of_birth))

person = Person()
person.details()
person.age()

#5.
class BankAccount:          # Creating A Class, Object & Consuctor
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()       # Here Instance Variable 'a' Calls The Class BankAccount
b = BankAccount()       # Here Instance Variable 'b' Calls The Class BankAccount
a.deposit(100)          # 'a' Access The Methods In The Class "BankAccount"
b.deposit(50)           # 'b' Also Access The Methods In The Class "BankAccount"
b.withdraw(10)
a.withdraw(10)

#6.
class Parent():
    def a(self):
        return self.b()

    def b(self):
        return 'Parent'

class Child(Parent):
    def b(self):
        return 'Child'

c = Parent()
d = Child()
print c.a(), d.a()
print c.b(), d.b()

#7.
class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of A called")

class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
x.m()

#8.
r = [7, 54, 27, 6]

# This prints the 1st index element
print(r[0])

# This raises IndexError since list contains only 4 elements
print(r[5])

s = {'a':1, 'b':2, 'c'=3}

# This prints the value hold by 'b' in the list
print(s[b])

# This raises the KeyError since d-key is not present in the list
print(s[d])

#9.
try:
    r = [7, 54, 27, 6]
    print(r[5])
except IndexError as e:
    print(e)
finally:
    print("End Of Index Error")

#10
try:
    s = {'a':1, 'b':2, 'c'=3}
    print(s[d])
except KeyError as e:
    print(e)
finally:
    print("End Of Key Error")