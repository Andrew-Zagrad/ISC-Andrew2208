def get_dovidnik():
    with open("./data/dovidnik.txt", encoding='utf-8') as dovidnik_file: 
        from_dovidnik = dovidnik_file.readlines()

    dovidnik_list = [] 

    for line in from_dovidnik:
        line_list = line.split(';')
        dovidnik_list.append(line_list)

   
    return dovidnik_list

def get_kyrs():
    with open("./data/kyrs.txt", encoding='utf-8') as kyrs_file:
        from_kyrs = kyrs_file.readlines()

    kyrs_list = [] 

    for line in from_kyrs:
        line_list = line.split(';')
        kyrs_list.append(line_list)

    return kyrs_list

def show_dovidnik(dovidnik):
    dovidnik_code_from = input("З якого коду банку?")
    dovidnik_code_to = input("По який код банку?")

    kol_lines = 0
    
    for cod in dovidnik:
        
        if dovidnik_code_from <= cod[0] <= dovidnik_code_to:
            print("Код: {:8} Найменування банку:{:20} ".format(cod[0], cod[1].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(dovidnik_code_from, dovidnik_code_to))

def show_kyrs(kyrs):
    kyrs_code_from = input("З якого коду банку?")
    kyrs_code_to = input("По який код банку?")

    kol_lines = 0

    for cod in kyrs:
        if kyrs_code_from <= cod[0] <= kyrs_code_to:
            print("Код:{:5} Долари,курс на 1.10:{:6} Курс на 1.11:{:6} Курс на 1.12:{:6} Марки,курс на 1.10:{:6} Курс на 1.11:{:6} Курс на 1.12:{:6} Рік:{:6}".format(cod[0], cod[1], cod[2], cod[3], cod[4], cod[5], cod[6], cod[7].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(kyrs_code_from, kyrs_code_to))

