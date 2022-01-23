# Exercise 1
#a = 5
#b = 7
#print(a + b)
#print(a + 5)
#c = int(input("Введите любое целое число: "))
#print(c - 1)
#d = input("Введите свое имя: ")
#print("Привет, ", d)

# Exercise 2
#t = int(input("Введите время в секундах: "))
#t_hour = t // 3600
#t_min = t % 3600 // 60
#t_sec = t % 3600 % 60
#print(f"Сейчас (в формате чч:мм:сс): {t_hour}:{t_min}:{t_sec}")

# Exercise 3
#i = int(input("Введите любое целое число: "))
#print(i + i * 11 + i * 111)

#Exercise 4
#i = int(input("Введите целое положительное число, но не более 999: "))
#while i < 10:
#    print("Самое большое число: ", i)
#    break
#while i >= 10 and i < 99:
#    n_1 = i // 10
#    n_2 = i % 10
#    if n_1 > n_2:
#        print("Самое большое число: ", n_1)
#    else:
#        print("Самое большое число: ", n_2)
#    break
#while i >= 100 and i < 999:
#    n_1 = i // 100
#    n_2 = i % 100 // 10
#    n_3 = i % 100 % 10
#    if n_1 > n_2 and n_1 > n_3:
#        print("Самое большое число: ", n_1)
#    else:
#        if n_2 > n_1 and n_2 > n_3:
#            print("Самое большое число: ", n_2)
#        else:
#            print("Самое большое число: ", n_3)
#    break
#print("Готово") 

#Exercise 5 and 6
#income = int(input("Пожалуйста, укажите выручку Вашей компании: "))
#costs = int(input("Пожалуйста, укажите издержки Вашей компании: "))
#if income > costs:
#   print("Ваша компания получает прибыль")
#    profit = (income - costs)/income
#    employee = int(input("Пожалуйста, укажите число сотрудников Вашей компании: "))
#    income_per_employee = income / employee
#    print(f"'Рентабельность Вашей компании': {profit}, 'Прибыль на 1 сотрудника': {income_per_employee}")
#else:
#        if income < costs:
#           print("Ваша компания терпит убытки") 
#        else:
#          print("Ваша компания достигла точки безубыточности")


#Exercise 7
result = int(input("Пожалуйста, укажите результат спортсмена в первый день, км: "))
threshold = int(input("Пожалуйста, какое расстояние спортсмен должен пробежать, чтобы программа рассчитала на какой день тренировок спортсмен достигнет этого результата: "))
day = 1
while result < threshold:
    day = day + 1
    result = result * 1.1
print(f"'На {day} день спортсмен достиг результата — не менее {threshold} км")

    


