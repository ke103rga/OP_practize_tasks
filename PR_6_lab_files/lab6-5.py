import datetime

import eks_module
import os

with open('input.txt', 'r') as file:
    a, b = map(int, file.readline().strip().split())
    filename = file.readline().strip()
eks_module.print_rectanlge(a, b, filename)
with open('output.txt', 'r') as file:
    print(f'Содержимое файла {filename}:')
    print(file.read())

with open('input1.txt', 'r') as file:
    a = int(file.readline().strip())
    filename = file.readline().strip()
eks_module.print_square(a, filename)
with open(filename, 'r') as file:
    print(f'Содержимое файла {filename}:')
    print(file.read())

# --------------------------------------------------------------------------------------------------------------------------------------------- #


files = os.listdir(os.getcwd()) # получение списка объектов в текущей директории
if eks_module.existance_of_file(files):
    with open('input.txt', 'r') as file:
        number = file.readline().strip().split()[0]
        out_file = 'output.txt' # название файла, в который будет записана информация
        eks_module.inform_about_num(number, out_file)
else:
    print('Файл с входными данными не обнаружен')

# --------------------------------------------------------------------------------------------------------------------------------------------------- #
files = os.listdir(os.getcwd())
if eks_module.existance_of_file(files):
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
    with open('output.txt', 'w') as out_file:
        out_file.write(' '.join(eks_module.prime_numbers(n)))
else:
    print('Файл с входными данными не обнаружен')

 # -=----------------------------------------------------------------------------------------------------------------------------------------#
with open('output.txt', 'w') as f:
    start_time = datetime.time()
    f.write(str(datetime.datetime.now()))

    file = open('input.txt', 'r')
    total = 0
    rad = int(file.readline().strip())
    x0, y0 = map(int, file.readline().strip().split())
    for x in range(x0 - rad, x0 + rad + 1):
        for y in range(y0 - rad, y0 + rad + 1):
            if eks_module.inside_circle(x, y, x0, y0, rad):
                 total += 1
    f.write(str(total))
    f.write(datetime.time() - start_time)
    file.close()

# ------------------------------------------------------------------------------------------------------#


