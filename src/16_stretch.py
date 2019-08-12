# maps, filters,

numbers = [1, 2, 3, 4, 5, 6]

""" js version 
newArray = numbers.map(num => num * num)
"""

# useing Python


def square(x):
    return x**2


print(list(map(square, numbers)))

# this can also be done with Lambda without the seperate function

print(list(map(lambda x: x**2, numbers)))

# another example

""" newArray = random_words.map(word => word.toUpperCase())"""
random_words = ['hi', 'bye', 'hello', 'goodbye']


def uppercase(string):
    return string.upper()


print(list(map(uppercase, random_words)))

# filter with Python

print(list(filter(lambda x: x > 3, numbers)))

# using for in python to filter returns all words that start with the letter h

for word in random_words:
    for h in word:
        if h == "h":
            print(word)
