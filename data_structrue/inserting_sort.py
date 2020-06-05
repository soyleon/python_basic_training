"""
插入排序
"""


def insertion_sort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):  # range函数包括前值，不包括后值
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break


if __name__ == "__main__":
    a_list = [10, 4, 3, 77, 5, 99, 3, 1]
    insertion_sort(a_list)
    print(a_list)
