import re
file_path = "directory.txt"


def show_all_data():
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def add_new_contact(fio, number):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(fio)
        f.write(" ")
        f.write(str(number))


def search_contact(value):
    flag = True
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            lst = line.split(" ")
            if str(value) in line:
                print(*' '.join(lst).split())
                flag = False
    if flag:
        print(f"{value} Запись не найдена")

def delete_contact(value):    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    pattern = re.compile(re.escape(value))
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)

def change_contact(value, chng):
    with open (file_path, "r", encoding="utf-8") as f:
        old_data = f.read()
        new_data = old_data.replace(value, chng)
    with open (file_path, "w", encoding="utf-8") as f:
        f.write(new_data)
    
def main():
    print("Выберите действие:\n1. Показать весь справочник \n"
                             "2. Найти контакт \n"
                             "3. Добавить контакт \n"
                             "4. Удалить контакт \n"
                             "5. Изменить контакт")
    select = int(input())
    if select == 1:
        show_all_data()
    elif select == 2:
        value = str(input("Введите фамилию, имя, отчество или телефон: "))
        search_contact(value)        
    elif select == 3:
        fio = input("Введите ФИО через пробел: ")
        number = input("Введите номер телефона: ")
        add_new_contact(fio, number)
    elif select == 4:
        value = str(input("Введите фамилию, имя отчество или телефон: "))
        delete_contact(value)
    elif select == 5:
        value = str(input("Введите данные которые нужно изменить: "))
        chng = str(input("Введите данные на которые нужно изменить: "))
        change_contact(value, chng)
main()