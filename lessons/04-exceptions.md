# Chapter 4 - Exceptions

Sometimes your program will have errors because you made a mistake when you wrote it.
Fear not, typos and lapses in logic happen to even the most seasoned developers.

Far more often, your users will do the wrong (or the unanticipated) thing.
Forgive them, for they know not what they do.

Many more times, you'll design your program to break in specific ways under specific circumstances.
There are reasons to force a program to fail, with specific conditions in mind.

No matter what the source, expect that a program will generate errors.
In Python, there's no real end to the types of errors a program can generate, partially because you can custom-bake your own.
The language does, however, have [its own built-in set](https://docs.python.org/3/tutorial/errors.html) that it will benefit you to become familiar with called **Exceptions**.
Here are a few of the more common Exceptions:

- `SyntaxError`: long story short: you wrote broken Python. You wrote something that isn't within Python's syntax rules. Python won't even run code with a `SyntaxError`; it'll just alert you of your mistake
- `NameError`: you tried to use a variable name that either you didn't create or isn't available in the current scope. Either way, the variable you are trying to use doesn't have an assignment
- `TypeError`: you tried to perform an operation on a type of object that can't do the thing you want, like adding the number "1" and the word "apple"
- `ValueError`: the "type" of object that you were trying to use was fine, but its value was an invalid value for whatever it was you're trying to do. Like, a function might take integers between "1" and "100" and you gave it the value "-55"
- `IndexError`: you tried to access an index within a list or tuple that doesn't exist
- `KeyError`: similar to an `IndexError`, you tried to access a key within a dictionary that doesn't exist
- `AttributeError`: the object you're trying to do something with doesn't have the attribute you thought it had
- `ImportError`: the thing you tried to import isn't importable for some reason. Maybe you didn't download it, or maybe it's importable by another name
- `KeyboardInterrupt`: whoever was running the application deliberately tried to kill it with `control + C`

Errors are **good things**.
They let your users know when they're doing something wrong or when something specific happened during the execution of your program.
As the programmer, you can raise your own errors at any time throughout your program to alert the user of some specific incorrect behavior.

## Using Exceptions in Code

Let's say that your program includes a function that calculates compound interest.

```python
def compound_interest(principal: float, interest_rate: float, years: float) -> float:
    """Given a principal amount, an interest rate, and some amount of years,
    calculate the amount of money that would result from money compounded monthly."""
    monthly_rate = interest_rate / 100 / 12
    amount = principal * (1 + monthly_rate) ** (12 * years)
    return amount
```

The way that this function is set up, your user is allowed to put in negative or zero years.
You don't want to allow that, as it doesn't make sense in the context of your function.
You can use the `ValueError` to inform the user of what types of values they're allowed to use for that parameter.

```python
def compound_interest(principal: float, interest_rate: float, years: float) -> float:
    """Given a principal amount, an interest rate, and some amount of years,
    calculate the amount of money that would result from money compounded monthly."""
    if years <= 0:
        raise ValueError(f"{years} is not a valid entry for years. Provide any number greater than 0.")
    monthly_rate = interest_rate / 100 / 12
    amount = principal * (1 + monthly_rate) ** (12 * years)
    return amount
```

The `raise` keyword will trigger whatever Exception you provide.
You can provide just the Exception on its own, i.e. `raise ValueError`.
You can also do like I did above and provide a custom message for the Exception being raised.
I would recommend this for the same reason that I recommend including documentation strings for all your functions: letting the user know what's going on makes for a better user experience, no matter what.

Now when your user tries to input a number of years less than or equal to "0", they'll get the `ValueError` along with a message telling them what values are valid.

```python
>>> compound_interest(1000.0, 3.5, -12.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in compound_interest
ValueError: -12.0 is not a valid entry for years. Provide any number greater than 0.
```

Whenever an Exception is raised, with or without a message, the program stops execution.
Period.
It doesn't matter how many function calls deep within your program that your Exception is raised, program execution stops.

## Dealing with Exceptions

The only time that an Exception *doesn't* stop your program's execution is when you deliberately try to catch it.
The way you catch an Exception is effectively to say in your code "I'm going to try to do this thing. If it succeeds, great! If it fails in this specific way, do this other thing instead of dying."
As that expression above notes, it'll work a lot like an "if...else" combination.

Let's see this at play in an example.
Let's say I want to run a function that perpetually requests data from some external resource.
I want to be able to stop that process with a `KeyboardInterrupt`, but I don't want to kill the program in the process.
I want to, say, log the last result.

```python
# some stuff happens above
data = None

try:
    while True:
        data = get_data(location='somewhere')
except KeyboardInterrupt:
    print(f'The last bit of data was {data}')

# some stuff continues below
```

Here, until that `KeyboardInterrupt` hits, that `while True` loop will continue.
When that `KeyboardInterrupt` finally happens, instead of raising the Exception and killing the program you print a message then go on about your day.

You can do a number of things with the `except` keyword.
If you don't provide a specific exception, it'll catch *any* exception.
**Using `except` without a specific Exception in mind is a bad way to use this keyword!**
When you don't provide a specific Exception, you don't really know what was raised in the first place and whether or not you were handling it correctly.

You can also alias the Exception that was going to be raised and then have access to that Exception object and any attributes it may have.

```python
except ValueError as e:
    print(e)
```

You can catch multiple exceptions at the same time by just separating them with commas:

```python
except TypeError, ValueError, NameError:
```

You can also catch separate exceptions and handle them in different ways:

```python
except TypeError:
    # do something
except ValueError:
    # do something else
except NameError:
    # do something else
```

## Recap

This was a really brief chapter, but we still covered some important stuff:

- What errors look like in Python
- How to raise errors in your own code to alert the user
- How to handle errors when they have been raised so that your program doesn't stop completely

In the next chapter we'll look at how you can test your Python code.
We'll consider some testing strategies, and hopefully remove some of the mystery and perceived difficulty from writing tests for a codebase.

## Exercises

<!-- TO DO: Write 2 or 3 exercises -->