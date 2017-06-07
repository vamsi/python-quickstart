# Object Oriented Programming

A quick glance at the basics of the Object Orientation terminology.

**class** : A class is the blueprint from which individual objects are created.
**object** : A real World entity which have state and behavior

Let's create a class `Person` with a class method `say` in the class.

```
class Person():
    def say(self):
        print("Hello")
```
Now let's create an object instance for the class.

```
class Person():
    def say(self):
        print("Hello")

jackman = Person()
jackman.say()
```

Extending the plot further lets us create two methods, ``hello`` and ``bye`` that take arguments.

```
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
```

##### Note:

``self`` is a default argument for all instance method


This needs us to repeat the instance variable for every class method instead of creating an object with the instance variables. It's now time to work with constructors.


## Constructors
---

Constructors in Python are written under a special method ``__init__``.


Now let us write a constructor for an object. In this, example let's create an object with instance variables `name` and `year_of_birth`.This process of writing a constructor in a class eliminates the repeating of the instance variables for every instance method.

```
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
```

## Classes and Objects
---

Let's now to understand more about the ``self`` variable and __init__ method (Constructor) by looking at the example below.

Example (save it as ``bank_account.py``)

```
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
```

Output:

```
$ python bank_account.py
100
50
40
90
```

## Single Inheritance
---

The inherited class is taken as an argument to the child class.To understand clearly, the parent class is named ``Parent`` and the child class that inherits this parent class is named ``Child``.

Example (save it as ``SingleInheritance.py``)
```
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

```

Output:
```
$ python SingleInheritance.py
Parent, Parent
Parent, Child
```

## Multiple Inheritance
---

This example illustrates the way classes are inherited in Python.

Example (save it as ``MultipleInheritance.py``)

```
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
```

Output:

```
$ python MultipleInheritance.py
m of D called
m of B called
m of C called
m of A called
```


## Exception Handling
---

This section deals with handling various exceptions in Python. Look at the following code and observe when exceptions are raised.


Example (save it as ``exception.py``)

```
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
```

Output:

```
$ python exception.py
7
IndexError: List index out of range
2
KeyError: 'd'
```

Now let's handle the exceptions raised in the above examples.


Example (save it as ``indexerror.py``)

```
try:
    r = [7, 54, 27, 6]
    print(r[5])
except IndexError as e:
    print(e)
finally:
    print("End Of Index Error")
```

Output:

```
python indexerror.py
list index out of range
End Of Index Error
```

Example (save it as ``keyerror.py``)
```
try:
    s = {'a':1, 'b':2, 'c'=3}
    print(s[d])
except KeyError as e:
    print(e)
finally:
    print("End Of Key Error")
```

Output:

```
$ python keyerror.py
'd'
End Of Key Error
```

##### Note:

The exceptions in the above programs have been raised on purpose to illustrate exception handling.
