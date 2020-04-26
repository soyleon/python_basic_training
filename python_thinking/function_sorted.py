#!/usr/bin/python
# -*- coding: UTF-8 -*-
import operator
# 获取列表的第二个元素


def take_second(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=take_second)

# 输出类别
print('排序列表：', random)


L = {'b': 1, 'a': 5, 'c': 3, 'd': 4}

print(sorted(L, key=lambda x: L[x]))           # 利用key


students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda s: s[2]))
print(sorted(students, key=lambda s: s[2], reverse=True))