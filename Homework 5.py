# Задание 1
# Создать программный файл в текстовом формате, записать в него построчно 
# данные, вводимые пользователем. Об окончании ввода данных будет 
# свидетельствовать пустая строка


a = open("test.txt", "w")
while True:
    c = input("Введите любой текст: ")
    if c == '': 
        break
    a.write(c + '\n')
a.close()

# Задание 2 
# Создать текстовый файл (не программно), сохранить в нём 
# несколько строк, выполнить подсчёт строк и слов в каждой строке.

import os

path = 'C:/repo'
os.chdir(path)

count = 0
with open("Text1.txt") as file:
    for line in file:
        count += 1
        b = len(line)
        print(f"В строке №{count} {b} символа")
        
print(f"В файле {count} строк")

# Задание 3
# Создать текстовый файл (не программно). Построчно записать фамилии 
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из 
# сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

path = 'C:/repo'
os.chdir(path)

report = []
sum_salaries = 0
with open('Text2.txt', 'r', encoding='UTF-8') as file:
     rows = file.readlines()
     print("Оклады сотрудников")
     for row in rows:
         row_items = row.split()
         report.append([row_items[0], int(row_items[1])])
         print(f"{row_items[0]}: {int(row_items[1])} руб.")
         sum_salaries += int(row_items[1])

print("\nСотрудники с окладом менее 20000 руб.")
[print(worker[0]) for worker in report if worker[1] < 20000]


print(f"\nСредний оклад сотрудников {sum_salaries / len(report):.2f} руб.")

# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно 
# данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

path = 'C:/repo'
os.chdir(path)

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

text_eng = ''
with open('Text3.txt', 'r', encoding='UTF-8') as file_eng:
    text_eng = file_eng.read()

text_rus = text_eng
for en, ru in dictionary.items():
    text_rus = text_rus.replace(en, ru)

with open('Text3_rus.txt', 'w', encoding='UTF-8') as file_rus:
    file_rus.write(text_rus)

# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор 
# чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в 
# файле и выводить её на экран.

import random

with open('Text4.txt', 'w', encoding='UTF-8') as file:
    glue = ''
    for _ in range(6):
        file.write(glue + str(random.randint(1, 10)))
        glue = ' '

with open('Text4.txt', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")

# Задание 6
# Сформировать (не программно) текстовый файл. В нём каждая строка должна 
# описывать учебный предмет и наличие лекционных, практических и лабораторных 
# занятий по предмету. Сюда должно входить и количество занятий. Необязательно, 
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество 
# занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re
import os

path = 'C:/repo'
os.chdir(path)

report = {}
with open('Text5.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        report.update({row_items[0]: sum([int(i) for i in hours])})

print(f"Исходный файл:\n{text}\n")
print(f"Словарь:\n{report}")


# Задание 7
# Создать вручную и заполнить несколькими строками текстовый файл, в 
# котором каждая строка будет содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
# прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их 
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
#                {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import os
import json

path = 'C:/repo'
os.chdir(path)


report = []
with open('Text6.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
            report.append(profits)
            report.append({'average_profit': (profit_sum / len(profits))})

with open('Text6.json.txt', 'w', encoding='UTF-8') as json_file:
    json.dump(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Исходный файл:\n{text}\n")
print(f"Список:\n{report}\n")
print(f"json-объект:\n{json_report}")
