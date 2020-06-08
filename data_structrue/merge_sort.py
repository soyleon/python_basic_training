#  coding:utf-8


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    left_li = merge_sort(alist[: mid])
    right_li = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    a_list = [1, 2, 3, 77, 5, 99, 3, 7, 12, 35, 23, 55]
    b_list = merge_sort(a_list)
    print(a_list)
    print(b_list)
