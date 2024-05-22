def filter_by_total_amount(min, max):
    return f"select * from bookings where total_amount between {min} and {max};"


def search_people(first_name_start, last_name_end):
    return f'select first_name, last_name from clients where first_name like "{first_name_start}%" and last_name like "%{last_name_end}";'


def add_member(jmeno, tel_cislo, email, adresa):
    return f'insert into member (name, phone, email, address) values ("{jmeno}", "{tel_cislo}", "{email}", "{adresa}");'


def zobraz_obsah_tabulky(table="student", limit=10):
    '''
    zobrazí prvních 10 záznamů z tabulky
    '''
    return f"select * from {table} LIMIT {limit};"


def pridej_studenta(jmeno, prijmeni, table_name="student"):
    '''
    vezme jméno, příjmení a vytvoří sql insert into..., který pak použijeme pro execute
    '''
    return f'insert into {table_name} (jmeno, prijmeni) values ("{jmeno}", "{prijmeni}");'

def vytvor_predmet(nazev, pozadovane_skore, table_name="predmet"):
    '''
    vezme nazev, pozadovane_skore a vytvori sql typu insert
    '''
    return f'insert into {table_name} (nazev, pozadovane_skore) values ("{nazev}", "{pozadovane_skore}");'

def dej_mi_id_studenta_podle_prijmeni(prijmeni, mycursor):
    '''
    pomocná funkce pro získání id studenta -> protože nemůžu přihlásit státnice nebo zapsat výsledek bez studenta
    je tam vazba
    '''
    #select podle prijméní mi vrať id - generuji sql
    sql = f'select idstudent from student where prijmeni="{prijmeni}";'
    #provedu sql
    mycursor.execute(sql)
    #přečtu výsledek -> beru jenom první hodnotu -> předpokládám jenom unikátní příjmení
    vysledek = []
    for x in mycursor:
        vysledek.append(x)
    return x[0]

def dej_mi_id_predmetu_podle_nazvu(nazev, mycursor):
    '''
    pro zapsání výsledku potřebuji předmět
    '''
    #generuji select query podle názvu předmětu mi dej id předmětu
    sql = f'select idpredmety from predmet where nazev="{nazev}";'
    #provedu sql query
    mycursor.execute(sql)
    #přečtu výsledek
    vysledek = []
    for x in mycursor:
        vysledek.append(x)
    #vracím první nalezený -> nepředpokládám duplicitní název
    return x[0]
    

def prihlas_studenta_na_statnice(student_prijmeni, datum, mycursor, uspech=0, table_name="statnice"):
    '''
    zapíšu studenta podle příjmení na dané datum na státnice -> vytvořím státnice s vazbou na studenta
    '''
    #použiju pomocnou funkci pro získání id studenta podle příjmení
    student_id = dej_mi_id_studenta_podle_prijmeni(student_prijmeni, mycursor)
    return f'insert into {table_name} (datum, uspech, student_idstudent) values ("{datum}", "{uspech}", "{student_id}");'

def zapis_vysledek_predmetu_studentovi(student_prijmeni, predmet_nazev, dosazene_skore, mycursor, table_name="vysledek"):
    '''
    zápis výsledku k studentovi a předmětu
    '''
    #pomocné funkce pro získání id
    student_id = dej_mi_id_studenta_podle_prijmeni(student_prijmeni, mycursor)
    predmet_id = dej_mi_id_predmetu_podle_nazvu(predmet_nazev, mycursor)
    return f'insert into {table_name} (student_idstudent, predmet_idpredmety, dosazene_skore) values ("{student_id}", "{predmet_id}", "{dosazene_skore}");'
