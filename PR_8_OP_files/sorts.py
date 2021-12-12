import random


def buble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(list1):
    for i in range(1, len(list1)):
        cur_value = list1[i]
        j = i - 1
        while j >= 0 and cur_value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = cur_value
    return list1


def search_sort(lst):
    def lowest_value(lst1):
        low_value = lst1[0]
        for i in range(1, len(lst1)):
            if lst1[i] < low_value:
                low_value = lst1[i]
        return low_value

    def lowest_value_index(lst2, sourse_list=lst):
        low_value = lowest_value(lst2)
        index = sourse_list.index(low_value)
        return index

    for i in range(len(lst) - 1):
        lst.insert(i, lst.pop(lowest_value_index(lst[i:])))
    return lst


def merge_sort(alist, start, end):
    def merge_list(alist, start, mid, end):
        left = alist[start:mid]
        right = alist[mid:end]
        k = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end):
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid:
            while k < end:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < end:
                alist[k] = right[j]
                j = j + 1
                k = k + 1

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = random.choice(lst)
    l_nums = [n for n in lst if n < q]
    e_nums = [q] * lst.count(q)
    b_nums = [n for n in lst if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)







