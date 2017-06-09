# Modules


## Standard Library Modules
---
Modules are reusable libraries of code in Python. Mostly, there are modules in the standard library, and then there are other Python files, or directories containing Python files, in the current directory (each of which constitutes a module).

A module is imported using the `import` statement.


Let's import a time module from the standard library

```
import time
print time.asctime()
```

##### Note:

To know the list of methods and functions in a modules use the ``dir`` function.

E.g.: `dir(time)` gives out all things existing in time module

You can also import in the following way:

```
from time import asctime
print(asctime())
```

Here were imported just the `asctime()` function from the time module.


## Writing Your Own Modules
---

Let's now create a simple module that calculates the square and cube of a number.

Example (save the files as ``sqcube.py``)

```
def square(x):
    return x * x

def cube(x):
    return x * x * x
```

Now open up your interpreter and say `import sqcube` and use the functions in the modules.

```
$ python
>>> import sqcube
>>> sqcube.square(25)

>>> sqcube.cube(12)
```

Woot! we created a Python library called ``sqcube``.



## Third Party Modules
---

Python has the greatest community for creating great Python packages. A Python package is a collection of all modules connected properly into one form and distributed.

**PyPI**, the Python Package Index maintains the list of Python packages available.

To install **pip**, securely download `get-pip.py`, from the url <https://bootstrap.pypa.io/get-pip.py>.

Then run the following (which may require administrator access):

`python get-pip.py`

Find all other installation instructions and details at https://pip.pypa.io/en/latest/installing.html

Now, after you are done with pip, go to the command promt/terminal and say ``pip install <package_name>``

##### Warning!

Windows users should make sure to append the path variable to the environment variable for the command to work.


Let's now install a great package named ``requests`` and see how we can get the content of a website.

`pip install requests`


Example (save it as ``requests.py``)

```
import requests
response = requests.get('https://api.github.com/events')
response.content
```

These three lines of code will have returned the entire contents of that url.
