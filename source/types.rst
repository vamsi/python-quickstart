.. highlight:: python
    :linenothreshold: 0

Types
=====

Numbers
-------
::




Strings
-------
::

    #Using Single Quotes
    x='Hello World'

    #Using Double Quotes
    y="Python Programming"

    # Printing The Strings
    print(x)

    print(y)



::
    $ python strings.py
    Hello World
    Python Programming



#### Accessing Of The Strings

::

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


Tuples
------


::

    # Let This Be Our Tuple
    team = ("Sachin", "Dravid", "Dhoni", "Kohli", "Raina")

    #It Prints All Elements In The Tuple
    print(team)

::

    $python tuple.py
    ('Sachin', 'Dhoni', 'Dravid', 'Kohli', 'Raina')


::

    #To Acess The 1st Element In The Tuple
    team[0]

    #To Acess The Last Element In The Tuple
    team[-1]

    #To Acess The Element From 1st Location To 2nd Location
    team[1:3]

::

    $ python team_access.py
    'Sachin'
    'Raina'
    ('Sachin', 'Dhoni')

Dictionaries
------------
A dictionary is mutable and is another container type that can store any number of Python objects, including
other container types.


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
enclosed in curly braces.


An empty dictionary without any items is written with just two curly braces, like this: {}.
Keys are unique within a dictionary while values may not be.


The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings,
numbers, or tuples


The main operations on a dictionary are storing a value with some key and extracting the value given the key.


It is also possible to delete a key:value pair with del.


If you store using a key that is already in use, the old value associated with that key is forgotten.


It is an error to extract a value using a non-existent key.


The keys() method of a dictionary object returns a list of all the keys used in the dictionary,
in arbitrary order (if you want it sorted, just apply the sorted() function to it).


To check whether a single key is in the dictionary, use the in keyword.


Accessing Values in Dictionary:


To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.
Following is a simple example:

::
    #!/usr/bin/python

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

    ]print "dict['Name']: ", dict['Name'];
    print "dict['Age']: ", dict['Age'];



When the above code is executed, it produces the following result:

::

    dict['Name']:  Zara
    dict['Age']:  7
