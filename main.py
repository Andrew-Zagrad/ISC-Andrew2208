"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файлі,
показує на екрані первинні дані
"""
import os
from process_data import create_zajavka
from data_service import show_kyrs, show_dovidnik, get_kyrs, get_dovidnik

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~~~~~~~~~~~~~~

1 - вивід аналізу рівня зміни курсу на екран
2 - запис аналізу в файл
3 - вивід курсу обміну 
4 - вивід довідника ринків
0 - завершити роботу
---------------------------------
"""

TITLE = 'АНАЛІЗ РІВНЯ ЗМІНИ КУРСУ ОБМІНУ ВАЛЮТ ДЛЯ ПРИВАТНИХ ОСІБ В БАНКАХ М.КИЄВА'

HEADER = \
"""
=========================================================================================================================
|  Код банку  |  Назва банку  |  Рік  |               Долари США               |                Марки ФРН               |
|             |               |       |========================================|========================================|
|             |               |       |Зміни на 1.11|Зміни на 1.12|Курс на 1.12|Зміни на 1.11|Зміни на 1.12|Курс на 1.12|
=========================================================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

FOOTER = \
"""
=========================================================================================================================

"""
def show_zajavka(zajavka_list):
    """вивод на екран розрахункової таблиці

    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n\n{TITLE:^86}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['cod']:^16}", 
              f"{zajavka['name']:14}",
              f"{zajavka['year']:10}",
              f"{zajavka['dol_1.11']:12}",
              f"{zajavka['dol_1.12']:10}",
              f"{zajavka['dol_kyrs']:^14}",
              f"{zajavka['mark_1.11']:14}",
              f"{zajavka['mark_1.12']:8}",
              f"{zajavka['mark_kyrs']:12}"
              )
     
    print(FOOTER)   

def write_file(zajavka_list):
    """запис списку заявок в файл

    Args:
        zajavka_list ([type]): список заявок
    """
    with open('./data/analiz.txt', "w",  encoding='utf-8') as zajavka_file:
        for zajavka in zajavka_list:
            line = \
                f"{str(zajavka['cod']) + ';':6}"      + \
                f"{str(zajavka['name']) + ';':14}"      + \
                f"{str(zajavka['year']) + ';':12}"      + \
                f"{str(zajavka['dol_1.11']) + ';':7}"      + \
                f"{str(zajavka['dol_1.12']) + ';':7}"      + \
                f"{str(zajavka['dol_kyrs']) + ';':10}"       + \
                f"{str(zajavka['mark_1.11']) + ';':7}"       + \
                f"{str(zajavka['mark_1.12']) + ';':7}"      + \
                f"{str(zajavka['mark_kyrs']) + ';':7}" + '\n'
            
            zajavka_file.write(line)
    
    print("Файл успішно сформовано ...")
            

while True:
    os.system('clear')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')
    
    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        zajavka_list = create_zajavka()
        show_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        zajavka_list = create_zajavka()
        write_file(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        kyrses = get_kyrs()
        show_kyrs(kyrses)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidnik(dovidniks)
        input(STOP_MESSAGE)
        

        
    