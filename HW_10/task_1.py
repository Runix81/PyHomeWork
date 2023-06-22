import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
num1 = 0
num2 = 0
data = pd.DataFrame(columns=['whoAmI', 'human', 'robot'])    # Создаем пустой датафрейм с назнаниями колонок
for i in range(len(lst)):
    if lst[i] == 'human':                                    # Если значения списка равно human, то 
        num1 = 1                                             #  num1 = 1
        num2 = 0                                             #  num2 = 0
        data.loc[len(data.index )] = [lst[i], num1, num2]    # Добавляем значения в датафрейм при каждой итерации цикла
    else:                                                    # Иначе
        num1 = 0                                             #  num1 = 0
        num2 = 1                                             #  num2 = 1
        data.loc[len(data.index)] = [lst[i], num1, num2]     # Добавляем значения в датафрейм при каждой итерации цикла
print(data)                                                  # Выводим на экран все строки датафрейма
