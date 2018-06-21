# Chapter 3 - Functions and Input

**Topics**

Last lesson I talked about the various ontainers native to the Python language, as well as the two different types of loops.
I wanted to talk about functions and testing during that lesson too, but I'm way too long-winded to make that fit in one chapter.
Let's start with functions!

## Functions - Saving Logic for Later

Remember how when we covered loops, they were described in the context of performing the same operation multiple times?
**Functions are for encapsulating a set of operations for use whenever and wherever you want in your code.**
If you find yourself doing the same thing (or the same sort of things) over and over again, chances are you'd be doing yourself to encapsulate that repetitive logic inside of a function.

So, how do we write functions?
Here's a generic template:

```python
def <function_name>(<comma-separated parameter list>):
    """Documentation here."""
    <a line of logic>
    <another line of logic>
    <really however much logic you want>
    <you may want to include a line like the following>
    return <some value>
```

When we declare functions, typically it's all lowercase.
If your function's name is more than one word, you separate the words by underscores.

Immediately after the function's name you have the parentheses, which must be there for proper Python syntax.
You can fill those parentheses with parameters, which are like variables that exist only inside the function, or you can leave them empty.
It always depends on what you need the function for.
We'll see examples of both.

After the colon following the parameter list you'll need a new line and an indentation.
After that, everything that you want to be a part of the function will be indented.
If you're a good, responsible developer you **include a documentation string to tell others (or even your future self) the succinct purpose of the function**.

Real talk: if your function's documentation takes more than...two lines, then your function is probably too complex and you need to break it up into smaller functions.
I'm not talking about the part of your doc string that talks about what the various arguments are for.
That comes after the initial function's summary.

The [Python style guide](https://www.python.org/dev/peps/pep-0008/) actually wants your "short summary" to be one line.
After that short summary, you cna write whatever you want to help document your code.

To actually use the function and execute the logic you've saved, you "call" the function.
Calling the function involves typing out the name of the function, followed by parentheses.

So, if our function was like the following:

```python
>>> def print_foo() -> None:
...     print('foo')
```

We would execute the logic inside that function like so

```python
>>> print_foo()
foo
```

We could call this function as many times as we like and get the same result.
Useful!

Up to this point, any Python tool that we've used (e.g. `random.randint()`) has been a function that we've called.
Any functionality that we want to employ will, naturally, be encapsulated in a function.

Now, functions in Python will come in several flavors:

- Take no arguments and return nothing, but execute some logic
- Take no arguments and return some value or object
- Take one or more arguments and return nothing
- Take one or more arguments and return some value or object

We've already seen a contrived example of the first.
Let's see some contrived examples of the rest.

### 1. No arguments, but something is returned

We've seen this type of function in `random.random()`, but we haven't actually built one ourselves.
Let's write a function that'll return the random choice from a list of names of professions.

```python
def random_profession() -> str:
    """Randomly choose and return a job title."""
    import random
    jobs = ["programmer", "manager", "lawyer", "doctor", "engineer"]
    return random.choice(jobs)
```

This function has no parameters, so takes no arguments when called.
It will, however, return a string when it's called.
When it's called, it'll import the `random` package from the Python standard library.
It'll assign a list of strings to the variable `jobs`.
Finally, the `random.choice` function is called, with `jobs` as an argument.

The result of that function call, whatever it may be, is then returned.
For example:

```python
>>> random_profession()
lawyer
```

### 2. Arguments, but nothing returned

We want a function that'll take in a user's name and print that user's name along with a greeting.
Here's one:

```python
def hello_name(first_name: str) -> None:
    """Take a user's first and last names and print a greeting."""
    msg = f"Hey {first_name}, how is life?"
    print(msg)
```

Here we have a function named `hello_name`.
It has one **_required_** parameter, `first_name` which will be expected to be a `string`.
More on that "type annotation" soon.

Inside the `hello_name` function, the value assigned to `first_name` is used in `msg`, then the resulting `msg` is printed.

When this function is put into use, it will (should) go like so:

```python
>>> hello_name("Henry")
Hey Henry, how is life?
```

When this function was called, we provided the value of "Henry" as an **argument** to this function.
The function took that value, assigned it to `first_name` within the function, and printed the message.
Done!

### 3. Arguments, and something is returned

How about a function that takes in some information for a food order and returns the subtotal, tax, and grand total for the order?

```python
from typing import List

def order_total(menu_items: List[dict], tax_rate: float=0.10) -> tuple:
    """Given a list of foods and their costs, and the expected tax_rate,
    return the subtotal, tax, and grand total."""
    subtotal = 0.0
    for item in menu_items:
        subtotal += (item['price'] * item['quantity'])
    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    return subtotal, tax, round(subtotal + tax, 2)
```

We start by importing the `List` **type alias** from Python's `typing` library.
This serves no other function than being a descriptor of a more complex container structure than a simple list of individual floats or strings.
More in the next section about that.

We have a function named `order_total` which has two parameters: `menu_items`, which is expected to be a `list` of `dict`s; and `tax_rate`, which is expected to be a `float` and has a default value of 10.
You can still pass any value you want as an argument to `tax_rate`, but with the default value being set you don't always need to.
More on that syntax in a bit.

Within the function, the `subtotal` variable is set to `0.0`.
Then, for every `item` in the `menu_items` list, the price of that item is added to the `subtotal`.
Next, the `tax` is calculated by multiplying the `subtotal` by the `tax_rate`.
Finally, the `subtotal`, `tax`, and grand total (`subtotal + tax`) are returned as a `tuple`.

Note, just because you have multiple inputs doesn't mean that you need multiple outputs.
It just worked out that way for this example.

When this sort of function is called, it'll end up being passed a list of dicts, and may or may not be given a tax rate.

```python
>>> customer_order = [{'name': 'Jerk Chicken', 'price': 12.99, 'quantity': 1}, {'name': 'Beef Patty', 'price': 2.50, 'quantity': 4}, {'name': 'Ting', 'price': 2.25, 'quantity': 2}]
>>> order_total(customer_order) # default tax_rate=0.10
(27.49, 2.75, 30.24)
>>> order_total(customer_order, .0892) # tax rate for Washington state, 2017
(27.49, 2.45, 29.94)
>>> order_total(customer_order, 0.055) # tax rate in Maine, 2017
(27.49, 1.51, 29.0)
```

#### Detour: About Type Annotations

We've dived a tad deeply into the Python language before hearing a halfway-decent description of what the language is.
**Python is a dynamic, interpreted programming language.**
What does this mean?

In the world of programming languages there exist statically-typed and dynamically-typed languages.
C and Java are statically-typed, compiled languages.
This means that you write code such that when you declare a variable, you declare *in advance* the type of object (string, list, tuple, etc.) it will hold.
It can then only ever hold that one type of object.
When you want to execute the code that you wrote, you first **compile** it.
This involves translating the code you wrote into **machine code**, checking for potential errors in the code as it's being translated.

The benefit of writing code in such a language is that when you run that compiled code it runs remarkably fast.
One of the downsides is that the readability of the codebase suffers, which can slow down development time and team communication.

**Python is not that type of language.**

As a dynamic, interpreted language, Python doesn't care about what type of value you assign to a variable.
You can do the following, without real consequence:

```python
>>> number = 5
>>> number = 4.0 + 1.0
>>> number = "five"
>>> number = ["5"]
```

At runtime, i.e. when you actually run the code, Python determines the type of each object on the fly.
This makes the program run slower, but dev speed is potentially faster because the code is more readable, more flexible, and more easily communicated.

However, there's a comforting certainty that comes with statically-typed languages requiring you to declare the type of everything that you create.
Larger applications become somewhat less of a headache by taking out any guesswork.
Things only are as you declare them to be, and if they aren't you won't even be able to compile the code.

In dynamically-typed languages you're never actually sure of what type of value you have until you have it, and then bugs and errors can pop up in your code at inopportune times.
This is especially bad when working with others on poorly-documented code, where oftentimes collaboration can be bogged down in the guesswork of just what exactly something is supposed to be.

Enter: Type Annotations.
A type annotation is another method of documenting your code in Python.
When you declare a variable or a parameter, you include with that declaration a note about the type of object it's expected to hold.
It became an official part of the language as of Python 3.5 and is here to stay.
Check [this page on "typing"](https://docs.python.org/3/library/typing.html) for more details about type annotations.

Type annotations can be used anywhere a variable or parameter is declared.
They can also be used to hint at what types of values a function will return.
At the end of the day, though, they are still only hints.
This means a couple imnportant things that bear standing on their own:

- **Type annotations are not required anywhere at all**.
- **Type annotations impose no actual restrictions on your code**.
- **Type annotations do not prevent the wrong types from being assigned to variables in your codebase.**

**_TYPE ANNOTATIONS ARE ONLY HINTS_**.

Since I wasn't trained to include type annotations, I am as of this writing still not used to implementing them.
They're a good practice, but just not because they were deliberately included in the language.
They're a good practice because they increase the ability for someone (including you) to understand your code.
I'll include type annotations for the same reason that I include descriptive variable names, and documentation at the tops of my Python files, within my functions, and later on within my classes: clear communication of my intent makes it easier for others to understand what I've done.

#### Annotating Functions: The Barest Minimum

With that long rant about the "why" of type annotations behind us, let's focus in on the "how".
As we move forward throughout this book, I'll only include type annotations on function declarations.
My own personal feeling is that annotations clutter the code outside of that scope.

When including type annotations in your functions, they will appear in two spots: the parameter list, and immediately before the final colon on the declaration line.

Consider a function that takes in a user's name, email, age, and list of favorite foods as arguments.
It'll package those values into a dictionary, then return that dictionary for use elsewhere in the codebase.

Without type hints, such a function might look like this:

```python
>>> def user_profile(name, email, age, foods):
...     """Construct and return a user's profile."""
...     new_profile = {
...         "name": name,
...         "email": email,
...         "age": age,
...         "foods" : foods
...     }
...     return new_profile
```

With type annotations in the parameter list, we include the data type of each parameter next to the parameter's name.

```python
>>> def user_profile(name: str, email: str, age: int, foods: list):
...     """Construct and return a user's profile."""
...     new_profile = {
...         "name": name,
...         "email": email,
...         "age": age,
...         "foods" : foods
...     }
...     return new_profile
```

We could go one level deeper and with our parameter list annotations and ask: "what type of data is held in that `foods` list?"
Probably a list of strings.

```python
>>> from typing import List
>>>
>>> def user_profile(name: str, email: str, age: int, foods: List[str]):
...     """Construct and return a user's profile."""
...     new_profile = {
...         "name": name,
...         "email": email,
...         "age": age,
...         "foods" : foods
...     }
...     return new_profile
```

With a type annotation at the end of our function declaration line, we make a note about what type of data this function will return.
In this particular case, it'll return a dictionary.
So:

```python
>>> from typing import List
>>>
>>> def user_profile(name: str, email: str, age: int, foods: List[str]) -> dict:
...     """Construct and return a user's profile."""
...     new_profile = {
...         "name": name,
...         "email": email,
...         "age": age,
...         "foods" : foods
...     }
...     return new_profile
```

You can get as deep as you want with adding type annotations, as long as it's done in the spirit of providing clarity while not killing readability.

This is just one example.
We'll see many more as time goes on.

## The Many Ways to Take Input

Programs that run on their own are all well and good, but the more interesting programs that we write include some degree of external input.
That input can come from a static file somewhere, from a user, or some combination.
Let's see what that can look like.

### Reading from File

Let's say I have a file of comma-separated values, each row containing a person's personal information.
It can look something like this

```
Darin Alvarado,36,Alabama
Peter Rhodes,31,Alabama
Teresa Ray,48,Alabama
Darryl Hansen,31,Alabama
William Henderson,48,Alabama
...etc...
```

I've provided this whole data file (200 people) to you in [from-notes/03-function-inputs/people.csv](../from-notes/03-function-inputs/people.csv).
Let's create a directory called `data` and copy this file into that directory.

Reading a file into Python is actually pretty straightforward.
One of Python's built-in functions is `open`.
Its job is to open files so you can read from them or write to them.

To read a file, literally any file, you provide the **relative or absolute path** to the file to the `open` function as a string.

```python
>>> in_file = open('data/people.csv')
```

If we look at what `in_file` is, we see the following

```python
>>> in_file
<_io.TextIOWrapper name='data/people.csv' mode='r' encoding='UTF-8'>
```

This doesn't look like the contents of the file yet because we haven't _read_ the file.
All we've done is open the file for reading.

If we want to actually read the file, there's 3 ways:

- One line at a time, as a string
- All lines at once, as one big string
- All lines at once, each line as a string in a list

### Input on Execution

### Input within the Program

## Recap

## Exercises