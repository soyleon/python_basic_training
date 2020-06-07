"""
快速排序
"""


def quick_sort(alist, start, end):
    if start >= end:
        return

    low = start
    high = end

    mid = alist[start]

    while low < high:
        while low < high and alist[high] > mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)


if __name__ == "__main__":
    a_list = [1, 2, 3, 77, 5, 99, 3, 7, 12, 35, 23, 55]
    quick_sort(a_list, 0, len(a_list)-1)
    print(a_list)