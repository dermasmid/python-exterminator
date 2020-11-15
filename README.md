# Pest control

Bugs are bad, but it's even worse when it happens in production, this is why it is a good idea to document all data possible when a exception occurs.

## Installing

``` bash
pip3 install exterminator
```

## Usage

You have three options.

### As a decorator

``` python
from exterminator import Exterminator

@Exterminator()
def main_function():
    # do stuff that might work

main_function()
```

### As a context manager

``` python
from exterminator import Exterminator

with Exterminator():
    # do stuff, you know the thing
```

### Globally

``` python
from exterminator import Exterminator

Exterminator().globally()

# that's it! now every exception that is not handled will be looged
```

## Important Note

If you are going to except all errors the context manager and globally solution wont work for you, the only option for you will be:

``` python
from exterminator import Exterminator

@Exterminator()
def main_function():
    # do stuff that work or not

try:
    main_function()
except:
    # do some stuff of you own...
```
