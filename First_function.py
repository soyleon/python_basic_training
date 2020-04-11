# def fahrenheit_convert(c):
#     fahrenheit = c * 9 / 5 + 32
#     return str(fahrenheit)
#
#
# C2F = fahrenheit_convert(30)
# print(C2F)


# 设计一个求直角三角形斜边长的函数
# import math
#
#
# def hypotenuse_calculate(right_angle_side_a, right_angle_side_b):
#     hypotenuse = math.sqrt(right_angle_side_a ** 2 + right_angle_side_b ** 2)
#     return hypotenuse
#
#
# (right_side_a, right_side_b) = input('请输入直角三角形的两边').split()
# hypo = hypotenuse_calculate(int(right_side_a), int(right_side_b))
# print('直角边为' + right_side_a + '.' + right_side_b + '的三角形，斜边为 :' + str(hypo))

def text_create(name, msg):
    desktop_path = 'C:/Users/Administrator/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)


censored_text_create('111', 'lame!lame!lame!') # 调用函数
