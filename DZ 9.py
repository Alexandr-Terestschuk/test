# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:55:40 2021

@author: Александр Терещук
ДЗ 9. Форматы файлов json, csv.
"""

# Цель задания - создать функции, которые будут генерировать 
# случайные данные нужного формата для записи в файлы разных типов.

# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 
# но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского 
# алфавита, цифры, пробелы, знаки препинания, символ перехода 
# на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, 
# а стоять отдельно.
# Знаки препинания всегда идут в конце слова.

import random


def create_text_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def create_number_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('0'), ord('9'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def split_text_line(txt_line):
    space_count = len(txt_line) // 10
    space_index_list = []
    while len(space_index_list) < space_count:
        index = random.randint(1, len(txt_line) - 2)
        if (index not in space_index_list and
                index - 1 not in space_index_list and
                index + 1 not in space_index_list):
            space_index_list.append(index)
    for index in space_index_list:
        txt_line = txt_line[:index] + " " + txt_line[index + 1:]
    return txt_line


def replace_text_to_number(word):
    if len(word) > 5:
        return word
    else:
        return create_number_line(len(word), len(word))


def replace_first_letter(word):
    return word.replace(word[0], word[0].upper(), 1)


def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)


def create_randome_txt_data(min_len=100, max_len=1000):
    txt_line = create_text_line(min_len, max_len)
    txt_line = split_text_line(txt_line)
    new_words = []
    for word in txt_line.split():
        case = random.randint(1, 100)
        if not case % 10:
            new_word = replace_text_to_number(word)
        elif not case % 2:
            new_word = replace_first_letter(word)
        elif not case % 5:
            new_word = replace_last_letter(word)
        else:
            new_word = word
        new_words.append(new_word)
    # word = txt_line.split()[0]
    # print(word, replace_last_letter(word))
    return " ".join(new_words)


number =150

if __name__ == "__main__":
    txt_data = create_randome_txt_data()
    print(txt_data)

##############################################################################


# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не
# более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв 
# английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в 
# диапазоне от 0 до 1, или True/False. Выбор значения должен быть равновероятным. 
# Т.е. вероятность того, что значение будет целым такая же, как и вероятность того, 
# что будет типа float или типа bool.

import pprint
import random
import string


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    return random.choice([
        lambda: random.randint(-100, 100),
        lambda: random.uniform(0, 1),
        lambda: random.choice([False, True])
    ])();
    

def random_dict():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}


pprint.pprint(random_dict())

##############################################################################

# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m 
# (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

import csv

def create_random_table_csv(filename):
    with open(filename, "w") as create_in_csv:
        writer = csv.writer(create_in_csv)
        x = random.randint(3, 10)
        for i in range(random.randint(3, 10)):
            writer.writerow(random.randint(0, 1) for row in range(x))

create_random_table_csv("C:/Users/User/Hillel_new/table.txt")



##############################################################################

# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - 
# полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для 
# записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"


import json
import csv
 
 
def generate_and_write_file(name):
    with open(name, "w+") as f:
        if (".json" in name):
            text = ("This text for \"JSON\" file.")
            json.dump(text, f)
            f.close()
 
        elif (".csv" in name):
            text = [
                ["Notebooks", 60],
                ["Pens", 25],
                ["Pencils", 30]
            ]
 
            writer = csv.writer(f)
            writer.writerows(text)
            f.close()
            
        elif (".txt" in name):
            f.write("This text for \"TXT\" file.")
            f.close()
        else:
            print("Unsupported file format")

generate_and_write_file("C:/Users/User/Hillel_new/format.txt")





