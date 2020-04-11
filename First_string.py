# coding:utf-8

# what_she_does = ' plays '
# her_instrument = 'piano'
# her_name = 'IRIS CHEN'
# artist_intro = her_name + what_she_does + her_instrument
#
# print(artist_intro)
#
#
# num = 1
# string = '1'
#
# print(type('word'))


# name = 'My name is leon'
#
# print(name[0])
# print(name[-4])

# word = 'friends'
# # find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
# # print(find_the_evil_in_your_friends)

# phone_number = '1386-666-0006'
# number1 = int(input('please input a number:'))
# print(type(number1))
# hiding_number = phone_number.replace(phone_number[:number1], '*' * number1)
# print(hiding_number)
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search) + 1) +
      ' to ' + str(num_a.find(search) + len(search)) + ' of num_a ')
print(search + ' is at ' + str(num_b.find(search) + 1) +
      ' to ' + str(num_b.find(search) + len(search)) + ' of num_b ')

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition='With', verb='came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))

