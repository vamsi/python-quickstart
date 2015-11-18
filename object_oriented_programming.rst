.. highlight:: python
    :linenothreshold: 0


Object Oriented Programming
===========================


A Quick Glance on the Basics on Object Orientation Terminology

class : A class is the blueprint from which individual objects are created.

object : A real World entity which have state and behavior



Lets create a class Person with a class method ``say`` in the class

::

    class Person():
        def say(self):
            print("Hello")


Now lets create an object instance for the class person

::

    class Person():
        def say(self):
            print("Hello")

    jackman = Person()
    jackman.say()


Extending the plot further lets us create two method ``hello`` , ``bye`` taking in arguments

::

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

.. note ::

    ``self`` is a default argument for all instance method

It's all vague repeating the instance variable for every class method so lets create an object with the instance variables.So, its now time to work with constructors




Constructors
------------

The Constructors in Python are written under a special method ``__init__``.


now write a constructor for an object. In this example lets create a Object with instance variables name, year_of_birth.This process of writing a constructor in a class eliminates the repeating of instance variables for every instance method.

::

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

Classes And Objects


Let's now to understand more about the ``self`` variable and __init__ method (Constructor) by looking at the example below

Example (save it as ``bank_account.py``)

::

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

.. code-block:: python

    $ python bank_account.py
    100
    50
    40
    90

Single Inheritance
~~~~~~~~~~~~~~~~~~

The Inherited class is taken as a argument to the child class.To understand clearly parent class is named ``Parent`` and child class that inherits parent class is named ``Child`` Class.

Example (save it as ``SingleInheritance.py``)
::

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

.. code-block:: python

    $ python SingleInheritance.py
    Parent, Parent
    Parent, Child

Multiple Inheritance
~~~~~~~~~~~~~~~~~~~~

This Example illustration the way classes are inherited in Python

Example (save it as ``MultipleInheritance.py``)

::

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

Output

.. code-block:: python

    $ python MultipleInheritance.py
    m of D called
    m of B called
    m of C called
    m of A called



Exception Handling
------------------


Handling Various Exceptions in Python.

Look at the following code and observe when the Exceptions are raised.


Example (save it as ``exception.py``)

::

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


Output

.. code-block:: python

    $ python exception.py
    7
    IndexError: List index out of range
    2
    KeyError: 'd'


Now let's Handle the above exceptions raised in the above examples


Example (save it as ``indexerror.py``)

::

    try:
        r = [7, 54, 27, 6]
        print(r[5])
    except IndexError as e:
        print(e)
        finally:
        print("End Of Index Error")

Output

.. code-block:: python

    $ python indexerror.py
    list index out of range
    End Of Index Error


Example (save it as ``keyerror.py``)
::

    try:
        s = {'a':1, 'b':2, 'c'=3}
        print(s[d])
    except KeyError as e:
        print(e)
    finally:
        print("End Of Key Error")

Output

.. code-block:: python

    $ python keyerror.py
    'd'
    End Of Key Error

.. note::

    The exceptions in the above programs are purposefully raised to illustrate Exception Handling
