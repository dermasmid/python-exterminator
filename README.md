# Pest control

Bugs are bad, but it's even worse when it happens in production, this is why it is a good idea to document all data possible when a exception occurs.

## Usage

You have two options.

### As a decorator

``` python
import exterminator

@exterminator.Exterminator()
def main_function():
    # do stuff that might work

main_function()
```

### As a context manager

``` python
import exterminator

with exterminator.Exterminator():
    # do stuff, you know the thing
```
