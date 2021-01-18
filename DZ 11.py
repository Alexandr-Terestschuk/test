# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:27:31 2021

@author:  Александр Терещук
ДЗ 11, data.json - файл с данными о некоторых математиках прошлого.
"""

# 1. Необходимо написать функцию, которая считает эти данные из файла. 
# Параметр функции - имя файла.

import json

def open_json_data(filename="data.json", encoding="utf-8"):
    with open(filename, "r", encoding=encoding) as json_file:
        result = json.load(json_file)
    return result

print(open_json_data("C:/Users/User/Hillel_new/data.json"))

##############################################################################

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" 
# (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat
# - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_surname(data):

        sort_surname = sorted(dicts, key = lambda item: item['name'])
        return (sort_surname)

dicts = [
    {"name": "Archimedes",
      "years": "c. 287 BC – 212 BC."},
    {"name": "Daniel Bernoulli",
      "years": "1700 – 1782."},
    {"name": "Brahmagupta",
      "years": "597 – 668.",},
    {"name": "Rene Descartes",
      "years": "1596 – 1650."},
    {"name": "Euclid",
      "years": "c. 325 – c. 270 BC."}
]
    
print(sort_by_surname(dicts))
    
##############################################################################

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def key(dict_):
    year = dict_["years"].split("–")[1]
    if len(year.split()) == 1:
        return int(year.split()[0][:-1])
    return -int(year.split(" ")[-2])


list_ = [{"name": "Archimedes",
      "years": "c. 287 BC – 212 BC."},
    {"name": "Daniel Bernoulli",
      "years": "1700 – 1782."},
    {"name": "Brahmagupta",
      "years": "597 – 668.",},
    {"name": "Rene Descartes",
      "years": "1596 – 1650."},
    {"name": "Euclid",
      "years": "c. 325 – c. 270 BC."}]

list_.sort(key = key)

print(*list_, sep = "\n") 

##############################################################################

# 4. Написать функцию сортировки по количеству слов в поле "text".

# word count using python dictionary

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print( word_count("Discovered a general method to find the sum of any integral power and hence the volume of a paraboloid; solved ‘Alhazen’s problem’ concerning the reflection of light from curved surfaces.\
                  Founded the sciences of mechanics and hydrostatics, calculated pi precisely, devised the law of exponents, created new geometrical proofs, invented numerous ingenious mechanical devices and more.\
                      Discovered the Bernoulli Effect explaining how aircraft wings generate lift; formulated a kinetic theory relating particle speeds in gases to temperature; made major discoveries in the theory of risk.\
                          Published more mathematics than any other single mathematician, much of it groundbreaking. An astonishing fraction of the total research work in mathematics and the physical sciences between 1730 and 1780 was carried out solely by Euler.\
                              Co-founded the disciplines of analytic geometry and probability theory and was a key player in the invention of calculus. There’s more to Fermat than his famous last theorem.\
                                  Established zero as a number and defined its mathematical properties; discovered the formula for solving quadratic equations.\
                                      One of the greatest philosophers of all time; advocate of skepticism in the scientific method; creator of new mathematical ideas including the independent founding of analytical geometry. Cartesian coordinates are named in his honor.\
                                          Authored the Elements, the most famous and most published mathematical work in history; another great work, Optics, explained light’s behavior using geometrical principles – the basis of artistic perspective, astronomical methods, and navigation methods for more than two thousand years.\
                                              The rebirth of Western mathematics: Fibonacci’s Book of Calculation introduced the Indian number system, now used worldwide, to Europe."))



