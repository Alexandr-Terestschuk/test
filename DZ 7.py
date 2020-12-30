# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:38:56 2020

@author: Александр Терещук
"""

# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random

random_list = []
# Set a length of the list to 20
for value in range(0, 20):
    # any random numbers from 1 to 100
    random_list.append(random.randint(1, 100))

print("Printing list of 20 random numbers")
print(random_list)

########################################################################

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с 
# помощью модуля random в диапазоне от -10 до 10 по каждой оси.


triangle = {"A": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            "B": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            "C": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10))
            }

print(triangle)

##########################################################################

# 3) Создать функцию my_print, которая принимает в виде параметра строку и 
# печатает ее с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***


def my_print():
    my_str = "I'm the string"
    asterisk = "*"
    
    return asterisk * 3 + my_str + asterisk * 3

print(my_print())

##########################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, 
# ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - 
# напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - 
# напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.


from collections import defaultdict

persons = [
    {"name": "John", "age": 15},
    {"name": "Johannes", "age": 20},
    {"name": "Jack", "age": 45},
    {"name": "Bob", "age": 80}
]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for symbol in persons:
    name = symbol['name']
    age = symbol['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('max_len_name:', *len_name_by_names[max_len_name])

print('average:', sum(ages) // len(ages))

##############################################################################

#5) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = {"January": 1, "February": 2, "March": 3}
my_dict_2 = {"March": 3, "April": 4, "May": 5}


# а) Создать список из ключей, которые есть в обоих словарях.

my_list = list(my_dict_1.keys()) + list(my_dict_2.keys()) 
print(my_list)
      

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

my_list_2 = []
for key in my_dict_1.keys():
    if key not in my_dict_2.keys():
        my_list_2.append(key)
print(my_list_2)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, 
# которые есть в первом, но нет во втором словаре.

my_dict_3 = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        my_dict_3[key] = value
print(my_dict_3)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: 
# [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_4 = {**my_dict_1, **my_dict_2}
for key, value in my_dict_1.items():
    if key == 'March':
        my_dict_4[key] = [value, value]

print(my_dict_4)






