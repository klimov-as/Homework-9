first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second == third:
    print('3 числа равны между собой')
elif first == second != third:
    print('2 числа равны между собой')
elif first == third != second:
    print('2 числа равны между собой')
elif second == third != first:
    print('2 числа равны между собой')
else:
    print('0 чисел равны между собой')
