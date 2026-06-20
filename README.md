# List Comprehension

List comprehension is a super concise way to create a new list by applying an expression or a condition to each item in an existing list. 

Consider the following example. We create a new list containing only even numbers from an existing list using a for-loop. 

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
