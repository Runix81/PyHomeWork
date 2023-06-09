# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list_len = int(input("Введите длину массива: "))
list_1 = list()
for i in range(list_len):
    list_1.append(random.randint(-20, 20))
min_number = int(input("Введите минимальное значение: "))
max_number = int(input("Введите максимальное значение: "))
print (*list_1)
for i in range(list_len):
    if min_number <= list_1[i] <= max_number:
        print(i)

