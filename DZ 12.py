# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:31:55 2021

@author: Александр Терещук

ДЗ 12. Все пункты сделать как отдельные функции
можно создавать дополнительные вспомагательные функции)
"""

# 1. Написать функцию, которая принимает в виде параметра целое число - 
# количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в 
# csv файл (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests

url = "http://api.forismatic.com/api/1.0/"

params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
for i in range(1):
    params["key"] = i
    r = requests.get(url, params=params)
    quote = r.json()
    # print(quote)
    quote_text = quote["quoteText"]
    print(quote_text)
    quote_author = quote["quoteAuthor"]
    print(quote_author)
    
import csv
  
def generate_and_write_file(name):
    with open(name, "w+") as f:
        
        if quote_author == '':

            text = "No author"
            writer = csv.writer(f)
            writer.writerows(text)
            f.close()
                
            
        elif 'quoteAuthor' in quote:
            text = quote_author + quote_text + url
            writer = csv.writer(f)
            writer.writerows(text)
            f.close()

generate_and_write_file("C:/Users/User/Hillel_new/forismatic.csv")

###############################################################################

# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание 
# на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, 
# и возвращает список словарей в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, 
# m-месяц, y-год)

# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]

# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

with open("C:/Users/User/Hillel_new/authors.txt", "r") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())
        
# lists

matches = [match for match in data if "birthday" in match]
matches_2 = [match for match in data if "death" in match]
matches_3 = [match for match in data if "author" in match]


print("Lines with birthday:")
print(matches)

print("Lines with death:")
print(matches_2)

print("Lines with author:")
print(matches_3)


# dictionaries

birthday_dictionary = dict.fromkeys(matches, "birthday")

print("Lines with birthday dict:")
print(birthday_dictionary)


death_dictionary = dict.fromkeys(matches_2, "death")

print("Lines with death dict:")
print(death_dictionary)


author_dictionary = dict.fromkeys(matches_3, "author")

print("Lines with author dict:")
print(author_dictionary)


# write a dict in a json file


import json

def write_file_json(name):
    with open(name, "w+") as f:
        if (".json" in name):
            text = birthday_dictionary 
            text_1 = death_dictionary
            text_2 = author_dictionary
            json.dump(text, f)
            json.dump(text_1, f)
            json.dump(text_2, f)
            f.close()


write_file_json("C:/Users/User/Hillel_new/dict.json")

