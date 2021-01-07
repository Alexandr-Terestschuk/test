# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:58:08 2021

@author: Александр Терещук.

ДЗ 8. Функции, чтение файлов.
"""

# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список 
# (названия сохранить без точки).

with open("C:/Users/User/Hillel_new/domains.txt", "r") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())

data = str(data)

for symbol in data:
    if symbol == ".":
        data = data.replace(symbol, '')

print(data)

###############################################################################


# 2. Считать данные из файла names.txt и поместить в список только фамилии 
# из файла. Каждая строка файла содержит номер, фамилию, страну, некоторое 
# число (таблица взята с википедии). Фамилия находится всегда на одной и той же 
# позиции в строке.


import pandas as pd 


col_list = ["Number", "Name", "Language", "Sum"]
df = pd.read_csv('C:/Users/User/Hillel_new/names.txt', usecols=col_list, sep=' ')
result = list(df["Name"])
print(type(result), result)

###############################################################################


# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в 
# функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как 
# буквы не смогут повторяться)

# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)

# >>>miller.249@sgdyyur.com



from random import randint
import io
import chardet
import os
import codecs
import random
from re import match
 
with open("C:/Users/User/Hillel_new/domains.txt", "r") as name:
    text = name.read()
    domen_name = text.replace(".", "")
 
with open('C:/Users/User/Hillel_new/names.txt', "r") as name1:
    surnames = '\n'.join([line.split()[1] for line in name1.readlines()])
 
random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))
 
emeil = surnames + "." + str(random_number) + "@" + str(random_word) + "." + domen_name
print(emeil)


