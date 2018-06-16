# Chapter 1 - Writing your First Python Program

**Topics**

- [Chapter 1 - Writing your First Python Program](#chapter-1---writing-your-first-python-program)
    - [Getting Started](#getting-started)
    - [Isolating Your Python](#isolating-your-python)
    - [Geez, Let's Write some Python!](#geez--lets-write-some-python)
        - [Keeping Data for Later](#keeping-data-for-later)
        - [More Fun With Strings](#more-fun-with-strings)
        - [Detour: Errors and Indentation](#detour--errors-and-indentation)
        - [Back to Strings and Things](#back-to-strings-and-things)
            - [1. Keep track of the position of the values you're using to fill the formatted string](#1-keep-track-of-the-position-of-the-values-youre-using-to-fill-the-formatted-string)
            - [2. Name the placeholders and associate data with those names](#2-name-the-placeholders-and-associate-data-with-those-names)
            - [3. Use Python 3.6's fancy f-string](#3-use-python-36s-fancy-f-string)
    - [Python in Files](#python-in-files)
    - [The First Program - The Dice Roller](#the-first-program---the-dice-roller)
    - [Making Decisions With Conditionals](#making-decisions-with-conditionals)
    - [Recap](#recap)
    - [Exercises](#exercises)

Hey!
You want to learn Python!
Awesome!

Python is a programming language that runs on a computer, in this case on your computer, and executes code.
Book done!
No, wait, there's a lot more to it than that.
It can do a lot of stuff, and I can't wait to show you.

## Getting Started

First, let's make sure that you have Python on your computer.
I'm biased, so I'm going to assume that you're on a Mac.
Open your Terminal application (or whatever other application lets you access the command line) and type `which python`.
It should look something like:

```
$ which python
/usr/bin/python
```

The path that gets printed to your terminal window doesn't have to be the same one that's in my example.
As long as some path has been printed, you have Python on your computer.
Congrats!

If you executed that command and didn't see any path printed to the screen, that's ok.
There's a number of great ways to get Python onto your computer.
You could download the latest version from [Python.org](https://www.python.org/), but I'm going to suggest a different way.
It'll set you up for some other successes in later lessons.

You should do this first part even if you have Python installed.

We're going to install a tool on your Mac called [Homebrew](https://brew.sh/).
It's a package manager specifically for Macs, and allows you to download and install a ton of programs in a consistent, sustainable way.
As the documentation states, you can install Homebrew with the following command:

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

You can just copy and paste that right into your terminal, then execute.
...It's worth noting that you should be connected to the internet in order for this to work.

Now that you've got Homebrew on your machine, let's get you some Python!
To use Homebrew to install packages, type `brew install <package name>`.
How do you think you'll be getting Python?

```
$ brew install python
```

And just like that you'll have access to the latest version of Python!

If you've installed Python through Homebrew, it'll tell you what version you got (v. 3.6.5 as of this writing).
If you've already got Python, great!
Check its version with `python -V`.
If the version that you have isn't version 3.6 or better, try `python3 -V`.
If you still don't have v. 3.6 or better, open an [issue](https://github.com/nhuntwalker/python-thirty-minutes/issues) or hit me up in some other way and we can figure this out.

## Isolating Your Python

So you've either already had Python or you now have Python everywhere.
Great!

Wait no, not that great!

You're going to be a developer and work on a great many different projects, all potentially using different versions of different tools.
If you install all of those into your global Python you're going to run into problems.

**Enter: virtual environments**

A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a directory that has its own little Python installation and its own set of libraries that are isolated from the global system.
It makes it so that when you're in the environment, you have access to all of the tools installed in that environment.
When you're not in the environment, you're just using the global Python installed on your computer and whatever Python libraries are installed with it.

Let's create a Python 3 virtual environment.
First, make a directory for our Python projects, branching off from our home directory.

```
$ cd ~
$ mkdir python-projects
```

Navigate to the `python-projects` directory that you just created.
Create another directory inside of `python-projects` where we'll build our first project: the dice roller!

```
$ cd python-projects
$ mkdir dice-roller
```

Navigate to the dice roller, and here we'll create our first virtual environment.

```
$ cd dice-roller
```

To create a virtual environment in any directory, run the following command in that directory:

```
$ python3 -m venv ENV
```

What does this command do?
`python3` is the command to invoke Python version 3 that you downloaded earlier with Homebrew.
The `-m` flag says "what's about to follow is a Python module".
We'll learn what a module is later.

You're saying, effectively, hey Python 3, can you run this module called `venv`?
When you run that module, give the directory that contains the virtual environment the name `"ENV"`.

So you've now made a virtual environment, but it's not yet activated.
In order for this thing to be useful, you have to activate it!
Conveniently, the `ENV` directory contains a file called `activate` in `ENV/bin/activate`.
It's the bash script whose job it is to isolate Python in this one environment.

It would probably be a good idea to know how to activate the environment.
If you're in the `dice-roller` directory, type:

```
$ source ENV/bin/activate
(ENV) $
```

If you ever want to leave the environment, run the `deactivate` command that the environment gives you.
Anyway, let's stay in the environment.

Here's the great thing about being in a virtual environment: the regular `python` command now maps to Python 3!
So we don't have to decide between different versions of Python.
We'll always be in Python 3.

## Geez, Let's Write some Python!

Enough with the setup, dammit!
We're here to learn a language not standards of configuration!
In your terminal type `python` to start the Python prompt.

```python
(ENV) $ python
Python 3.6.5 (default, Mar 30 2018, 06:41:53) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

We're developers, right? Right.
When we're trying something new in programming, we always start by displaying "Hello, world!" somewhere.
In Python, when we want to print words to the screen, you call the `print()` function, and pass in the `string` that you want printed as an argument.
So, without further ado...

```python
>>> print('Hello, world!')
Hello, world!
>>>
```

When you want to create a string in Python (also known as a "string literal"), you use quotation marks and place some text in between.
Python doesn't care whether you use single or double quotes, as long as you start and end with the same types of quotes.
What follows are examples of strings in Python:

- `'I am a string'`
- `"I am also a string"`
- `"""Wait, I'm also a string?!"""`
- `'''Oh yeah, you can do this with single quotes too'''`

Yes, the third and fourth ones are indeed also Python strings.
Python allows you to use triple quotes to create a multi-line string.
It maintains all the formatting and whitespace that you put inside of it, exactly as you wrote it.

### Keeping Data for Later

Printing an individual string is great, but it's not of much use if it's just one-and-done.
As with other programming languages, Python lets you store data in a variable that you can use later.
You can store data using the assignment operator, `"="`.

```python
>>> hello = "Hello, world!"
>>> print(hello)
Hello, world!
```

No special keywords necessary to assign values to variables like "var", "let", or "const".
You don't even need to declare the type of value you're going to assign (although as of Python 3.6 you can if you really really want to).
You just need a properly-formatted name, containing only letters a &rarr; z, A &rarr; Z, numbers 0 &rarr; 9, and underscores.

Whenever you assign a string to a variable name, that variable name is now a reference to a copy of that string in memory.
Once assigned, _**you cannot change that string!**_

Let me be clear about what I mean by that.
Above I assigned `"Hello, world!"` to the variable name `hello`.
If I perform an operation on that string, like `.lower()`

```python
>>> hello.lower()
'hello, world!'
>>> hello
'Hello, world!'
```

Oh did I mention that if you just type out the variable name and hit `<Return>` the Python interpreter will print the value of that variable?
I have now!

Anyway, notice how even after calling the string method that converts every character in the string to its lowercase form, the value assigned to the `hello` variable didn't actually change.
I could always **re-assign** the value that `hello` holds if I wanted to mutate the string, but I can't actually change the value of `hello` without reassignment.

```python
>>> hello = hello.lower()
>>> hello
'hello, world!'
```

Let's say "Hello" to some other things.

One of the great things about strings in Python is that they can be formatted to contain whatever we want.
All that we have to do is provide the appropriate data.
So, instead of **hard-coding** the message of `"Hello, world!"`, we can put in a placeholder that can be filled with the data we want.

### More Fun With Strings

In versions of Python prior to Python 3.6, you could format a string using the `.format()` string method.
Here's how it works.

```python
>>> msg = "Hello, {}!"
>>> print(msg.format('universe'))
'Hello, universe!'
```

The `"{}"` in the string is just a placeholder.
If `.format()` is never called on the string, you would just end up printing those curly-braces as-is.
If you call `.format()` though, whatever argument you pass into the `.format()` method will fill that placeholder.

```python
>>> nouns = ["sunshine", "rain", "summer", "Spain", 42]
>>> for noun in nouns:
...     print(msg.format(noun))
... 
Hello, sunshine!
Hello, rain!
Hello, summer!
Hello, Spain!
Hello, 42!
```

In this example we have declared a Python `list` named `nouns`.
That list has a variety of data types, because Python lets you do that.
You can use the `for` loop control structure to perform the same operation a bunch of times, like calling `print()` and formatting the string with a new word from that list every time.
And every time print is called, that placeholder is filled with some new data without changing the original string.
Useful!

### Detour: Errors and Indentation

If you're following along in your own Python prompt and tried to write the `for` loop, you might have gotten something like this

```python
>>> for noun in nouns:
... print(msg.format(noun))
  File "<stdin>", line 2
    print(msg.format(noun))
        ^
IndentationError: expected an indented block
```

"Yeah, Nick! What was that about? I wrote exactly what you did!"
Yeah...no you didn't.
You see, Python is a language that sees significance in **white space**, or the spaces between characters.
What I did when I wrote my `for` loop in the Python prompt was write the first line of the loop, `for noun in nouns:`, hit `<Return>`, then hit `<Tab>`.
After hitting `<Tab>` I wrote the second line of my loop.

I **_indented_** the contents of the loop.
With Python, there's no "end" statement that kills a `for` loop.
Whatever's indented underneath the initial line of the loop is considered a part of the loop.
Once you unindent, you're no longer writing code that pertains to the loop!

If you don't indent, you get that `IndentationError` noted above.
It's a type of `SyntaxError`, or rather an error in the way that you wrote your code.
Whenever an error of any type is encountered in your codebase, the engine that interprets your Python code (**the Python interpreter**) will stop, notify you of the error, and kill the thing that you were attempting to do.
There's ways to get around that, which we'll get to later.
Just know that bad Python will be punished!

### Back to Strings and Things

Right, so string formatting.
A useful tool that lets one string become one million strings.
Python strings can fill more than one placeholder at a time too, but if you start filling your strings with multiple placeholders you're going to want to keep track of them.
As with many things in Python, there are a number of ways to do that.

#### 1. Keep track of the position of the values you're using to fill the formatted string

```python
>>> msg = "For breakfast I like to eat {0}, {1}, and {2}"
>>> print(msg.format('eggs', 'bacon', 'potatoes'))
For breakfast I like to eat eggs, bacon, and potatoes
```

Position 0 is occupied by "eggs", position 1 by "bacon", and 2 by "potatoes".
If I shuffled the order a bit, the right values will go in the places that I intend.

```python
>>> msg = "I like to {0} {1}, {0} {2}, and {0} {3}!"
>>> print(msg.format('eat', 'apples', 'bananas', 'strawberries'))
I like to eat apples, eat bananas, and eat strawberries!
```

#### 2. Name the placeholders and associate data with those names

When you start filling a string with a lot of data, keeping track of position can start to become a pain.
Starting to think of placeholders as *variables* within the string may ease your burdens a bit.
Consider this example:

```python
>>> msg = """Dear {name},
... 
... Congratulations! Your proposal of {title} has been accepted to this year's conference! We can't wait to hear you give your talk about it, but we do need one more thing from you. We'll need an abstract by {due_date}. Please submit it in the same email chain as your submission for {title} and we'll get that all squared away. After that, we can get you your stipend of ${money} and you can be on your merry way! Thank you, {name}, for submitting to our conference.
... 
... Sincerely,
... Yanine Cole
... Conference of Cool Things and Stuff"""
>>> print(msg.format(
... title="100 Years of Awesomeness",
... due_date="August 31st, 2018",
... money=5000,
... name="Senedra Haynes"
... ))
Dear Senedra Haynes,

Congratulations! Your proposal of 100 Years of Awesomeness has been accepted to this year's conference! We can't wait to hear you give your talk about it, but we do need one more thing from you. We'll need an abstract by August 31st, 2018. Please submit it in the same email chain as your submission for 100 Years of Awesomeness and we'll get that all squared away. After that, we can get you your stipend of $5000 and you can be on your merry way! Thank you, Senedra Haynes, for submitting to our conference.

Sincerely,
Yanine Cole
Conference of Cool Things and Stuff
```

As we saw earlier, you can pass many values to the `.format()` string method, separated by commas.
You can also give them names!
Now you don't have to care about their position in the ordering.
You just assign a value to a name, like a variable.
Then that name gets substituted in the big string by the value you passed.
Neat!

#### 3. Use Python 3.6's fancy f-string

Building on the idea from option 2, if you know that your values are going to be like variables in your string, why not just make them reference actual variables?
Available only in versions of Python after 3.6, there's a special type of string called the **f-string**.
Visually, it's just your normal string pattern with an "f" in front of it, like so:

```python
>>> thing = "blerg"
>>> msg = f"Flerg the {thing}"
>>> print(msg)
Flerg the blerg
```

One big difference is that **_any variable you want to use in your f-string must have already been declared_**.
If you didn't declare the variable, then you get an error.

```python
>>> msg = f"Flerg the {stuff}"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'stuff' is not defined
```

This `NameError` pops up in Python whenever you're trying to use a variable name that hasn't yet had a value assigned.

## Python in Files

Thus far, I've had you writing Python in the Python prompt.
That's an OK way to do things, but let's be real here: you're not going to be writing or running most of your Python programs this way.
Sure, the prompt is a great way to test out little snippets of code, but you can't then pack up your prompt and ship it somewhere else for someone else's use.
Shippable code will come in the form of files (and later, directories).
So, let's make ourselves a Python file!

First, we need to get out of the Python prompt.
I mean, you could always just open another terminal window, navigate to the same working directory, active the environment in that terminal window, then get to work, but why do that when you can just exit the prompt?
To quit the Python prompt just type `exit()` and hit `<Return>`.
Then you get booted back to your normal command line.

OK, so a Python file.
Making a Python file is as simple as making a file ending in `.py`.
On your command line you can do this with the `touch` command.

```
(ENV) $ touch example.py
```

`touch` will create a file for you with the name you gave it if it doesn't already exist in that directory.
Now, let's open that file in your favorite text editor so that we can fill it with stuff.

What's that? You don't have a text editor?

Aight, get your self a text editor then!
I'm writing these words in an editor called [Visual Studio Code](https://code.visualstudio.com/).
Download and install it if you don't have one of your own, it works as well as any other (and it's free!).

After you've gotten yourself the application, go to [this part of its documentation](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line) to find out how to launch the application from the command line.
It'll make this whole coding thing a lot simpler in the near future.

Aight I'm going to assume that by this point you've gotten an editor that you can launch from the command line.
If something isn't working for you, just hit me with an [issue](https://github.com/nhuntwalker/python-thirty-minutes/issues) and we can hopefully get it solved.
Either way, I'm gonna go ahead and assume that you're using VS Code.

Where was I?
Right, the Python file.
So you just made `example.py`.
Open it in your editor with `code example.py`

```python
(ENV) $ code example.py
```

You should be greeted with the most glorious of all things, a blank page.
Here, we can write our Python code.

Let's start simple.
In `example.py` write `print("Hello, world!")` at the top then save the file.
We've seen this sort of thing before, so we should know what to expect: When Python runs this code it'll show the words "Hello, world!" in the command line.

To run a Python file, in your command line type `python`, then a space, then the name of the file you want to run.
In this case, it's `example.py`.
Go into your terminal window and try it out.

```
(ENV) $ python example.py
Hello, world!
```

Exhilirating!
There's something special about things working exactly as you expect them to.

Within a Python file we can encapsulate any logic that we want to have executed, then execute that logic with the `python` command.

## The First Program - The Dice Roller

OK so we can make Python files, great.
Let's make a real program.

The program we're making is the dice roller, and its job will be to simulate rolling dice.
Right now, it'll be fairly straightforward: when the program runs it'll output the result of one rolled six-sided die.
After that, the program will exit.
We'll continue to build on this as we learn more, but for now let's just get something working.

Create a Python file called `roll_dice.py`.
When you're naming your Python files (and directories that hold Python files), you want to make all the names lowercase and separate words with underscores.
You don't *have* to, but it makes it easier on you when you're looking for filenames later on.

If we're being good boys and girls, at the top of `roll_dice.py` we'll include a stand-alone multi-line string that serves to describe what's being encompassed in the file.
That string is a type of **doc string**, or "documentation string".

Doc strings have saved my ass on many occasions, as they remind me of what I was trying to accomplish within a file, function, or class (we'll learn about those latter two in later chapters).
It's extremely helpful for other people, and even future-you, to include docs about everything that you were doing or intend to do in a codebase.

There's all kinds of documentation formatting you can adhere to if you'd like.
I'll point you to [the official Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), also known as PEP 8, for learning about that.
In reality though, you can write your docs in whatever way suits your coding style.
Accurate documentation describing what the file contains and how to use its contents is far better than none at all.

```python
"""Simulate rolling one six-sided die."""
```

A fair dice roll is always random, and with what we know about Python right now (hell, with what I know about Python in total) we can't write all of the logic that it would take to encompass randomness.

Fortunately, we don't have to!
This wheel has already been invented, so let's build on the back of someone else's work and use the [random](https://docs.python.org/3/library/random.html) library!

`random` came installed with Python as a part of what's known as the **Python standard library**.
In general, the Python standard library contains a bunch of useful tools that other people have written far better than you can write them.
They've been (mostly) optimized and vetted, so there's no reason to not use them in lieu of writing that code yourself (unless you just really want to).

To have access to code that exists in an installed library, we can use Python's `import` statement.
It'll look something like `import <library name>`.
When the Python interpreter executes that import statement, it'll look through all of the installed libraries in your environment for a name matching the one you provided.
If it can't find one, it'll raise an error. Like so:

```python
>>> import flerg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'flerg'
```

In `roll_dice.py`, import the `random` library.

```python
"""Simulate rolling one six-sided die."""
import random
```

So, a dice roll can effectively be thought of as the random choice of either 1, 2, 3, 4, 5, or 6.
These are all integers in Python, and the `random` library has a function that we can run that chooses from a range of random integers called `randint()`.
If we want to see exactly how it works, we can open the Python prompt, import `random`, and use the `help` function to read its doc string.

```python
>>> import random
>>> help(random.randint)
```

It'll clear the terminal window and show the documentation attached to the `randint` function.

```
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
(END)
```

Hit `q` to quit that screen of text.

From what the documentation says, all we'll need to do is provide two numbers to `randint`, and it'll spit out (or **return**) a random integer in the range from the first number to the second number.
It's more or less random, so your results will vary.

```python
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
2
```

Let's put this in `roll_dice.py`.

While we could get away with just having the program print a number to the screen and have that be that, we're going to write code my way.
My way is to make what the user has done as obvious as possible with good messaging, so let's make some good messages.

How many die are the user rolling? One.

How many sides does the die have? Six.

What was the result? Some number that'll be populated by the result of `random.randint`.

Let's write that code!

```python
"""Simulate rolling one six-sided die."""
import random

print("🎲 Rolling one six-sided die 🎲")
result = f"You rolled a { random.randint(1, 6) }!"
print(result)
```

Yeah, you can stick emojis in Python 3 strings.
More about that another time, but go wild.

When this code is executed, this is the result:

```
(ENV) $ python roll_dice.py
🎲 Rolling one six-sided die 🎲
You rolled a 6!
```

Congratulations, you've written your first Python program!

## Making Decisions With Conditionals

The little six-line program written above is totes adorbs, but I'm feeling the need to throw a little English on it.
As I mentioned before, I'm heavily in favor of providing my users with big, obvious messages of what was done, or what's currently happening.
As a part of that messaging philosophy, I'm gonna suggest that instead of just providing the user with the number, we give them a symbol that goes with the number.
Need to reel in those visual learners.

We can use text to make symbols of dice!
For example, rolling a "3" might look like

```
 _______
|     o |
|   o   |
| o     |
 -------
```

This is called [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) and isn't Python-specific.

Aight so we can make these ASCII representations in text for all of our possible dice.
How can we decide which one to display?
The simplest thought process just involves a series of conditional decisions.
If a "1" is rolled, show the illustration of the die with 1 showing on its face.
If "2" then show the illustration for 2, etc. etc.

This exact type of conditional flow is encapsulated in Python's **conditional statements**.
There's 3 of them, though only one is absolutely necessary:

- `if <condition>:` (required) - if condition is True, then do what follows
- `elif <condition>:` - if the first condition wasn't true but this one is, then do what follows
- `else:` - if none of the conditions are True, do what follows

The `<condition>` next to the first two must in some way evaluate to `True` or `False`, Python's two **boolean values**.
One way that we can evaluate to `True/False` is via comparisons between things.
Python has a few **comparison operators** to work with that take values on either side

- `A == B` - value A and value B equate to the same value. So `1 == 1` is `True`. `1 == 2` is `False`
- `A != B` - value A and value B are **not** equal. So `1 != 2` is `True`. `1 != 1` is `False`
- `A > B` - value A is **greater than** value B. `2 > 1` is `True`. `1 > 1` is `False`
- `A < B` - value A is **less than** value B
- `A >= B` - value A is **greater than OR equal to** value B. `2 >= 1` is `True`. `1 >= 1` is also `True`
- `A <= B` - take a guess
- `A is B` - the object A is the exact same object as B in memory. More on this another time.
- `A is not B` - the object A is not the exact same object as B.

You can even combine comparison statements to make more complex conditional statements using the `and` and `or` keywords along with some well-placed parentheses.

- `(A == B) and (B < C)` - if A and B are the same value AND B is less than C, this evaluates to `True`
- `(A == B) or (B < C)` - if A and B are the same value, this is True. If B is less than C, this is also True. If both conditions are True, then this is True. All this needs is one condition to pass.

We can use these to make our conditional statements.
I'm thinking it's going to look something like:

```python
roll_result = random.randint(1, 6)
if roll_result == 1:
    # do something
elif roll_result == 2:
    # do something
elif roll_result == 3:
    # do something
elif roll_result == 4:
    # do something
elif roll_result == 5:
    # do something
else:
    # do something
```

By the way, the symbol `#` makes whatever comes after it into a "comment", or inactive code.

Why am I using `elif` instead of `if`?
Well in this one particular instance it doesn't matter all that much.
However, if all those `elif`s were instead `ifs`, then we could run into problems, as each condition would be checked instead of just one.

Let me show an example of the difference.
Let's consider the case where we have a number and we print different things based on what range that number sits in.

```python
num = 1
if num < 2:
    print('This number is less than 2!')
elif num < 5:
    print('This number is less than 5!')
```

When this code is run, we'll see `"This number is less than 2!"` printed to the terminal because `1 < 2` evaluates to `True` and none of the other conditional statements run.

If instead we had this setup:

```python
num = 1
if num < 2:
    print('This number is less than 2!')
if num < 5:
    print('This number is less than 5!')
```

Now instead of just asking one question at a time, we're asking two questions, one after the other.
Is the number less than 2? Yes! Print the message.
Is the number less than 5? Yes! Print this second message.

The difference between `if-elif` and `if-if` chains isn't necessarily a problem, as each has its own useful domain.
However, you do need to be aware of that difference, as it'll determine how your code executes when the time is right.

If we incorporate the branching logic embodied by conditional statements into our `roll_dice.py` program, the file now looks like

```python
"""Simulate rolling one six-sided die."""
import random

print("🎲 Rolling one six-sided die 🎲")

roll_result = random.randint(1, 6)
if roll_result == 1:
    dice_img = """
 _______
|       |
|   o   |
|       |
 -------"""
elif roll_result == 2:
    dice_img = """
 _______
|     o |
|       |
| o     |
 -------"""
elif roll_result == 3:
    dice_img = """
 _______
|     o |
|   o   |
| o     |
 -------"""
elif roll_result == 4:
    dice_img = """
 _______
| o   o |
|       |
| o   o |
 -------"""
elif roll_result == 5:
    dice_img = """
 _______
| o   o |
|   o   |
| o   o |
 -------"""
else:
    dice_img = """
 _______
| o   o |
| o   o |
| o   o |
 -------"""

result = f"You rolled a { roll_result }!"
result = result + dice_img
print(result)
```

So what exactly is happening above?
From top to bottom:

- A doc string is written at the top of the Python file, describing what the file contains and what its use is
- The `random` library is imported into the running Python interpreter
- A print statement shows a message on the command line letter the user know that "dice" are being rolled
- The actual roll (random choice) happens and the result is stored in the obviously-named`roll_result` variable
- The value of `roll_result` is checked, and if any of those checks is `True` the appropriate dice image is assigned to the `dice_img` variable
- The `roll_result` value is inserted into the string being assigned to `result`
- The value previously assigned to `result` is concatenated (i.e. adding one string on the end of another) along with the string value of the `dice_img` variable, and the resulting combined string is assigned to the variable named `result`
- The final output string is printed to the console

Now THAT'S a program!

## Recap

Blah blah blah, bunch of stuff.
What'd you actually do?

- Opened and worked within the Python prompt
- Learned about formatting Python strings
- Learned about the built-in `print` and `help` functions
- Created two Python files
- Learned how to run a Python script with the `python` command
- Learned about doc strings
- Learned about importing code from installed libraries
- Learned about Boolean operators
- Used conditional statements to make decisions in your code

That's...actually quite a bit.
If you don't practice, you might lose it.
Lucky for you, I've got some exercises you can do to help reinforce your skills.

## Exercises

Note: there are solutions to every exercise in the [solutions](../solutions) directory.

Make sure to use a Python 3 virtual environment.
If you're going to be pushing your code to GitHub then **DO NOT COMMIT THE ENVIRONMENT DIRECTORY (ENV)!**

Don't worry if the code that you write isn't as elegant as possible.
It doesn't have to be, as long as it fulfills the requirements.
If you'd like some feedback on your code, fork this repository, work on a branch named `<your first name>-<exercise name>`, then submit a [pull request](https://github.com/nhuntwalker/python-thirty-minutes/pulls) to this repository from your fork.
**I won't merge your work** but I will comment on the Pull Request as my time permits.

1. **Interesting Numbers**: Write a program that will generate a random number between 0 and 250,000. Based on whatever number is generated, only one of the following statements should be printed to the console:
    - `$<the number> is less than most people's household income in the United States! Most people make less than $60,000 per year! That's just a depressing figure.`
    - `<the number> is less than the amount of hours in a year, which is 6,360`
    - `<the number> is more than the median US income, but less than the population of Bridgetown, Barbados (around 110,000)`
    - `<the number> is bigger than all the other thresholds! Damn that's large!`
2. **Zodiac**: Write a program that will generate a random date and use that date to print the characteristics of the [Zodiac sign that it corresponds with](http://astrostyle.com/zodiac-sign-dates/). You can get the characterstics of each sign [here](http://nuclear.ucdavis.edu/~rpicha/personal/astrology/). The month should be a number between 1 (January) and 12 (December). The day of the month should be a number between 1 and 29, 30, or 31 (depending on the month). Example:
    - date: `4/18`; output:
    ```
    4/18 is for Aries!

    Adventurous and energetic
    Pioneering and courageous
    Enthusiastic and confident
    Dynamic and quick-witted 

    Selfish and quick-tempered
    Impulsive and impatient
    Foolhardy and daredevil
    ```
