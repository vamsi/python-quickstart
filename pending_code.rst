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
