# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


poem = str(input("Введите текст стихотворения Винни: "))
poem = poem.lower()
list_1 = ["а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"]
list_2 = ["a", "e", "i", "o", "u", "y"]
poem = poem.split(' ')
print(poem)
count_1 = 0
count = list()
for i in range(len(poem)):
    word = poem[i]
    # print(word)
    for j in range(len(word)):
        if word[j] in (list_1 or list_2):
            count_1 += 1
    count.append(count_1)
    count_1 = 0
    # print(count)
res = True
for i in range(len(count)-1):
    if count[i] != count[i+1]:
        res = False
        break
    else:
        res = True
if res:
    print("Парам пам-пам")
else:
    print("Пам парам")
