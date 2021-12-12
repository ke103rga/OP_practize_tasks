import random
import sorts
import time
import pandas as pd


def check(sorted_list):
    """
    :param sorted_list: list of numbers
    :return: bool
    """
    for i in range(len(sorted_list) - 1):
        if not sorted_list[i] <= sorted_list[i + 1]:
            return False
    return True


def time_of_working(func, *args_for_func):
    """
    :param func: function whose working time you want to know
    :param args_for_func: arguments for function
    :return: float time in seconds
    """
    start_time = time.perf_counter()
    res = func(args_for_func)
    end_time = time.perf_counter()
    return end_time - start_time


def result(method, types_of_list):
    """
    :param method: method of sorting
    :param types_of_list: pandas.Series object with different types of lists
    :return: dict where keys are types of lists and values are time of working for this method
    """
    results = {}
    list_for_check = [random.randint(-10000, 10000) for _ in range(30)]
    if check(method(list_for_check)):
        for index in types_of_list.index:
            results[index] = time_of_working(method, types_of_list[index])
    return results



def table_of_results(types_of_list, methods):
    """
    :param types_of_list: pandas.Series object with different types of lists
    :param methods: list of different methods for sorting
    :return: pandas.DataFrame object where index are names of methods and columns are types of lists
    """
    my_index = list(map(lambda func: func.__name__, methods))
    my_data = [result(method, types_of_list).values() for method in methods]
    my_columns = types_of_list.index
    table = pd.DataFrame(data=my_data, index=my_index, columns=my_columns)
    return table


def write_to_file(filename, mode, data, n):
    """
    :param filename: name of file, where you want to save information
    :param mode: 'a' if you want to add some information and 'w' if you want to work with empty file
    :param data: information wich you want to save
    :param n: quantity of elements of lists
    :return: None
    """

    with open(filename, mode) as out_file:
        print(f'количество элементов в обрабатываемых последовательностях: {n}', file=out_file)
        print(data, file=out_file)
        print('\n'*4, file=out_file)






if __name__ == "__main__":
    n = int(input('Введите число элементов последовательностей -> '))

    my_index = ['sorted_list', 'random_list', 'reverse_sorted_list']
    my_data = [[i for i in range(n)], [random.randint(-10000, 10000) for _ in range(n)], [i for i in range(n - 1, -1, -1)]]
    types_of_list = pd.Series(index=my_index, data=my_data)

    methods = [sorts.buble_sort, sorts.search_sort, sorts.insertion_sort, sorts.quick_sort]

    write_to_file('output.txt', 'w', table_of_results(types_of_list, methods), n)












