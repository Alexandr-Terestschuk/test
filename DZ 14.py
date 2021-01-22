# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:20:26 2021

@author: Александр Терещук

Lesson 14. ООП. Область видимости атрибутов и методов класса. 
Наследование классов.
"""

# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.


class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 1
        self.agility = 1
        self.intellect = 1
 
    def therapy(self):
        if self.health < 100:
            self.health += 10
            
   
class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan)
        self.air = air  
        self.fire = fire
        self.water = water
 
    def augment(self):
        if self.intellect < 10:
            self.intellect += 1
 
class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan)
        self.bow = bow
        self.crossbow = crossbow
 
    def augment(self):
        if self.agility< 10:
            self.agility += 1
 
 
class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(self, name )
        self.sword = sword
        self.axe = axe
        self.pike = pike
 
    def augment(self):
        if self.power < 10:
            self.power += 1