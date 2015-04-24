.. highlight:: python
    :linenothreshold: 0

Types
=====

Numbers
-------
Python can handle normal long integers (max length determined based on the operating system, just like C),

Python long integers (max length dependent on available memory), floating point numbers (just like C doubles), octal and hex numbers, and complex numbers (numbers with an imaginary component).

Generic C++ example

::

    int a = 3; //inline initialization of integer
    float b; //sequential initialization of floating point number
    b = 4.0f;



Generic Python example

::

    a = 3    # Taken as Int
    b = 4.0  # Taken as Float

.. note::

   To verify the type that's assumed by the your interpreter use ``type`` function
   Eg: ``type(var)`` this returns the type of variable




Strings
-------

Python strings are "immutable" sequences which means they cannot be changed after they are created (Java strings also use this immutable style). Since strings can't be changed, we construct *new* strings as we go to represent computed values.

So for example the expression ('hello' + 'there') takes in the 2 strings 'hello' and 'there' and builds a new string 'hellothere'.

Characters in a string can be accessed using the standard [ ] syntax, and like Java and C++,

Python uses zero-based indexing, so if str is 'hello' str[1] is 'e'.

If the index is out of bounds for the string, Python raises an error.

Example (save it as strings.py)

::

    #Using Single Quotes
    x='Hello World'

    #Using Double Quotes
    y="Python Programming"

    # Printing The Strings
    print(x)

    print(y)


Output

::

    $ python strings.py
    Hello World
    Python Programming



.. note::

    Guess the use of single Quotes and Double Quotes


slice , len()
~~~~~~~~~~~~~~~~~~

The handy "slice" syntax (below) also works to extract any substring from a string.

::

    var[begin:end]

The len(string) function returns the length of a string.

The ``[ ]`` syntax and the ``len()`` function actually work on any sequence type -- strings, lists, etc


Example (save it as string_access.py)

::

    x='Hello World'

    #prints only the character at 0th(First) location
    print x[0]

    prints only the character at 4th location
    print x[4]

    prints the characters from 0th location to (11-1)locations
    print x[0:11]

    prints the characters till (6-1)th locations and concats Python to that
    print x[:6]+"Python"

    prints only the last character
    print x[-1]

    prints the third last character
    print x[-3]


Output

::

    $ python string_access.py
    H
    o
    Hello World
    Hello Python
    d
    r

Lists
------

The most basic data structure in Python is the sequence.Each element of a sequence is assigned a number - its position or index.
The first index is zero, the second index is one,and so forth.


The list is a most versatile datatype available in Python.The list of items should be enclosed in square brackets ``[]`` so that Python understands that you are specifying a list.The items in the list should be seperated by comma.The "empty list" is just an empty pair of brackets ``[ ]``.

.. note::

    Good thing about a list is that items in a list need not all have the same type.
    ::

        list = ["Hello",1,True,False]


Once you have created a list, you can add, remove or search for items in the list.Since we can add and remove items, we say that a list is a "mutable" data type i.e. this type can be altered.


Example (save it as lists.py)
::

    # Let this be our First List
    fruits = ['Mango','Apple','Banana','Orange']

    # Let this be our Second List
    vegetables = ['Brinjal','Potato','Cucumber','Cabbage','Peas']

    # Printing Our First List
    print(fruits)

    # Printing Our Second List
    print(vegetables)

::

    $ python list.py
    ['Mango','Apple','Banana','Orange']
    ['Brinjal','Potato','Cucumber','Cabbage','Peas']


Example (save it as list_access.py)
::

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

Method
~~~~~~

Tuples
------
Tuples are sequences, just like lists.The only difference is that tuples can't be changed i.e., tuples are immutable and tuples use parentheses
whereas lists are mutable and use square brackets.


Creating a tuple is as simple as putting different comma-separated values and optionally you can put these comma-separated values between parentheses also.Tuples are pretty easy to make. You give your tuple a name, then after that the list of values it will carry.


We can access the items in the tuple by specifying the item’s position within a pair of square brackets just like we did for lists.
This is called the "indexing operator".


For example, here we have created a variable "team" which consists of a tuple of items.


"len" function can be used to get the length of the tuple. This also indicates that a tuple is a "sequence" as well.


Now if we just give the variable name "team" then we will get all the set of elements in tuple.

Example
::

    # Let This Be Our Tuple
    team = ("Sachin", "Dravid", "Dhoni", "Kohli", "Raina")

    #It Prints All Elements In The Tuple
    print(team)

::

    $python tuple.py
    ('Sachin', 'Dhoni', 'Dravid', 'Kohli', 'Raina')


::

    #To Access The 1st Element In The Tuple
    team[0]

    #To Access The Last Element In The Tuple
    team[-1]

    #To Access The Element From 1st Location To 2nd Location
    team[1:3]

::

    $ python team_access.py
    'Sachin'
    'Raina'
    ('Sachin', 'Dhoni')

Dictionaries
------------
A dictionary is mutable and is another container type that can store any number of Python objects, including other container types.

Dictionaries consist of pairs (called items) of keys and their corresponding values.

Python dictionaries are also known as associative arrays or hash tables.


::

    The general syntax of a dictionary is as follows:

    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}


"dict" is the name of the dictionary.


It contains both the key and value pairs i.e,"Alice" is the key and "2341" is the value and the same is for next values.
You can create dictionary in the following way as well:

::

    dict1 = { 'abc': 456 };
    dict2 = { 'abc': 123, 98.6: 37 };


Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is
enclosed in curly braces.An empty dictionary without any items is written with just two curly braces, like this: {}.Keys are unique within a dictionary while values may not be.
The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings,
numbers, or tuples.

The main operations on a dictionary are storing a value with some key and extracting the value given the key.It is also possible to delete a key:value pair with del.If you store using a key that is already in use, the old value associated with that key is forgotten.It is an error to extract a value using a non-existent key.


The keys() method of a dictionary object returns a list of all the keys used in the dictionary,
in arbitrary order (if you want it sorted, just apply the sorted() function to it).


To check whether a single key is in the dictionary, use the in keyword.


Accessing Values in Dictionary:


To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.
Following is a simple example:

::

    #!/usr/bin/python

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

    print "dict['Name']: ", dict['Name'];
    print "dict['Age']: ", dict['Age'];



When the above code is executed, it produces the following result:

::

    dict['Name']:  Zara
    dict['Age']:  7
