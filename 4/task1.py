import random

length_of_list = int(input("Ввведіть довжину списка: "))
a = float(input("Ввведіть нижню межу: "))
b = float(input("Введіть верхню межу: "))
print("-"*30)
list1 = []
list2 = []
sum_arr = 0
print("Список: ")
while len(list1) <= length_of_list:
    x = random.randint(1, 3)
    match x:
        case 1:
            value = random.uniform(a, 0)
        case 2:
            value = random.uniform(0, b)
        case 3:
            value = 0
    list1.append(value)
    sum_arr += value
    print(str(value).center(50))
print('cyma: ', sum_arr)
print("-"*30)
if sum_arr > 0:
    print("Сума більше 0")
    for i in list1:
        if i < 0:
            minus = list1.index(i)
            break
    print("Індекс першого від'ємного елементу: ", minus)
    for i in list1:
        if i == 0:
            zero = list1.index(i)
            break
    print("Індекс першого нульового елементу: ", zero)
    if minus < zero:
        for i in range((minus+1), zero):
            print(str(list1[i]).center(50))
    if minus > zero:
        for i in range((zero+1), minus):
            print(str(list1[i]).center(50))
    print("-"*30)


elif sum_arr < 0:
    print("Сума менше 0")
    elem = sum_arr/ len(list1)
    print("Середнє арифметичне", elem)
    for i in range(len(list1)):
        list2.append(elem)
        print(str(list2[i]).center(50))
