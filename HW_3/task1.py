# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random
N = int(input("Введите количество элементов: "))
X = int(input("Введите число от 1 до 9: "))
A = []
i = int(0)
res = 0

while i <= N:
    A.append(random.randint(1, 9))
    if A[i] == X:
        res += 1
    # print(A[i])
    i += 1

print(res)
