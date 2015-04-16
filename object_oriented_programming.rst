.. highlight:: python
    :linenothreshold: 0


Object Oriented Programming
===========================




.. code:: python

    class Person():
        def say(self):
            print("Hello")

    jackman = Person()
    jackman.say()

.. code:: python

    class Person():

        def hello(self,name):
            print("Hello %s How are you ?")
        def bye(self,name):
            print("Nice Meeting You %s"%(name))

    jackman = Person()
    jackman.say("lee")
    jackman.bye("edison")

Constructors

.. code:: python

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

.. code:: python

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
    a.deposit(100)          # 'a' Aceess The Methods In The Class "BankAccount"
    b.deposit(50)           # 'b' Also Aceess The Methods In The Class "BankAccount"
    b.withdraw(10)
    a.withdraw(10)

.. code:: bash

    $python BankAccount.py
    100
    50
    40
    90

Single Inheritance

.. code:: python

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

.. code:: bash

    $python SingleInheritance.py
    Parent, Parent
    Parent, Child

Multiple Inheritance

.. code:: python

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

.. code:: bash

    $python MultipleInheritance.py
    m of D called
    m of B called
    m of C called
    m of A called

Super()

.. code:: python

    class A:              # The Method 'm' Of D Should Execute The Code Of 'm' Of B, C and A as well  By Using Super()
        def m(self):
            print("m of A called")

    class B(A):
        def m(self):
            print("m of B called")
            super().m()

    class C(A):
        def m(self):
            print("m of C called")
            super().m()

    class D(C,B):
        def m(self):
            print("m of D called")
            super().m()

    x = D()
    x.m()

.. code:: bash

    $python Super.py
    m of D called
    m of C called
    m of B called
    m of A called

Super() And Constructor

.. code:: python

    class A:
        def __init__(self):
            print("init of A")

    class B(A):
        def __init__(self):
            print("init of B")
            super().__init__()

    class C(A):
        def __init__(self):
            print("init of C")
            super().__init__()


    class D(B,C):
        def __init__(self):
            print("init of D")
            super().__init__()

    a = A()

    b = B()

    c = C()

    d = D()

.. code:: bash

    $python Super1.py
    init of A

    init of B
    init of A

    init of C
    init of A

    init of D
    init of B
    init of C
    init of A

Exception Handling

.. code:: python

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

.. code:: bash

    $python Exception.py
    7
    IndexError: List index out of range
    2
    KeyError: 'd'

.. code:: python

    try:
        r = [7, 54, 27, 6]
        print(r[5])
    except IndexError as e:
        print(e)
        finally:
        print("End Of Index Error")


.. code:: bash

    $python indexerror.py
    list index out of range
    End Of Index Error

.. code:: python

    try:
        s = {'a':1, 'b':2, 'c'=3}
        print(s[d])
    except KeyError as e:
        print(e)
    finally:
        print("End Of Key Error")


.. code:: bash

    $python keyerror.py
    'd'
    End Of Key Error
