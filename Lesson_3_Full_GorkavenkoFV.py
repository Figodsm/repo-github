# -*- coding: utf-8 -*-








#Задание 1
#Реализовать функцию, принимающую два числа (позиционные аргументы) и 
#выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
#обработку ситуации деления на ноль.

a = 0
b = 0

'''
Вариант без учета возможности введения нуля
'''

def fill_func_1(a, b):
    a = int(input("Укажите первое любое число: "))
    b = int(input("Укажите второе любое число: "))
    quo = a / b
    return quo

print(quo)

fill_func_1(a, b)

'''
Вариант c учетом возможности введения нуля
'''

def fill_func_1(a, b):
    try:
        a = int(input("Укажите первое любое число: "))
        b = int(input("Укажите второе любое число: "))
    except ValueError:
        return 
    quo = a / b
    return quo

val = quo 
print(val)

fill_func_1(a, b)
        
#Задание 2
#Выполнить функцию, которая принимает несколько параметров, описывающих 
#данные пользователя: имя, фамилия, год рождения, город проживания, email, 
#телефон. Функция должна принимать параметры как именованные аргументы. 
#Осуществить вывод данных о пользователе одной строкой.

val_name = input("Укажите Ваше имя: ")
val_surname = input("Укажите Вашу фамилию: ")
val_birth_year = input("Укажите Ваш год рождения: ")
val_city = input("Укажите город в котром Вы проживаете: ")
val_mail = input("Укажите Вашу электронную почту: ")
val_tel = input("Укажите Ваш телефон: ")


def fill_func_2(val_name, val_surname, val_birth_year, val_city, val_mail, val_tel):
    return val_name, val_surname, val_birth_year, val_city, val_mail, val_tel

print(f"Данные пользователя: имя - {val_name}, фамилия - {val_surname}, год рождения - {val_birth_year}, город проживания - {val_city}, электронная почта - {val_mail}, телефон - {val_tel}")

#Задание 3
#Реализовать функцию my_func(), которая принимает три позиционных аргумента и
#возвращает сумму наибольших двух аргументов.

a = int(input("Укажите первое любое число: "))
b = int(input("Укажите второе любое число: "))
c = int(input("Укажите третье любое число: "))

def fill_func_3(a, b, c):
    fill_list = [a, b, c]
    fill_list.sort(reverse = True)
    fill_sum = fill_list[0] + fill_list[1]
    return fill_sum

result = fill_func_3(a, b, c)
print(result)

#Задание 4
#Программа принимает действительное положительное число x и целое 
#отрицательное число y. Выполните возведение числа x в степень y. Задание 
#реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись 
#без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в 
#степень с помощью оператора **. Второй — более сложная реализация без 
#оператора **, предусматривающая использование цикла.

x = int(input("Укажите действительное положительное число: "))
y = int(input("Укажите целое отрицательное число: "))

def fill_func_4(x, y):
    return x ** y

result_2 = fill_func_4(x, y)
print(result_2)

#Задание 5
#Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
#При нажатии Enter должна выводиться сумма чисел. Пользователь может 
#продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма 
#вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы
#завершается. Если специальный символ введён после нескольких чисел, то 
#вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
#этого завершить программу.

   
user_nums = input("Введите строку чисел, разделенных пробелом: ")
def my_func(user_nums):
    d = 0
    for idx, nums in enumerate(user_nums.split(" ")):
        a = int(nums)
        d = d + a
    return d
res_sum = my_func (user_nums)
print(res_sum)
o_res = 0 + res_sum
while True:
    next_add = input("Для добавления следующих чисел нажмите 'ENTER', для завершения введите '@': ")
    if next_add.lower() in ("ENTER"):
        next_enter = next_add.lower() == "ENTER"
        user_nums = input("Введите следующие числа:")
        sec_res = my_func(user_nums)
        o_res = o_res + sec_res
        print(o_res)
    elif next_add.lower() in ("@"):
        print("Программа завершeна")
        break
    else:
        break
print(f"Ваш итоговый результат: {o_res}")

#Задание 6
#Реализовать функцию int_func(), принимающую слова из маленьких латинских букв 
#и возвращающую их же, но с прописной первой буквой. 
#Например, print(int_func(‘text’)) -> Text. 

text = input('Введите слово с маленькой буквы: ')
    
def fill_func_6(text):
    new_text = text.capitalize()
    return new_text

result_4 = fill_func_6(text)
print(result_4) 

#Задание 7
#Продолжить работу над заданием. В программу должна попадать строка из слов, 
#разделённых пробелом. Каждое слово состоит из латинских букв в нижнем 
#регистре. Нужно сделать вывод исходной строки, но каждое слово должно 
#начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().   

text_long = input('Введите неколько слов с маленькой буквы: ')
    
def fill_func_7(text_long):
    new_text = text_long.title()
    return new_text

result_5 = fill_func_6(text_long)
print(result_5)    
    
    