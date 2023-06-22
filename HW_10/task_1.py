import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
num1 = 0
num2 = 0
data = pd.DataFrame(columns=['whoAmI', 'human', 'robot'])
for i in range(len(lst)):
    if lst[i] == 'human':
        num1 = 1
        num2 = 0
        data.loc[len(data.index )] = [lst[i], num1, num2]
    else:
        num1 = 0
        num2 = 1
        data.loc[len(data.index)] = [lst[i], num1, num2]
print(data)
