# Writing your First Python Program

**Topics**

- [Writing your First Python Program](#writing-your-first-python-program)
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
>>> msg = "Hello, {}"
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