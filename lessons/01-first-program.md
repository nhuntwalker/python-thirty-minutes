# Writing your First Python Program

**Topics**

- [Writing your First Python Program](#writing-your-first-python-program)
    - [Getting Started](#getting-started)
    - [Isolating Your Python](#isolating-your-python)

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

