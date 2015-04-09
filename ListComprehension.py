#!/usr/bin/Python
# William Thing
# 4/19/2015
# Praciticing list comprehension for an interview

import math # used for math.pow

# using imported math pow function returns float instead of integer
list1 = [math.pow(2,x) for x in range(5)]
print list1

# using built in pow() function returns an integer
list2 = [pow(2, x) for x in range(5)] 
print list2

# creates a list of only positive integers squared from 0 to 5 (exclusive)
result = [i*i for i in range(5) if i%2 == 0]
print result

# will create a list of only the first letters in the sentence!
word = "Hello world, my name is William Thing."
print [text[0] for text in word.split()]

# creates a list of only the vowels from the word 
print [text[0] for text in word.split() if text[0].lower() in 'aeiou']

# same output, both split words in the sentence
print word.split()
print [text for text in word.split()]

# for sanity check
print [x for x in range(1,5)]

# nested loops to list comp
result = [i * j for i in range(1,4) for j in range(1,5)]
print result

### some map stuff vs list stuff
def mapstuff(x):
	return x+1

# same result for map and list comp
print map(mapstuff, range(5))
print [x+1 for x in range(5)]

### mapping
input = [x+1 for x in range(10)]
interest = [x+1 for x in range(10)]
def add(x, y): return x + y
print map(add, input, input)

# creating a matrix
matrix = [[x*y for y in range(1,5)] for x in range (1,4)]
print matrix

# transposing a matrix
transposed = [list(row) for row in zip(*matrix)]
print transposed



