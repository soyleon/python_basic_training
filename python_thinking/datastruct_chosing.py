"""
              practice 1
write a program to read a file. split every line into
word. Delete the whitespace and punctuations. Then convert
all of the words into low case

"""

# import string
# word = []
# with open('somewords.txt') as file:
#     for raw_word in file.read().split():
#         word.append(raw_word.strip(string.punctuation).lower())
# print(word)


"""
            Practise 2
    fix the program above to read a book that you just 
    downloaded. Jump the information of the beginning and 
    to process it in the same way. Then modify it to count
    how much of the whole words and every word.
    Print the number of the word unrepeated.
"""

import string
words = []
with open('Walden.txt') as file:
    for raw_word in file.read().split():
        words.append(raw_word.strip(string.punctuation).lower())
print(len(words))

words_index = set(words)
count_dict = {index: words.count(index) for index in words_index}

count_sorted = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
print(count_dict)
print(count_sorted)
for word in count_sorted:
    print('{} --{}times.'.format(word, count_dict[word]))
