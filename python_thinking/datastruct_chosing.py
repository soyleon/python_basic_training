"""
              practice 1
write a program to read a file. split every line into
word. Delete the whitespace and punctuations. Then convert
all of the words into low case

"""

import string
word = []
with open('somewords.txt') as file:
    for raw_word in file.read().split():
        word.append(raw_word.strip(string.punctuation).lower())
print(word)

