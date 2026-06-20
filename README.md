# List Comprehension

List comprehension is a super concise way to create a new list by applying an expression or a condition to each item in an existing list. 

Consider the following example. We create a new list containing only even numbers from an existing list using a `for` loop. 

```
res = []
x = [1, 2, 3, 4, 5, 6]
for num in x:
	if num % 2 == 0:
		res.append(num)

print(res)
#  [2, 4, 6]
```

The above code works just fine. But it’s verbose and kind of clunky (according to the [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)).

By using a list comprehension, we can write the same program like this: 

```
x = [1, 2, 3, 4, 5, 6]
res = [val for val in x if val % 2 == 0]
print (res)
#  [2, 4, 6]
```

It’s not just concise; it’s beautiful and [Pythonic](https://en.wikipedia.org/wiki/Zen_of_Python#Being_Pythonic)!

We can even use functions in a list comprehension. We’re going to create a new list by squaring every integer within an existing list.

```
def square_number(n: int) -> int:
	return n * n

x = [1, 2, 3, 4, 5]
res = [square_number(val) for val in x]
print (res)
#  [1, 4, 9, 16, 25]
```

We can also combine both conditions and functions in a single list comprehension. We are going to print a new list with squares of only even numbers using the function from above.

```
x = [1, 2, 3, 4, 5, 6]
res = [square_number(val) for val in x if val % 2 == 0]
print (res)
# [4, 16, 36]
```

The format of list comprehension is simple:

`result_list = [expression for item in iterable if condition]`

- expression: what you want to do to the item before you put it in your new list (e.g., square_number(val)).
- for item in iterable: the standard loop that will step through each value in the array.
- condition (optional): to check if an individual value should be included at all.

## Assignment (difficulty: 5)

We are working on building a new programming language called **RobustaScript**, and we need to have functionality called “map” for transforming original arrays (yes, we are calling ‘lists’ arrays in this language) to a new array. 

We wanted to use `for` loops, but we’re writing Python, and loops would make this functionality slow (Ouch).

Complete the function `map`. It takes a list of values of any type and a function that transforms an item to a new item and returns a new list.
