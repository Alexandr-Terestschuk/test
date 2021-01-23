# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:31:55 2021

@author: Александр Терещук

ДЗ 12. Все пункты сделать как отдельные функции
можно создавать дополнительные вспомагательные функции)
"""
import requests
import json
import re
import csv


# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

def get_quotes(count):
    quote_dict_list = []
    i = 0
    url = "http://api.forismatic.com/api/1.0/"

    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"}
    while i != count:
        params["key"] = i
        r = requests.get(url, params=params)
        quote = r.json()
        quote_dict = {"Author": "", "Quote": "", "URL": ""}
        if len(quote["quoteAuthor"]) > 0:
            quote_dict["Author"] = quote["quoteAuthor"]
            quote_dict["Quote"] = quote["quoteText"]
            quote_dict["URL"] = quote["quoteLink"]
            quote_dict_list.append(quote_dict)
            i += 1
    return quote_dict_list


quotes = get_quotes(10)


def key_sorted_by_name(quote):
    return quote["Author"]


quotes = sorted(quotes, key=key_sorted_by_name)


def write_quotes_csv(filename="quotes.csv"):
    with open(filename, "w", encoding="utf-8") as csv_file:
        fieldnames = {"Author": "", "Quote": "", "URL": ""}
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(quotes)


write_quotes_csv("C:/Users/User/Hillel_new/forismatic.csv")

###################################################################################################################
# # 2. Дан файл authors.txt
# # 2.1) написать функцию, которая считывает данные из этого файла,
# # возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# # Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
def read_txt(filename="authors.txt"):
    with open(filename, "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            if line.find("'s") >= 0 and (line.find("birthday") >= 0 or line.find("death") >= 0):
                data.append(line)
    return data


list_autors = read_txt("C:/Users/User/Hillel_new/authors.txt")


# ###################################################################################################################
#
# # 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# # в формате {"name": name, "date": date},
# # где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# # Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# # {"name": "J. D. Salinger", "date": "01/01/1919"}]

def dict_names(autor):
    old_dict_names = re.findall(r"[A-Z][A-Za-z. ]+[']", autor)
    dict_names = [i.strip(' \'') for i in old_dict_names]
    return dict_names


month_name_map = {
    'January': "01",
    'February': "02",
    'March': "03",
    'April': "04",
    'May': "05",
    'June': "06",
    'July': "07",
    'August': "08",
    'September': "09",
    'October': "10",
    'November': "11",
    'December': "12"
}


def dict_data(autor):
    old_dict_data = re.findall(r"[0-9]\S+ \S+ \S+[0-9]", autor)
    data_list = []
    year = re.findall(r"[0-9]+", autor)[-1]
    day = re.findall(r"[0-9]+", autor)[0]
    month = re.findall(r"[A-Z][a-z]+[ ][1]", autor)
    month_names = ''.join([i.strip(' 1') for i in month])
    month_names = month_name_map[month_names]
    result = (f"{day}/{month_names}/{year}")
    return result


def list_to_dict(list_autors):
    dict_list = []
    for autor in list_autors:
        name = ''.join(dict_names(autor))
        date = dict_data(autor)
        author_dict = {"name": name, "date": date}
        dict_list.append(author_dict)
    return dict_list

print(list_to_dict(list_autors))
# ##################################################################################################################
# # 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def write_json(filename = "list_autors.json"):
    with open(filename, "w") as write_in_json:
        json.dump(list_to_dict(list_autors), write_in_json)

write_json("C:/Users/User/Hillel_new/dict.json")