# Chapter 2 - Iterables, Loops, Functions, and User Input

**Topics**

- [Chapter 2 - Iterables, Loops, Functions, and User Input](#chapter-2---iterables--loops--functions--and-user-input)
    - [Iterables - Collections of Things](#iterables---collections-of-things)
        - [Sequences](#sequences)
            - [Lists](#lists)
            - [Tuples](#tuples)
            - [Strings Revisited](#strings-revisited)
            - [Slicing - Just for Sequences](#slicing---just-for-sequences)
        - [Non-Sequences](#non-sequences)
            - [Sets](#sets)
            - [Dictionaries](#dictionaries)
    - [Loops - Doing the Same Thing a Bunch of Times](#loops---doing-the-same-thing-a-bunch-of-times)
    - [Functions - Saving Logic for Later](#functions---saving-logic-for-later)
    - [The Many Ways to Take User Input](#the-many-ways-to-take-user-input)
    - [Untested Code is Broken Code](#untested-code-is-broken-code)
    - [Recap](#recap)
    - [Exercises](#exercises)

Last lesson we learned about virtual environments, the Python interpreter, writing Python files, strings, `print`, errors (a bit), the `random` module, boolean statements, and `if` statements.
When you list it all like that, it's a lot.
Good!
Let's keep that pace.

In this lesson we're going to cover iterables, loops (`for` and `while`) in more depth, functions, and handling user input.

## Iterables - Collections of Things

There's a very specific property that makes an "iterable" object in Python, but we'll get into that another time.
For now, let's just think of Python iterables as existing within two categories: **sequences** and **non-sequences**.

### Sequences

A sequence in Python is a collection of items that have indexes and can be accessed with those indexes.
What does that look like?
Let's start with one of the more basic Python iterables, the `list`.

#### Lists

Lists in Python are roughly equivalent to arrays in other languages, and even look like them.
They are bounded on either side by square brackets `[]`.
The individual items within the list, the **list elements**, are separated by commas, though a list can also be empty.
A list of 4 integers would look like.

```python
[1, 2, 3, 4]
```

Similarly, a list of some strings might look like this

```python
["foo", "bar", "bin", "bang", "pow"]
```

A Python list can hold any type of value, including other lists!
They can also hold combinations of types, because lists are pretty much indiscriminate about what values they contain.
The following will be as valid of a list as the previous two examples:

```python
["one", 2, 3.0, ["f", "o", "u", "r"]]
```

You can construct a list from square brackets as we have above, or using the `list()` type constructor (i.e. the thing that builds all lists).
In many cases, your lists won't be built pre-filled with values.
Instead you'll start with an empty list and add stuff to it.
Let's do that.

Here's an empty list

```python
>>> food = []
```

For whatever reason, we want this list to contain the names of foods.
Currently it's empty.
If we want to add, say, "eggs" to the list of foods, we can `append()` it to the list.

```python
>>> food.append("eggs")
```

The `append()` method returns nothing.
Instead, it takes action on the list, adding whatever value is provided to the end of the list as the last item in the list.
In adding this new item, it **_mutates_** the list.
This term will have more meaning a bit later.

`append()` will only let you add one item at a time.
You might be thinking to yourself "well, maybe I can add multiple items if I separate them by commas?".
No. No you can't, it'll throw an error.

"What if I chain `append()` methods? Can I add multiple items that way?"
Let's say that you did that.
It might look like...

```python
>>> food.append("bacon").append("salad")
```

In this instance what happens is that first Python would add `"bacon"` as the last item in the food list.
As was mentioned before, the `append()` method returns nothing.
Literally, it returns an object called `None`, which possesses no methods.
So, after calling `.append("bacon")` you have a `None` object, and you're then trying to call `.append("salad")` on a `None` object.
`None` doesn't *have* a method called `.append` that you can use.
Whenever you try to use a method that an object doesn't possess, you'll see an error like this:

```python
>>> food.append("bacon").append("salad")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'append'
```

Ok, back to lists.
`.append()` adds one item at a time to a list.
You can also add many items at once with `.extend()`.
You have to give `.extend` another iterable, e.g. a `list`, to...*extend* the list.
`.extend` will then add each item in the new iterable to the list.

```python
>>> food.extend(["salad", "steak", "biscuits", "danishes"])
>>> print(food)
['eggs', 'bacon', 'salad', 'steak', 'biscuits', 'danishes']
```

We've seen that we can add things to a list.
That's great!
How about accessing things within a list we've built?

As was mentioned, one of the defining properties of a Python sequences is the possession of **indexes**.
An index is a number that corresponds to a position in a sequence.
If you provide a given sequence with that number, it'll hand back to you the value at that position in the sequence.
You provide a sequence with an index using square brackets `[]`.

All Python sequences start at 0 on the leftmost side and go up from there.
Let's see this with the following example:

```python
>>> nonsense = ["foo", "bar", "bin", "bang", "pow"]
>>> nonsense[0]  # <-- give me the item at index 0
'foo'
>>> nonsense[2]
'bin'
>>> nonsense[-1]
'pow'
```

That last example shows that you can access items within a sequence with **negative indexing**.
In Python, the index `-1` corresponds to the last object in the sequence.
Accordingly, `-2` is the second to last object, `-3` is the third to last object, etc.
If you try to provide a list with an index it doesn't possess, you'll get an `IndexError`

```python
>>> nonsense[99]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Just like you can retrieve values from a collection by index, you can assign values to an *existing* index the same way that you'd assign values to a variable.

```python
>>> nonsense[4] = "flerg"
>>> print(nonsense)
['foo', 'bar', 'bin', 'bang', 'flerg']
```

If you try to assign a value to an index that the list doesn't already possess, you'll get the same sort of `IndexError` we saw above.

In addition to getting and setting values, we can remove values from a list with the `.pop()` method.
`.pop()` is a little bit special.
Called on its own, the `.pop()` method simply removes and returns the last item in the list.

```python
>>> print(nonsense)
['foo', 'bar', 'bin', 'bang', 'flerg']
>>> nonsense.pop()
'flerg'
>>> print(nonsense)
['foo', 'bar', 'bin', 'bang']
```

Because `.pop()` is a "remove and return" operation, you could take the returned value from `.pop()` and assign it to a variable, or do whatever else you want with it.
If you `.pop()` on an empty list, you'll get an `IndexError`.

You can also pass an index into the `.pop()` method and the item at that index will be removed and returned.

```python
>>> nonsense.pop(2)
'bin'
>>> print(nonsense)
['foo', 'bar', 'bang']
```

Lists are about as basic of a container as you can get in Python.
At least, it is next to this next one.

#### Tuples

The Python `tuple` (I pronounce it "two-pull", but many say "tuh-pull" and those people are weird) is the most basic container, holding items like a list but removing all of the functionality that would change the container.
As such, the `tuple` is an **immutable** (unchangeable) container.

In practice, this means that once I construct a tuple (using parentheses) I can't really do much of anything to it.
The methods actually don't exist.

```python
>>> clothes = ("hat", "pants", "shirt", "socks")
>>> clothes.append("shoes")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>>
>>> clothes[1] = "sweater"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

I can still access the values by index, even if I can't reassign the values at those indexes.

#### Strings Revisited

Strings are also sequences!

They're containers specifically for text, and they're much like tuples in the sense that they're immutable once they've been constructed.
They're constructed with, as was mentioned in [the last lesson](./01-first-program.md#more-fun-with-strings), single quotes `' '`, double quotes `" "`, and triple quotes of either type `''' ''', """ """`.

You can access the individual characters by index like values in any other sequence.

```python
>>> name = "Nicholas Hunt-Walker"
>>> print(name[2])
c
```

While you can't modify strings, you can concatenate two strings together using the `+` operator.

```python
>>> city = "Seattle"
>>> state = "Washington"
>>> print(city + ", " + state)
Seattle, Washington
```

Or you could use the string formatting that we learned [last lesson](./01-first-program.md#back-to-strings-and-things) to construct new strings from existing ones.

```python
>>> place = f"{city}, {state}"
>>> print(place)
Seattle, Washington
```

#### Slicing - Just for Sequences

One thing I haven't covered yet has been **slicing**, or being able to access a section of a sequence.
In Python, slicing is pretty straightforward and will look a lot like indexing.
This makes sense, since the slices depend on indexing to return data to you.

Slicing looks the same whether it's a list, tuple, or string.
I'll try to provide examples of each.

Enough preface.
To slice a Python sequence you use square brackets, and provide the starting index and the ending index (which won't be included).
For example, let's say I had this list of numbers `[17, 95, 86, 40, 21, 70, 15, 79, 13, 27]` and I wanted all the numbers from index 2 up to but not including index 5.

```python
>>> numbers = [17, 95, 86, 40, 21, 70, 15, 79, 13, 27]
>>> numbers[2:5]
[86, 40, 21]
```

With slicing, the syntax is always `container[start_index:end_index:step_size]`.
By default, the `step_size` is always `1`.
So above, when I sliced from index 2 up to index 5, I retrieved values at indexes 2, 3 (2 + 1), and 4 (2 + 1 + 1).
If I wanted every other value, I could provide a step size of 2.

```python
>>> numbers[2:8:2]
[86, 21, 15]
```

And now I've got numbers at index 2, 4 (2 + 2), and 6 (2 + 2 + 2).

My step size doesn't need to always be positive!
You'll commonly find Python developers walking backward through their sequences (e.g. reversing a list) using syntax like this:

```python
>>> phrase = "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration."
>>> phrase[::-1]
'.noitaretilbo latot sgnirb taht htaed-elttil eht si raeF .rellik-dnim eht si raeF .raef ton tsum I'
```

The above syntax is saying start at the very first index, go up until the last index, including the last index, and step backward one index at a time.

Unlike straight indexing, you can slice outside of the range of your sequence without throwing an error.

```python
>>> phrase[22:907]
'is the mind-killer. Fear is the little-death that brings total obliteration.'
```

What is returned to you is just as much as you can slice out of the sequence you have, starting at the index you provided.
Of course, slices that lie completely outside of the existing index range will return to you an empty sequence.

```python
>>> favorite_things = ('kettles', 'mittens', 'packages tied with string')
>>> favorite_things[5:12]
()
```

### Non-Sequences

There are two other built-in containers in the Python language worth noting: dictionaries (a.k.a. `dicts`) and sets.
Let's dig into those a bit, starting with sets.

#### Sets

The idea for sets comes from mathematics, where a numerical set is collection of **_distinct_** objects.
Yes, that word is bolded AND italicized for a reason.
You'll find that one of the main ways that sets are used in Python codebases is to create a collection of **unique values**.

You can build a `set` from the ground up using the curly braces `{}`, separating your values by commas.
You'll end up creating something that only has one instance of every value, no matter how many copies you may put in.

```python
>>> example = {1, 2, 3, 2, 1, 2, 3}
>>> example
{1, 2, 3}
```

You can also build a set out of pre-existing sequences.
Let's say I wanted to find out all of the unique characters in my name...

```python
>>> name = "Nicholas Hunt-Walker"
>>> unique_letters = set(name.lower())
{'e', 'u', 's', 'r', 'k', 'a', ' ', 'o', 'l', 't', 'w', 'c', '-', 'h', 'n', 'i'}
```

Note how the above arrangement of letters doesn't follow any order with respect to the string it deconstructed.
No matter how it may _seem_, **sets in Python do not have an inherent order**.
Don't be fooled by appearances!
Because sets don't have any order, you can't access the values within by index.
You can't have an index if your container has no order!
What would be at position 0?

Sets are not immutable objects, so you can `.add()` and `.remove()` from a set to your heart's content.
Calling the `.add()` method on a set is a great way to, say, run through some data and only collect the unique values in that data set.
After all, you'd only be adding a thing if it wasn't already present!

The `.add()` method takes one value as an argument.

```python
>>> unique_letters.add(1)
>>> print(unique_letters)
{'e', 1, 'u', 's', 'r', 'k', 'a', ' ', 'o', 'l', 't', 'w', 'c', '-', 'h', 'n', 'i'}
```

The `.remove()` method also takes one value as an argument.
However that value must be in the set.
Otherwise, Python will throw you an error.

```python
>>> unique_letters.remove('u')
>>> print(unique_letters)
{'e', 1, 's', 'r', 'k', 'a', ' ', 'o', 'l', 't', 'w', 'c', '-', 'h', 'n', 'i'}
>>> unique_letters.remove('u')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'u'
```

There's a whole host of other things you can do with sets, but we can just leave it here for now.

#### Dictionaries

Even moreso than lists, dictionaries (a.k.a. `dicts`) are probably the most versatile of Python's built-in objects.
In other languages they're known as "object literals", "associate arrays", and "hash tables", but it's all the same.
Here's the basics of the Python `dict`.

You initialize an empty dictionary using either `dict()` or `{}`.
To put values into a dictionary, you provide a "key" with which to access that value.
Similar to how in lists you have an index that points to a value, in a dictionary you have a key that points to a value.

```python
>>> students = {}
>>> students["first grade"] = ["Tonell", "Zalinia", "Aikira", "Elaya", "Zhaire"]
>>> students["second grade"] = ["Dominique", "Hazell", "Antwon", "Dmitry"]
>>> print(students)
{
  'first grade': ['Tonell', 'Zalinia', 'Aikira', 'Elaya', 'Zhaire'],
  'second grade': ['Dominique', 'Hazell', 'Antwon', 'Dmitry']
}
```

Although you can use any immutable value as a "key" for a dictionary, we tend to use strings.
The values, in turn, can be anything.
Like literally, anything.
Anything that can be assigned to a variable in Python can be a value in a dictionary.
In fact, that's how Python maintains your list of available variables; everything in Python ends up falling back in some way, shape, or form to a dictionary.

Now that our dictionary has keys that map to values, we can access those values by using their unique, immutable key, just like we can access a value in a list by knowing its index.

```python
>>> print(students["first grade"])
['Tonell', 'Zalinia', 'Aikira', 'Elaya', 'Zhaire']
```

You can assign values to an existing or new key, you can delete existing keys, you can do everything that you'd normally do with a variable assignment.

As of Python 3.6, dictionaries are now ordered objects.
What this means is that the order in which you declare keys is the order you'll always see them when you print the dictionary.
However, even though dictionaries are ordered, you can't slice on them because **dictionaries aren't sequences**.

If you want to know what keys a dictionary has available for you to use, you can check using the `.keys()` method.
As of Python 3, the object you get back from `.keys()` will look like but not quite be a list of all of the keys present in your dictionary.
You can get iterate through the object (we'll talk about this in a bit), but you can't actually access its data by index.
You can similarly get key-value pairs by using the `.items()` method.

```python
>>> print(students.keys())
dict_keys(['first grade', 'second grade'])
>>> print(students.items())
dict_items([('first grade', ['Tonell', 'Zalinia', 'Aikira', 'Elaya', 'Zhaire']), ('second grade', ['Dominique', 'Hazell', 'Antwon', 'Dmitry'])])
```

Is with every object we've discussed thus far, there's far more you can do with `dicts` than was shown here.
However, we have a good foundation for these basic containers and we can start to do some interesting stuff with Python, as we'll see in the next section.

### Python Container Miscellania

This isn't even going to be that big of a subsection.
Just some stuff I couldn't quite figure out where to place it.

- Yes, Python `set`s and `dict`s both use curly braces. They're also both not sequences, and up until recently were both unordered. That being said, they act very differently. Remember, sets are containers containing only unique values, while dictionaries are key-value pairs.
- Whether you add values to any of these containers or not, they all inherently keep track of their own lengths. You can check that length with the built-in `len()` function. It will _**always**_ return an integer value of 0 or more

```python
>>> len(students)
2
>>> len(students['first grade'])
5
>>> len(unique_letters)
16
```

- Of all these containers, the only one that acts a little weird when you try to make an instance containing one value is the tuple. If you're making a tuple with one element only, leave a trailing comma before you close the parentheses. `my_var = (5,)` is a tuple with one value of 5. `my_var = (5)` is the integer "5".

## Loops - Doing the Same Thing a Bunch of Times

As the subtitle says, whenever you want to perform the same operation or set of operations multiple times, a loop will be your tool.

### For loops, for finite iteration

We saw briefly in the previous lesson that the structure of a `for` loop in Python is as follows:

```python
for <item> in <some iterable thing>:
    <a line of logic>
    <another line of logic>
    <really however much logic you want>
```

- You must have the `for` and `in` keywords on your initializing line, as well as the colon `:` at the end.
- You MUST indent your next line under the initial `for` loop line.
[Standard Python convention](https://www.python.org/dev/peps/pep-0008/) says that it should be 4 spaces.
Make it 4 spaces.
- When you're done with your loop, unindent out to the same level as the left edge of "`for`". **There is no other way to end a for loop in Python**

Now that we've talked about containers, we have plenty of things that we can iterate through to show *how* loops can work.
For example, let's say that we have a list of foods and we want to take each one and print out that we love said food.
If we were doing it the long, inefficient, unmaintainable clunky way, we might write...

```python
>>> foods = ["beets", "ice cream", "chocolate", "sushi", "blackberries", "avocadoes", "pomegranates", "brie", "bread", "salami"]
>>> love_string = "hot damn do I love {}!"
>>> print(love_string.format(foods[0]))
hot damn do I love beets!
>>> print(love_string.format(foods[1]))
hot damn do I love ice cream!
>>> print(love_string.format(foods[2]))
hot damn do I love chocolate!
>>> print(love_string.format(foods[3]))
hot damn do I love sushi!
>>> print(love_string.format(foods[4]))
hot damn do I love blackberries!
>>> print(love_string.format(foods[5]))
hot damn do I love avocadoes!
>>> print(love_string.format(foods[6]))
hot damn do I love pomegranates!
>>> print(love_string.format(foods[7]))
hot damn do I love brie!
>>> print(love_string.format(foods[8]))
hot damn do I love bread!
>>> print(love_string.format(foods[9]))
hot damn do I love salami!
```

The code above is an atrocity.
Seriously, not only is it tedious to write, but it's ugly to look at!
It's so bad that I didn't even write it out manually--I USED A LOOP TO GENERATE THAT CODE BLOCK!

Loops are for the lazy.
Good programmers are lazy.
Become lazy. Become a good programmer.

All jokes aside, this brings us to one of the standard guidelines of writing in any programming language: as much as you can stand to avoid it, **DON'T REPEAT YOURSELF**.
This of course has its nuances.
Should you start rethinking your code if you wrote the same bit twice? Probably not.
Three times? Maybe start thinking about it. Depends on the circumstance.
Five times? Yeah, start rethinking your code.

Instead of writing that same code 10, 100, or 1000 times in order to perform some operation, write it once and let the programming language do the heavy lifting.
In this particular case we know we want to iterate 10 times--once for each food item in the list of foods.
We set up our `for` loop like so:

```python
>>> foods = ["beets", "ice cream", "chocolate", "sushi", "blackberries", "avocadoes", "pomegranates", "brie", "bread", "salami"]
>>> love_string = "hot damn do I love {}!"
>>> for i in range(10):
...     print(love_string.format(foods[i]))
...
hot damn do I love beets!
hot damn do I love ice cream!
hot damn do I love chocolate!
hot damn do I love sushi!
hot damn do I love blackberries!
hot damn do I love avocadoes!
hot damn do I love pomegranates!
hot damn do I love brie!
hot damn do I love bread!
hot damn do I love salami!
```

Read it aloud, it'll make more sense that way:

**for "i" in range(10)...** effectively means: create an iterable with the values 0 through 9. For each value, assign it to the variable `i`. Then...

**print(love_string.format(foods[i]))**... print my `love_string`, substituting the item in the `foods` list at index `i` for the placeholder in my `love_string`.

Does this mean "iterate 10 times and when you iterate perform this operation"? Yes, but it's only a strong implication.
The code-to-english bit that I wrote above is what it really means.
Let's see another example to see how this can differ.
It's important to get the literal understanding of loops early.

Instead of looking at indexes of the `foods` list, I can access each food item individually and just shove that in my `love_string`.
Behold!

```python
>>> foods = ["beets", "ice cream", "chocolate", "sushi", "blackberries", "avocadoes", "pomegranates", "brie", "bread", "salami"]
>>> love_string = "hot damn do I love {}!"
>>> for food in foods:
...    print(love_string.format(food))
...
hot damn do I love beets!
hot damn do I love ice cream!
hot damn do I love chocolate!
hot damn do I love sushi!
hot damn do I love blackberries!
hot damn do I love avocadoes!
hot damn do I love pomegranates!
hot damn do I love brie!
hot damn do I love bread!
hot damn do I love salami!
```

How many times am I iterating?
You know what, I have no idea (10, the answer is 10).
I don't need to have an idea.
I know that I want to **access every item in `foods`**, so I tell my `for` loop to access each one, one at a time, and assign that value to a variable named `food`.
Then, in the context of my `for` loop, my `food` variable has the value of that one food item, and I can use it within my loop logic.

Lists are easy pickings, but any of the containers that we saw above (tuples, sets, strings, dictionaries) can serve as the iterable that a `for` loop would need.
My favorite examples involve dictionaries.

Let's say I have a similar dictionary to the one that I built in the last section, but I have 5 keys instead of just 2.

```python
students = {
  'first grade': ['Tonell', 'Zalinia', 'Aikira', 'Elaya', 'Zhaire'],
  'second grade': ['Dominique', 'Hazell', 'Antwon', 'Dmitry'],
  'third grade': ['Michael', 'Daniel', 'Bridget', 'James', 'Robert', 'Joshua'],
  'fourth grade': ['Jack', 'Rodney', 'Melvin', 'Kirsten', 'Sara'],
  'fifth grade': ['Sharon', 'Anna', 'Jared', 'Dawn']
}
```

For every grade of students that I have, I want to print a nicely-formatted new line for that student's name.
At the end of the day I just want a list of all my students' names.
As with most programming things, there's a number of ways to accomplish this.
Here's one with `for` loops:

```python
# try it!
for grade_level in students:
  for student in students[grade_level]:
    print(student)
```

Ooh, double `for` loop!
Yes, you CAN nest loops. Thanks for asking!

So what's happening here?
When you iterate over a dictionary, you're really only iterating over the keys.
So the first loop is effectively accessing one key in the dictionary at a time.

For each key (a string) that it accesses, it then uses that key on the dictionary to get the value associated iwth that key.
In this case, that value is a list of names.
Then for each name in the list of names, print that name.

If you find that you want to iterate over the length of a container, but also want to have access to the indexes of that container (or want to artificially build indexes), you can do this in two ways.
The classical way is:

```python
for i in range(len(my_container)):
```

Find the length of my container, build a range of numbers for the length of that container, and assign each value to `i`.

The more maintainable, scalable way that you should pretty much choose from here on is

```python
for idx, item in enumerate(my_container):
```

For every `item` in my container, give me an index `idx` that it corresponds to if I were counting things.
`enumerate` returns to you an object that, when iterated over, returns not one but TWO values at a time.
So why not take those two values and assign them to two variables?
As for why this is a scalable, better way, ask me when we get to **Python generators** later on.

### While loops - Go until I say stop!

The structure of a `while` loop is quite a bit simpler than that of a `for` loop.
The flow of logic is essentially:

1. Is some condition True?
2. If the condition is True, run some logic
3. Go back to 1.

As long as that condition evaluates to True, the loop will continue.
Let's see with an example.

```python
count = 0
while count < 25:
    print(f"The count is {count}")
    count += 1
```

Assign the value of `0` to `count`.
**As long as** the value of `count` is less than `25`, `print` the current value of `count`, then increment its value up by `1`.
I'm emphasizing "as long as" here because that's how you should think about `while` loops—as long as that condition is true, the indented logic will run.

`for` loops are for a finite number of iterations.
`while` loops are for conditional iterations.
`while` loops can go on infinitely, and `for` loops typically don't.

### Stop and Go In Iteration

If you find yourself in a position where you want to stop iterating in either one of these types of loops, you can use `break`.
Let's consider a loop that tries to match a pre-determined number by drawing random numbers.

```python
import random

the_number = 4
n_iters = 0
while True:
    n_iters += 1
    the_guess = random.randint(0, 10)
    if the_guess == the_number:
        print(f"The number was guessed after {n_iters} iterations")
        break
```

In the above loop we iterate and guess a number from 0 to 10.
If `the_guess` ends up matching `the_number`, print a message showing how many times it took, and then leave the loop with the `break` statement.
Once the `break` statement is hit, we leave the loop.

**NOTHING ELSE WITHIN THE LOOP HAPPENS AFTER A BREAK STATEMENT**.

If there are nested loops, then the `break` statement only kills the innermost loop.
So with this setup

```python
for character in 'abcd123':
    if character.isnumeric():
        num = int(character)
        while num < 20:
            if num % 3 == 0:
                break
            num *= 2
    else:
        print("This wasn't a number!")
```

The `for` loop will iterate over the `'abcd123'` string one character at a time.
For every character, there will be a check to see if that character is numeric (i.e. is a number) with `.isnumeric()`.
If it is, *as long as* the number is less than 20, check to see if it's evenly-divided by 3.
If it is evenly-divided by 3, **_break out of the `while` loop_** and return to the `for` loop.
If it isn't, then multiply it by 2 and continue through the `while` loop.

The other loop-relevant keyword is `continue`, which tells the loop to stop with the current iteration at that line and go on to the next iteration in the loop.
A loop written like this:

```python
while True:
    print("This is the loop that doesn't end")
    continue
    print("This line will never get hit. Ever.")
```

Will go on infinitely and never hit the second `print` line.
Each time `continue` is seen, the next iteration is started.
If you were to run this code, you would see the line "This is the loop that doesn't end" go on forever, until you killed the process with `CTRL + C`.

## Functions - Saving Logic for Later



## The Many Ways to Take User Input

## Recap

## Exercises