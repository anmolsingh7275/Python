# The reduce() function applies a function cumulatively to the items of an iterable, reducing it to a single value.

# Unlike map() and filter(), reduce() is not built-in in Python 3.
# It is available in the functools module.

import functools

from functools import reduce

# reduce(function, iterable, initializer)
# function → A function that takes two arguments

# iterable → A sequence (list, tuple, etc.)

# initializer (optional) → Initial starting value



from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
