
a, b, c = int(input()), int(input()), int(input())
if a > 0 and b > 0 and c > 0:
    if max(a, b, c) < sum([a, b, c]) - max(a, b, c):
        if a == b and a == c:
            print('Треугольник равносторонний')
        elif a == b or a == c or b == c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник общего вида')
    else:
        print('Треугольник не существует')
else:
    print('Треугольник не существует')

#--------------------------------------------------------------------------------------------#
def D(a, b, c):
    return b**2 - 4 * a * c
def float_out(x):
    return '{0:.5f}'.format(float(x))
def answers(a, b, c):
    d = D(a, b, c)
    return [float_out((-b + d**0.5) / (2*a)), float_out((-b - d**0.5) / (2*a))]
def outpur(a, b, c):
    d = D(a, b, c)
    print('Уравнение:')
    print(f'({float_out(a)})*X^2 + ({float_out(b)})*X + ({float_out(c)}) = 0')
    if d > 0:
        print('Количество корней: 2')
        print(*answers(a, b, c), sep = '\n')
    elif d == 0:
        print('Количество корней: 1')
        print(*answers(a, b, c), sep='\n')
    else:
        print('Количество корней: 0')

a, b, c = float(input()), float(input()), float(input())
outpur(a, b, c)

#--------------------------------------------------------------------------------------------#

def quantity_of_days(hp):
    return f'{hp // 24} days'
def time_of_arrival(hotp, motp, hp, mp):
    return f'{(hotp + hp) % 24 + (motp + mp) // 60} hours : {(motp + mp) % 60} minutes'
hotp, motp = int(input()), int(input())
hp, mp = int(input()), int(input())
print(time_of_arrival(hotp, motp, hp, mp))
print(quantity_of_days(hp))


#-------------------------------------------------------------------------------------------#

def correct_writing_rubles(quantity_of_rubles):
    if quantity_of_rubles in [i for i in range(11, 21)]:
        return f'{quantity_of_rubles} рублей'
    elif quantity_of_rubles % 10 == 1:
        return f'{quantity_of_rubles} рубль'
    elif quantity_of_rubles % 10 >= 2 and quantity_of_rubles % 10 <= 4:
        return f'{quantity_of_rubles} рубля'
    else:
        return f'{quantity_of_rubles} рублей'
def correct_writing_cops(quantity_of_kops):
    if quantity_of_kops in [i for i in range(11, 21)]:
        return f'{quantity_of_kops} копеек'
    elif quantity_of_kops % 10 == 1:
        return f'{quantity_of_kops} копейка'
    elif quantity_of_kops % 10 > 1 and quantity_of_kops % 10 <= 4:
        return f'{quantity_of_kops} копейки'
    else:
        return f'{quantity_of_kops} копеек'
kop = int(input())
quantity_of_rubles = kop // 100
quantity_of_kops = kop % 100
if quantity_of_rubles != 0:
    print(correct_writing_rubles(quantity_of_rubles))
if quantity_of_kops != 0:
    print(correct_writing_cops(quantity_of_kops))