import random
import sorts
import time
import pandas as pd


def check(sorted_list):
    for i in range(len(sorted_list) - 1):
        if not sorted_list[i] <= sorted_list[i + 1]:
            return False
    return True


def time_of_working(func, *args_for_func):
    start_time = time.perf_counter()
    res = func(args_for_func)
    end_time = time.perf_counter()
    return end_time - start_time


def result(method, dict_of_lists):
    results = {}
    list_for_check = [random.randint(-10000, 10000) for _ in range(30)]
    if check(method(list_for_check)):
        for key in dict_of_lists.keys():
            results[key] = time_of_working(method, dict_of_lists[key])
    return results



def table_of_results(dict_of_lists, methods):
    index = list(map(lambda func: func.__name__, methods))
    data = [result(method, dict_of_lists).values() for method in methods]
    columns = dict_of_lists.keys()
    table = pd.DataFrame(data=data, index=index, columns=columns)
    return table


def write_to_file(filename, data, n):
    with open(filename, 'a') as out_file:
        print(f'количество элементов в обрабатываемых последовательностях: {n}', file=out_file)
        print(data, file=out_file)
        print('\n'*4, file=out_file)






if __name__ == "__main__":
    n = int(input('Введите число элементов последовательностей -> '))

    dict_of_lists = {
        'sorted_list': [i for i in range(n)],
        'random_list': [random.randint(-10000, 10000) for _ in range(n)],
        'reverse_sorted_list': [i for i in range(n, -1, -1)]
    }
    methods = [sorts.buble_sort, sorts.search_sort, sorts.insertion_sort, sorts.quick_sort]

    write_to_file('output.txt', table_of_results(dict_of_lists, methods), n)






