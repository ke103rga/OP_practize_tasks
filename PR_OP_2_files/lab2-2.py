# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = 9.0
int_number = 9
str_number = '9'

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
print(type(float_number))
print(type(int_number))
print(type(str_number))


# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
float_number = int(float_number)
int_number = float(int_number)
float_number = str(float_number)