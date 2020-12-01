""" розрахунок заявок на товари по магазину
"""

from data_service import get_kyrs, get_dovidnik

# словник в якому будуть накопичуватись результати розрахунків
zajavka = {
    "cod":0,
    "name":"",
    "year":0,
    "dol_1.11":0.0,
    "dol_1.12":0.0,
    "dol_kyrs":0,
    "mark_1.11":0.0,
    "mark_1.12":0.0,
    "mark_kyrs":0

}

def create_zajavka():
    """формування списку заявок по магазину на основі вхідних файлів
    """
    dovidniks = get_dovidnik()
    kyrses = get_kyrs()

    def get_bank_name(bank_code):
        """повертає назву банку по його коду

        Args:
            bank_code : код банку

        Returns:
            bank_name: назив банку
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == bank_code:
                return dovidnik[1]

        return "*** назва не знайдена"           

    # список заявк по магаину, що формується
    zajavka_list = []

    # обробляємо послідовно кожний рядок 'kyrs`
    for kyrs in kyrses:
        
        # підготувати робочий словник для рядка `kyrs`
        zajavka_copy = zajavka.copy()

        # заповнити робочий словник значеннями з `kyrs`
        zajavka_copy['cod'] = kyrs[0]
        zajavka_copy['name']  = get_bank_name(kyrs[0]).rstrip()
        zajavka_copy['year']    = kyrs[7]
        zajavka_copy['dol_1.11']  = kyrs[2]
        zajavka_copy['dol_1.12']  = kyrs[3]
        zajavka_copy['dol_kyrs'] = int(float(kyrs[3])*100)
        zajavka_copy['mark_1.11'] = kyrs[5]
        zajavka_copy['mark_1.12'] = kyrs[6]
        zajavka_copy['mark_kyrs'] = int(float(kyrs[6])*100)

        zajavka_list.append(zajavka_copy)

    return zajavka_list


#result = create_zajavka()

#for line in  result:
    #print(line)