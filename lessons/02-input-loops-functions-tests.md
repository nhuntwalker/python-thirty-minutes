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


## Loops - Doing the Same Thing a Bunch of Times

As we saw before, the structure of a `for` loop in Python is as follows:

```python
for <item> in <some iterable thing>:
    <a line of logic>
    <another line of logic>
    <really however much logic you want>
```



## Functions - Saving Logic for Later

## The Many Ways to Take User Input

## Untested Code is Broken Code

## Recap

## Exercises