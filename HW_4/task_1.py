# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


import random
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
i = 0
list_1 = list()
list_2 = list()
set_res = set()
while (i <= n or i <= m):
    if i < n:
        list_1.append(random.randint(1, 9))
    if i < m:
        list_2.append(random.randint(1, 9))
    i += 1
i = 0
if n > m:
    for i in range(n):
        if list_1[i] in list_2:
            set_res.add(list_1[i])
        i += 1
else:
    for i in range(m):
        if list_2[i] in list_1:
            set_res.add(list_2[i])
        i += 1
print(list_1)
print(list_2)
print(sorted(set_res))
