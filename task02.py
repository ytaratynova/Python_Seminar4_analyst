# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))

multipliers = []

for i in range(2, number):

    while number % i == 0:
        multipliers.append(i)
        number /= i

if number != 1:
    multipliers.append(int(number))    

print(f'Разложение на простые множители: {multipliers}')
