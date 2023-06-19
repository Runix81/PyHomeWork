# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.




import pandas as pd
df = pd.read_csv("sample_data/california_housing_test.csv")
print(f"Средняя стоимость дома с численностью населения меньше 500 человек = {df[df['population']<=500]['median_house_value'].mean()}")
minpop = df['population'].min()
print(f"В зоне с наименьшей численностью населения, максимальное число жильцов в доме = {df[df['population']==minpop]['households'].max()}")
