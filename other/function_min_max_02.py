# Фукция нахождения минимального и максимального числа и суммы чисел списка
# Найти минимальное из них, максимальное из них, их сумму и вывести результат на экран
numbers = [] # Создаем пустой список

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(f'Минимальное число: {min(numbers)}')
print(f'Макcимальное число: {max(numbers)}')
print(f'Сумма чисел равна: {sum(numbers)}')
print(numbers)