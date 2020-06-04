def selection_sort(alist):
    n = len(alist)
    for j in range(n-1):
        max_index = 0
        for i in range(n-j):
            if alist[i] >= alist[max_index]:
                max_index = i
        alist[n-j-1], alist[max_index] = alist[max_index], alist[n-j-1]


if __name__ == "__main__":
    a_list = [1, 2, 3, 77, 5, 99, 3, 7]
    selection_sort(a_list)
    print(a_list)
