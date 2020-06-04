def bubble_sort(alist):
    for j in range(len(alist)-1):
        count = 0
        for i in range(len(alist)-j-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count = count+1
            if count == 0:
                break


if __name__ == "__main__":
    a_list = [1, 2, 1, 2, 1, 2]
    bubble_sort(a_list)
    print(a_list)
