# coding: utf-8
# Подключение модуля производится командой import.
# Модули os,sys идут в комплекте с Python'ом.
# Функция type выводит информацию о типе переменной (объекта)
# Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
# Функция help выводит встронную справку об объекте
#---------------------------------------------------
'''Суровый встроенный отладчик
В командной строку прописать:
python -m pdb [имя файла.py]

help - список команд
b [имя функции] - брейкпоинт для отладки

continue - запуск программы

а - fhuevtyns ntreotq aeyrwbb

l - текущая позиция в коде программы

n - строка кода без захода в функци.

s - с заходом в функцию'''
#---------------------------------------------------
import os, sys, shutil
# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil
#----------------------------------------------------------------------------------------------
#Функция приветствия
def choice():
    print("Отлично, друг!")
    print("Я умею:")
    print("\t[1] - выведу список файлов текущей директория")
    print("\t[2] - выведу информацию об операционной системе")
    print("\t[3] - выведу список id процессов")
    print("\t[4] - дублирую файлы в текущей директории")
    print("\t[5] - дублирую указанный файл")
    print("\t[6] - удаляю дибликаты")
    print("\t[7] - сыграем в руссую рулетку")
    do = int(input("Укажите номер действия: "))
    return do
#Функция проверки выполнения операции дублирования
def duplikate_file(file_name):
    #Проверка является ли элемент файлом
    if os.path.isfile(file_name):
        newfile = file_name + '.dupl'
        #копируем
        shutil.copy(file_name, newfile)
        #Проверяем
        if os.path.exists(newfile):
            print("Файл ",newfile," создан")
            return True
        else:
            print("Возникли проблемы коирования.")
            return False
#Функция вывода информации о системе
def sys_info():
    print("Вот, что я знаю о системе: ")
    print("\tКоличество процессоров: ", psutil.cpu_count())
    print("\tПлатформа: ", sys.platform)
    print("\tКодировка файловой системы: ", sys.getfilesystemencoding())
    print("\tТекущая директория: ", os.getcwd())
    print("\tТекущий пользователь: ", os.getlogin())
#Функция удалениябуликатов
def delete(dirname):
    i = 0
    file_list = os.listdir(dirname)
    for f in file_list:
        # join формирует имя файла в зависимости от операционной системы / \
        file_name = os.path.join(dirname,f)
        # проверка на окончение файла
        if file_name.endswith('.dupl'):
            os.remove(file_name)#Удалить
            #Проверка на удаление
            if not os.path.exists(file_name):
                print("Файл ",file_name," удалён")
                i += 1
            else:
                print("Проблема удаления")
        return i
                
#----------------------------------------------------------------------------------------------
def main():
    print("\t\tРобот помошник Python")
    print("\t\tПривет, программист!")
    name = input("Ваше имя: ")

    print(name, ", добро пожаловать в мир Python!")

    while True:
        answer = input("Давайте поработаем? (Y/N) ")
             
        if answer == 'Y' or answer == 'y':
            
            do = choice()
            
            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                file_list = os.listdir()
                for f in file_list:
                    duplikate_file(f) 
            elif do == 5:
                file_name = input("Введите имя файла и относительный путь до него (. - текущая): ")
                duplikate_file(file_name)          
            elif do == 6:
                dirname = input("Укажите относительную директорию (. - текущая): ")# . текущая
                samm = delete(dirname)
                print("Файлов удалено - ", samm)
            else:
                print("Введите цифру из списка!")
            
        elif answer == 'N' or answer == 'n':    
            print("До свидания!")
            break
        else:
            print("Неизвестный ответ")
            
#Проверка запускается ли именно эта программа
if __name__ == '__main__':
    main()
