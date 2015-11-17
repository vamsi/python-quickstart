.. highlight:: python
    :linenothreshold: 0


Modules
========

Standard Library Modules
------------------------

Modules are reusable libraries of code in Python. Mostly, there are modules in the standard library and there are other Python files, or directories containing Python files, in the current directory (each of which constitute a module).

A module is imported using the import statement.


Lets import a time module from the standard library

.. code-block:: python

    import time
    print time.asctime()

.. note::

        To know the list of methods and functions in a modules use the ``dir`` function

        Eg: dir(time) gives out all things existing in time module

You can also do the import the either way

.. code-block:: python

    from time import asctime
    print(asctime())

Here were imported just the asctime function from the time module.


Writing Own Modules
-------------------

Lets now create a simple Module that calculates the square,cube of a number

Example (save the files as ``sqcube.py``)

::

    def square(x):
        return x * x

    def cube(x):
        return x * x * x


Now open up your interpreter and say import sqcube and use the functions in the modules

.. code-block:: python

    $ python
    >>> import sqcube
    >>> sqcube.square(25)

    >>> sqcube.cube(12)


Woot! we create a python library ``sqcube``



Third Party Modules
-------------------

The python has got the greatest community for creating great python packages


Python Package is a collection of all modules connected properly into one form and distributed


PyPI, The Python Package Index maintains the list of Python packages available.

To install pip, securely download get-pip.py, from the url `get-pip <https://bootstrap.pypa.io/get-pip.py>`_

Then run the following (which may require administrator access):

python get-pip.py

Find all other Installing Instruction details at https://pip.pypa.io/en/latest/installing.html

Now when you are done with pip

Go to command promt/terminal and say ``pip install <package_name>``

.. warning::

    Windows users make sure that you append your path variable in environment variable for your command to work



Lets now install a great package named ``requests`` and see how we can get the content of a website

.. code-block:: python

    pip install requests


Example (save it as ``requests.py``)

.. code-block:: python

    import requests
    response = requests.get('https://api.github.com/events')
    response.content

Three lines of code returned the entire contents of that url.
