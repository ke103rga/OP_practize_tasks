"""I didn't realize which variant am I,
   so I decided to do more than 2 tasks"""


''' Task № 1'''

def P(n, m):
    if n == 0:
        return 1
    elif n == 1:
        return m
    elif n >= 2:
        return ((2*n - 1) * m * P(n - 1, m) - (n - 1) * P(n - 2, m)) / n

def values_of_polinom():
    n = int(input('Введите коэффициент n  -> '))
    x = float(input('Введите x  -> '))
    for i in range(n + 1):
        print(P(i, x), end=' ')



# ----------------------------------------------------------------------#

''' Task № 2'''

def div(a, b):
    if a < b:
        return 0
    else:
        return div(a - b, b) + 1

def result_of_div(filename):
    a = int(input('Ведите первое число  -> '))
    b = int(input('Ведите второе число  -> '))
    with open(filename, 'w') as out_file:
        print(f'div({a}, {b}) = {div(a, b)}', file=out_file)


# ----------------------------------------------------------------------#

'''Task № 3'''

def nod_by_divizion(a, b):
    """Даже если одним из аргуменвтов будет предан ноль - функция сработает корректно,
    т.к. ноль делится на любое число и НОД будет равняться второму переданному аргументу."""
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return nod_by_divizion(max(a, b) % min(a, b), min(a, b))

def nod_by_sub(a, b):
    if a == b:
        return a
    else:
        return nod_by_sub(max(a, b) - min(a, b), min(a, a))

def result_of_nod(method = nod_by_divizion):
    a, b = int(input('Введите первое число  -> ')), int(input('Введите второе число  -> '))
    print(f'НОД({a}, {b}) = {method(a, b)}')


# ----------------------------------------------------------------------#

''' Task № 4'''


def bin_k(n, m):
    if m == 0 or m == n:
        return 1
    else:
        return bin_k(n - 1, m) + bin_k(n - 1, m - 1)


def print_bin_value():
    n = int(input('Введите коэффициент n  -> '))
    m = int(input('Введите коэффициент m  -> '))
    print(bin_k(n, m))


# ----------------------------------------------------------------------#

''' Task № 6 and 7, differences only in function "f"'''
f = lambda x: x ** 2 - 3


def find_root(a, b, eps, func):
    if func(a) * func(b) > 0:
        return 'There are no roots in this segment'
    else:
        midpoint = (a + b) / 2
        if (b - a) / 2 < eps or func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            return find_root(a, midpoint, eps, func)
        else:
            return find_root(midpoint, b, eps, func)


def count_root():
    print('Введите границы отрезка:')
    a, b = float(input('а = ')), float(input('b = '))
    eps = float(input('Введите значение допустимой погрешности: '))
    print(f'Корень уравнения x = {round(find_root(a, b, eps, f), len(str(eps)[str(eps).index("."): -1]))}')





