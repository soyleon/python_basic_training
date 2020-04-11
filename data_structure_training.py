# password_list = ['*#*#', '12345']
#
#
# def account_login():
#     password = input('Password:')
#     password_correct = password == password_list[-1]
#     password_reset = password == password_list[0]
#     if password_correct:
#         print('Login success!')
#     elif password_reset:
#         new_password = input('Enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changed successfully!')
#         account_login()
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
#
#
# account_login()

# establish 10 txt on the desktop
# def text_create(name):
#     desktop_path = 'C:/Users/Administrator/Desktop/'
#     full_path = desktop_path + str(name) + '.txt'
#     file = open(full_path, 'w')
#     file.close()
#
#
# for i in range(1, 11):
#     text_create(i)


#  compound interest, call functions and reture the
#  interest of every year

#
# def invest(amount, rate, time):
#     for i in range(1, time+1):
#         amount += amount * rate
#         print('year'+str(i)+':'+str(amount))
#
#
# invest(100, 0.05, 10)


#  print even number from 1 to 100
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         i += 1
#     else:
#         i += 1

#  下注金额和赔率
#  1.初始金额为1000元；金额为0时结束，默认赔率为1倍。
# import random
#
#
# def roll_dice(numbers=3, points=None):
#     print('<<<<< ROLL THE DICE! >>>>>')
#     if points is None:
#         points = []
#     while numbers > 0:
#         point = random.randrange(1, 7)
#         points.append(point)
#         numbers = numbers - 1
#     return points
#
#
# def roll_result(total):
#     is_big = 11 <= total <= 18
#     is_small = 3 <= total <= 10
#     if is_big:
#         return 'Big'
#     elif is_small:
#         return 'Small'
#
#
# def start_game():
#     print('<<<<< GAME STARTS! >>>>>')
#     choices = ['Big', 'Small']
#     your_coin = 1000
#     while your_coin > 0:
#         your_choice = input('Big or Small :')
#         your_bet = int(input('How much you wanna bet ? -'))
#         while your_bet > your_coin:
#             print('Your bet should not bigger than your total money')
#             your_bet = int(input('How much you wanna bet ? -'))
#         if your_choice in choices:
#             points = roll_dice()
#             total = sum(points)
#             youwin = your_choice == roll_result(total)
#             if youwin:
#                 print('The points are', points, 'You win !')
#                 your_coin = your_coin + your_bet
#                 print('You gained' + str(your_bet)+', you have' + str(your_coin) + 'now')
#             else:
#                 print('The points are', points, 'You lose !')
#                 your_coin = your_coin - your_bet
#                 print('You lost' + str(your_bet) + ', you have ' + str(your_coin) + ' now')
#         else:
#             print('Invalid Words')
#             start_game()
#     print('Game Over')
#
#
# start_game()

# periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
# print(periodic_table[0])
# print(periodic_table[-2])
# print(periodic_table[0:3])
# print(periodic_table[-10:-7])
# print(periodic_table[-10:])
# print(periodic_table[:9])

# import time
#
# a = []
# t0 = time.clock()
# for i in range(1, 20000):
#     a.append(i)
# print(time.clock() - t0, 'seconds process time')
#
# t0 = time.clock()
# b = [i for i in range(1, 20000)]
# print(time.clock() - t0, 'seconds process time')

# path = "C:Users\Administrator\Desktop\Walden.txt"
# with open(path, 'r') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print('{}-{} times'.format(word, words.count(word)))


# import string
#
# path = 'C:Users\Administrator\Desktop\Walden.txt'
#
# with open(path, 'r') as text:
#     words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
#     words_index = set(words)
#     counts_dict = {index:words.count(index) for index in words_index}
#
# for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
#     print('{} -- {} times'.format(word, counts_dict[word]))
