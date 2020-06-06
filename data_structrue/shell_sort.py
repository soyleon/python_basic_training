"""
希尔排序
"""


def shell_sort(alist):
    n = len(alist)
    gap_len = n // 2

    while gap_len > 0:
        for j in range(gap_len, n):
            for k in range(j, gap_len, -gap_len):
                if alist[k] < alist[k-gap_len]:
                    alist[k], alist[k-gap_len] = alist[k-gap_len], alist[k]
                else:
                    break
        gap_len = gap_len//2


if __name__ == "__main__":
    a_list = [1, 2, 3, 77, 5, 99, 3, 7, 11]
    shell_sort(a_list)
    print(a_list)
