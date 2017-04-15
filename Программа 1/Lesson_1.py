# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#   функциями dir и help исследовать модули os, sys, psutil
#   вывести максимум информации о системе (ветка №2):
#   имя текущей директории, платформа (ОС), кодировка файловой системы,
#   логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модули os,sys идут в комплекте с Python'ом.
import os
import sys
import shutil
# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil       


print("\t\tРобот помошник Python")
print("\t\tПривет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

while True:
    answer = input("Давайте поработаем? (Y/N)")
         
    if answer == 'Y' or answer == 'y':
        print("Отлично, друг!")
        print("Я умею:")
        print("\t[1] - выведу список файлов текущей директория")
        print("\t[2] - выведу информацию об операционной системе")
        print("\t[3] - выведу список id процессов")
        print("\t[4] - дублирую файлы в текущей директории")
        
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Вот, что я знаю о системе: ")
            print("\tКоличество процессоров: ", psutil.cpu_count())
            print("\tПлатформа: ", sys.platform)
            print("\tКодировка файловой системы: ", sys.getfilesystemencoding())
            print("\tТекущая директория: ", os.getcwd())
            print("\tТекущий пользователь: ", os.getlogin())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            file_list = os.listdir()
            for i in range(len(file_list)):
                newfile = file_list[i] + '.dupl'
                #копируем
                shutil.copy(file_list[i], newfile)
            
        else:
            print("Введите цифру из списка!")
       
    # Функция type выводит информацию о типе переменной (объекта)
    # Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
    # Функция help выводит встронную справку об объекте
        
    elif answer == 'N' or answer == 'n':    
        print("До свидания!")
        break
    else:
        print("Неизвестный ответ")    
