.. highlight:: python
    :linenothreshold: 0

This file contains pending example code



Super() And Constructor

::

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

::

    $python super1.py
    init of A

    init of B
    init of A

    init of C
    init of A

    init of D
    init of B
    init of C
    init of A


a = [98,76,87,45,90,23,65,2,9,20]
b = [123,12]
a.append(4)
print(a)
a.extend(b)
print(a)

Super()
~~~~~~~

Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

Example (save it as ``super-illustration.py``)
::

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

::

    $ python super-illustration.py
    m of D called
    m of C called
    m of B called
    m of A called
