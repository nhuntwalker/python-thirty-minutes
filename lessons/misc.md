### Differences in Function Parameters

In that last example, we saw for the first time a function with both a required and an optional parameter.
An optional parameter is created when the parameter is assigned a value in the parameter list instead of just being declared as a name (and a type).

The value assigned to an optional parameter can be any valid Python value.
In the above example, the optional parameter was assigned a `float`.
However, that could've just as easily been a `str`, `tuple`, `list`, `dict`, or even a separate function!
Whatever value you assign to an optional parameter is then bound to that function and is as much a part of that function as the logic within.
This may not mean much now, but allow me to show you how it can matter a lot, specifically with respect to mutable objects.

A programming fan favorite is the [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) (1, 1, 2, 3, 5, 8,...).
It's an infinite sequence where the next number is the sum of the previous two numbers.
So 1 + 1 = 2, 1 + 2 = 3, 2 + 3  = 5, etc.

Often in interviews, programmers will be asked to write some function that has to do with this sequence.
For example, given a list of at least 2 numbers, add the next `N` numbers in the sequence.
If no list of numbers is given, just show the first `N` numbers of the sequence.
Either way, return the resulting sequence.

One might think the solution to such a problem could look like:

```python
def fib_sequence(n: int, sequence: list=[]) -> list:
    """Find and return either the first n numbers or the next n numbers of the fibonacci sequence."""
    if len(sequence) < 2:
        sequence.extend([1, 1])
        n -= 2

    for i in range(n):
        a = sequence[-2]
        b = sequence[-1]
        sequence.append(a + b)

    return sequence
```

You test the function with a prefilled sequence like `[1, 1, 2, 3, 5, 8]` and you see that it works

```python
>>> fib_sequence(3, [1, 1, 2, 3, 5, 8])
[1, 1, 2, 3, 5, 8, 13, 21, 34]
```

For good measure, you test it without the starter sequence and you see that it works there too

```python
>>> fib_sequence(5)
[1, 1, 2, 3, 5]
```

It works in both cases that you thought of, so you feel like you can call it a day.
However, you've introduced an unfortunate bug.
You'll see it if you call the function again without a starter sequence.

```python
>>> fib_sequence(3)
[1, 1, 2, 3, 5, 8, 13, 21]
```

That doesn't look like a list of 3 numbers to me.
Does this same thing happen when you give it a list of numbers?

```python
>>> fib_sequence(3, [1, 1, 2])
[1, 1, 2, 3, 5, 8]
```

It works fine with the list of numbers, but not without.
What gives?

When you declare a function with an optional parameter whose default value is set to any mutable object, you're baking that one instance of that mutable object INTO the function.
This means that when you rely on that default value in your function call, you're referencing that same instance over and over again, changing it with every function call.

If this type of behavior is something you want, then feel free to leave it and go on about your business.
Just always be aware of what values you're using as default values.

Any valid Python function can have either required params or optional params, both, or neither.
There is an appropriate order to things when you include both.
**Required parameters always come first in your function declaration and in your function calls.**
This means that this sort of function call will throw an error.

```python
>>> fib_sequence(sequence=[1, 1, 2], 5)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

If you end up having more than one optional parameter, you can provide arguments for those parameters in whatever order you want, **as long as they all come after the required parameters**.
This even works for required parameters if they're being provided arguments by name.

```python
>>> def monthly_payment(principal: float, apy: float) -> float:
...    """Calculate the amount to pay per month for some principal and interest rate."""
...    return round(principal * (1 + apy) / 12, 2)
...
>>> monthly_payment(50000.0, 0.12)
4666.67
>>> monthly_payment(apy=0.12, principal=50000.0)
4666.67
```

If you want your function to take in any amount of required arguments (a.k.a. "positional" arguments), you can declare your function with the syntax (`*args`).

```python
>>> def print_stuff(*args: list) -> None:
...    """Print whatever its been given."""
...    for stuff in args:
...        print(stuff)
...
>>> print_stuff(1)
1
>>> print_stuff(1, 2, 3, 4, 5)
1
2
3
4
5
```

Similarly, if you want to provide any number of required arguments, you can provide a list or tuple of those arguments preceded by an asterix.
Just make sure that the number of arguments you're providing matches the number of arguments the function requires, in the order that makes the function make sense.

```python
>>> things_to_print = [1, 'apple', {'chair': 'potato'}, ['na', 'na', 'na']]
>>> print_stuff(*things_to_print)
1
apple
{'chair': 'potato'}
['na', 'na', 'na']
```

The single asterisk says "here are some values for you to unpack. Do not treat this as one singular item".
Without the asterisk, you're saying "here is one singular item to use in the function."

You can do a similar thing with optional parameters (a.k.a. keyword parameters).
If you want your function to take in any number of optional parameters, include `**kwargs` in your parameter list.

```python
>>> def running_out_of_ideas(**kwargs):
...    """Seriously though, running out of ideas."""
...    print(kwargs)
...
>>> running_out_of_ideas(potato='salad', makers='mark', drugs='bad, mmkay')
{'potato': 'salad', 'makers': 'mark', 'drugs': 'bad, mmkay'}
```

If you have a function with optional parameters, you can provide it with keyword arguments even if it wasn't declared with `**kwargs` by passing in a dictionary preceded by the double-asterisk.

```python
>>> monthly_payment(**{'principal': 25000, 'apy': 0.25})
2604.17
```