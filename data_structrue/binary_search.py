from quick_sort import quick_sort
#  coding:utf-8


def binary_search(alist, item):
    """二分查找,递归版本"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binary_search(alist[mid+1:], item)
        else:
            return binary_search(alist[:mid], item)
    else:
        return False


def binary_search_normal(alist, item):
    n = len(alist)
    first = 0
    last = n - 1
    while first < last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return False


if __name__ == "__main__":
    a_list = [12, 34, 32, 656, 65, 61, 78, 23, 6, 8, 4]
    quick_sort(a_list, 0, len(a_list)-1)
    print(binary_search_normal(a_list, 12))
    print((binary_search_normal(a_list, 8)))
