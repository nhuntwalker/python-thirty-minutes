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
After that short summary, you can write whatever you want to help document your code.

I'd like to reiterate a bit that might've gotten skimmed over above: **FUNCTIONS SHOULD BE SMALL AND DO ONE THING WELL**.
In practice you're going to write bugs.
It's inevitable; where there's code there are bugs.
Writing small, focused functions makes it easier for you to diagnose where those bugs pop up.

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

If we want to actually *read* the file, there's 3 ways:

- One line at a time from the top of the file, as a string with `in_file.readline()`
- All lines at once, as one big string with `in_file.read()`
- All lines at once, each line as a string in a list with `in_file.readlines()`

A word of caution: even though we're about to read the entire file, **reading all lines in a file at once can be a prohibitively-slow procedure**.
Imagine trying to read a 10GB text file all at once!

While there are packages in the Python standard library that are specifically geared toward reading CSV files, we're going to parse this file manually into a list of dictionaries with some basic Python methods/functions.

First let's read in all the data and check the first 5 lines.

```python
>>> file_data = in_file.readlines()
>>> file_data[:5]
['Joshua Lin,47,Georgia\n', 'Parker Montgomery,53,Georgia\n', 'Ronald Bradley,23,Georgia\n', 'Jasmine Robertson,55,Georgia\n', 'Samantha Carson,54,Georgia\n']
```

That looks like our data.

Those two characters, `"\n"` at the end of every string are actually one character and are an example of **whitespace**.
They signify that there's a new line in the string.
We want to get rid of that.

Strings have a method called `strip()` which will remove whitespace from the beginning and the end of the given string, but leave the whitespace within the string intact.
We can see that if we try using it on a few strings.

```python
>>> for line in file_data[:5]:
...     print(line.strip())
...
Joshua Lin,47,Georgia
Parker Montgomery,53,Georgia
Ronald Bradley,23,Georgia
Jasmine Robertson,55,Georgia
Samantha Carson,54,Georgia
```

Ok so we know how to get the excess space off of every line.
Those commas in every line denote separations in data, also known as **delimiters**.
What we need now is a way to separate those columns of data into individual strings.

Strings have another method that's useful for processing called `split()`.
If you pass a string into `split()` as an argument, that string will be...split...based on that string into a list of strings.

```python
>>> line = "Joshua Lin,47,Georgia"
>>> line.split(',')
['Joshua Lin', '47', 'Georgia']
```

If you call `split()` without an argument, it'll just split based on whitespaces.

We can combine the `strip()` and `split()` methods to do two operations on one line:

```python
>>> for line in file_data[:5]:
...     print(line.strip().split(','))
...
['Joshua Lin', '47', 'Georgia']
['Parker Montgomery', '53', 'Georgia']
['Ronald Bradley', '23', 'Georgia']
['Jasmine Robertson', '55', 'Georgia']
['Samantha Carson', '54', 'Georgia']
```

Why does this work?
Well, `.strip()` is a function, and when it's called it returns a string.
Specifically, it returns the result of removing whitespace from the left and right sides of the original string.
Since the result is itself a string, you can call `.split()` on it to split that result.

Let's wrap this up by rolling all this into a list of dictionaries.

```python
>>> def process_line(line: str) -> dict:
...     """Assign values from lines of a data file to keys in a dictionary."""
...     name, age, state = line.strip().split(',')
...     result = {
...         "name": name,
...         "age": int(age),
...         "state": state
...     }
...     return result
...
>>> people = []
>>> for line in file_data[:5]:
...     people.append(process_line(line))
...
>>> print(people)
[{'name': 'Joshua Lin', 'age': 47, 'state': 'Georgia'}, {'name': 'Parker Montgomery', 'age': 53, 'state': 'Georgia'}, {'name': 'Ronald Bradley', 'age': 23, 'state': 'Georgia'}, {'name': 'Jasmine Robertson', 'age': 55, 'state': 'Georgia'}, {'name': 'Samantha Carson', 'age': 54, 'state': 'Georgia'}]
```

The `process_line` function takes what we had been doing in the `for` loop and turns it into a repeatable routine.
Within, it takes the result of `line.strip().split(',')` and uses Python's multiple-assignment to assign the resulting 3 values to 3 variables.
Note: you can only use multiple assignment if the number of variables on the left matches the number of values coming from the right.
So, `a, b = 1, 2` will work.
`a, b, c = 1, 2` will not, nor will `a, b = 1, 2, 3`.

Finally, when you're done working with a file's contents, or at least don't have to read from the same file anymore, make sure to `close` the file.
Keeping too many resources open at once can slow down your machine, and it can prevent modification of that file by other processes.

Also it's just good to clean up after yourself.

```python
>>> in_file.close()
```

For a top-to-bottom view of how this code would look in a Python file, check out the `from-notes` directory [here](../from-notes/03-functions-input/people_parser.py).

### Input on Execution

Oftentimes when running Python files from the command line, you'll see some syntax like

```
$ python <python filename> <arg1> <arg2>
```

This sort of execution works because there's code set to take in and handle those command line arguments.
Let's see what this can look like.

I want a program that'll do some math for me.
I want to be able to tell it what type of operation to do (add, subtract, multiply, divide), and give it two numbers to act on.
Then, it'll print the result for me.
I'm going to call this program `math.py` and I want to be able to run it like `$python math.py multiply 4 5`.

```python
"""Do whatever math I want to do at a given point in time."""
def add(num1: float, num2: float) -> float:
    """Add two numbers."""
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    """Subtract two numbers."""
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    """Multiply two numbers."""
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    """Divide two numbers."""
    return num1 / num2

switchboard = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("Run math.py in the following format: python math.py <operation> <number> <number>. The supported operations are 'multiply', 'divide', 'add', and 'subtract'.")
        sys.exit()
    elif len(sys.argv) < 4:
        print("ERROR: You didn't provide enough arguments!")
        sys.exit()
    elif len(sys.argv) > 4:
        print("ERROR: You provided too many arguments!")
        sys.exit()

    operation = sys.argv[1]
    if operation not in switchboard:
        print(f"ERROR: {operation} isn't a supported operation. Try 'multiply', 'divide', 'add', or 'subtract'")
        sys.exit()

    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    result = switchboard[operation](num1, num2)
    print(f'Result: {result}')
```

The first few functions are the same regular functions we've seen a dozen times by now.
The `switchboard` dictionary maps keys to values of the same name, each value being a function.
In the same way that keys in a dictionary can point to strings, numbers, and lists, they can point functions too as functions are just another object.

The newest thing is what's happening in this `if __name__ == "__main__"` conditional statement.
In addition to the functions and variables you declare, your Python files also come with some prepopulated "special" variables, denoted by two underscores before and after the variable name.

This particular special variable gets populated with a string that is the "name" of the file.
If we were to import the `math` module, its `__name__` would be "math".
However, if we run the file directly from the command line with `$ python math.py`, then it's the "main" program.
In that situation, its "name" is "__main__".
In short: **it's a signal that there's special code to be executed only when this file is run from the command line**.
Let's focus in on that block.

```python
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("Run math.py in the following format: python math.py <operation> <number> <number>. The supported operations are 'multiply', 'divide', 'add', and 'subtract'.")
        sys.exit()
    elif len(sys.argv) < 4:
        print("ERROR: You didn't provide enough arguments!")
        sys.exit()
    elif len(sys.argv) > 4:
        print("ERROR: You provided too many arguments!")
        sys.exit()

    operation = sys.argv[1]
    if operation not in switchboard:
        print(f"ERROR: {operation} isn't a supported operation. Try 'multiply', 'divide', 'add', or 'subtract'")
        sys.exit()

    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    result = switchboard[operation](num1, num2)
    print(f'Result: {result}')
```

In this particular case, *when `math.py` is run from the command line*, the `sys` package from the Python standard library is imported.
The `sys` package is specifically for direct interaction with the Python interpreter.
In this particular case, we're inspecting the arguments that were provided when the code was run with the `argv` property.

If I run a Python file like so `$ python filename.py arg1 arg2 arg3`, then `sys.argv` will be populated like `['filename.py', 'arg1', 'arg2', 'arg3']`.
The `sys.argv` property will always be a list, and it will always read the command line arguments as strings.
It'll also always have at least 1 entry.

According to the code block above, we first check to see if the user just tried to run `math.py` on its own.
They may not know how to run the code, so we tell them how it's supposed to work.
**Always make painfully obvious to your user how to use your codebase and its purpose.**
You'll thank yourself when you return to your code 6 months later with no clue what it was about.

After printing a message to the user, we call `sys.exit()`, which stops the execution of the current Python file and returns you to the command line.
Then there's two more checks to make sure that the right number of arguments has been provided.

Once the initial checks are done, we harvest the actual `<operation>` that the user provided.
That'll be the first argument after the filename, and since the filename is in `sys.argv[0]`, the operation must be in `sys.argv[1]`.
As soon as we get the operation we make sure it's a valid one.
If it isn't, we inform and exit.

If all the checks pass, we harvest the two numbers that were passed in, converting them to `floats`.
We then use the provided `<operation>` argument to point to the actual function that executes that operation, pass in the two numbers as arguments to whatever function that is, and print the result.

### Input within the Program

Just like you can take input from the command line, you can prompt the user for new input while the program is running.
To do this, use the aptly-named built-in function, `input()`.

Here's how `input()` works:

1. In your code, set up a variable to receive the return value of the `input()` function
2. Pass a string into `input()` that you want the user to see that prompts them for input
3. User sees the prompt, types something, and hits `<Enter>`
4. What user typed is then stored in a variable as a string

Here's an example:

```python
>>> billie_jean = input('Billie Jean is not my: ')
Billy Jean is not my: lover
>>> print(billie_jean)
lover
```

When you want a more verbose prompt, you'll find it useful to `print()` a message first, then use the `input()` line.

A note: in Python 2 you'll find that `input` works differently. In Python 2, `raw_input` serves the same function as Python 3's `input`.
There's still an `input` function in Python 2, but it'll take your input and evaluate it as if it was a variable or a value.
Be careful!

## Recap

Finally we've covered functions!
Now we can start to write programs that actually DO things, and do them over and over again.
Not only that, but we've talked about 3 different ways of handling user input.

In the next lesson we'll talk about...

- what it looks like when things go wrong
- what to do when we encounter those situations

## Exercises

Note: there are solutions to every exercise in the [solutions](../solutions) directory.

Make sure to use a Python 3 virtual environment.
If you're going to be pushing your code to GitHub then **DO NOT COMMIT THE ENVIRONMENT DIRECTORY (ENV)!**

Don't worry if the code that you write isn't as elegant as possible.
It doesn't have to be, as long as it fulfills the requirements.
If you'd like some feedback on your code, fork this repository, work on a branch named `<your first name>-<exercise name>`, then submit a [pull request](https://github.com/nhuntwalker/python-thirty-minutes/pulls) to this repository from your fork.
**I won't merge your work** but I will comment on the Pull Request as my time permits.

1. **Blackjack: Reloaded**: In the last lesson you started building out a blackjack game. Now refactor the code to include functions and add user input.
    - When `blackjack.py` is run from the command line the user should input alongside the filename an integer from 1-10. Use that number to determine how many decks of cards they'll be playing through. Kill the program with an appropriate message if they provide anything but an integer from 1-10.
    - Write a function called `build_deck` that'll use that initial number to construct the deck.
    - Explicitly prompt the user for how much money they want to play with. The minimum bet will be $20, so their amount needs to be at least that much. If user inputs anything besides a number, print an appropriate error message and reprompt them for input. If they input a number less than 20, print an appropriate error and reprompt.
    - Add a key to the `player` dictionary that represents how much money they have
    - Prompt the user for how much they will bet for the next hand. If they can't cover the minimum bet, print an error and kill the program. If they try to bet more than they have, print an error and reprompt.
    - Write a function called `deal_card` that takes in a dictionary representing the player or the dealer,  a dictionary representing a deck, and optionally a boolean that says whether this is the initial deal or not for a hand (default: True). The function will deal one card from the deck at random into their hand. If it's not the initial deal, print what card just got dealt.
    - After the initial deal, show the user their hand, then ask if they'd like to "hit" (get dealt another card) or "stay" (take no more cards). This should be case-insensitive. If the user types anything besides some variation of "hit" or "stay", print an error and reprompt
    - The same card values and win/loss rules apply as before. If the player wins, they double their bet. If not, they lose their bet.
    - Continue the game as long as there are cards in the deck or the player has money, starting each hand with a prompt for their bet and dealing two cards to each person
    - Feel free to include any other functions that you feel might be useful but aren't mentioned here.
2. **Caribbean Restaurant Point of Sale**: Let's make a command line program that will act as the point of sale for a Caribbean restaurant. This one will have far less explicit direction of what to write, and more about what it should do. Think it through holistically
    - When starting the program up, the user should be greeted by the restaurant and asked if they want to see the menu or just start ordering. The data file for the menu items is [here](../from-notes/03-function-inputs/data/restaurant_menu.csv)
    - After seeing the menu, they should be asked what they'd like to order
    - If what they order is on the menu, add it to their total order. If what they order isn't on the menu, tell them it isn't. Make their input case-insensitive by using [the ".lower()" method](https://www.tutorialspoint.com/python/string_lower.htm) of strings
    - After ordering an item, the user should be asked if they want to order something else or check out.
    - If the user checks out, print out a listing of everything they ordered, the subtotal of their order, the tax, and the grand total. You may also want to suggest tipping. Remember, you're working with money so make sure your output looks like money
    - Along with a receipt, the user should be informed that their food will be ready in some amount of minutes. Then the program should exit.