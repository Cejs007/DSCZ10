def filter_by_total_amount(min, max):
    return f"select * from bookings where total_amount between {min} and {max};"


def search_people(first_name_start, last_name_end):
    return f'select first_name, last_name from clients where first_name like "{first_name_start}%" and last_name like "%{last_name_end}";'


def add_member(jmeno, tel_cislo, email, adresa):
    return f'insert into member (name, phone, email, address) values ("{jmeno}", "{tel_cislo}", "{email}", "{adresa}");'


def retrieve_table(table="student", limit=10):
    return f"select * from {table} LIMIT {limit};"


def pridej_studenta(jmeno, prijmeni, table_name="student"):
    return f'insert into {table_name} (jmeno, prijmeni) values ("{jmeno}", "{prijmeni}");'

def vytvor_predmet(nazev, pozadovane_skore, table_name="predmet"):
    return f'insert into {table_name} (nazev, pozadovane_skore) values ("{nazev}", "{pozadovane_skore}");'

def dej_mi_id_studenta_podle_prijmeni(prijmeni, mycursor):
    sql = f'select idstudent from student where prijmeni="{prijmeni}";'
    mycursor.execute(sql)
    vysledek = []
    for x in mycursor:
        vysledek.append(x)
    return x[0]

def dej_mi_id_predmetu_podle_nazvu(nazev, mycursor):
    sql = f'select idpredmety from predmet where nazev="{nazev}";'
    mycursor.execute(sql)
    vysledek = []
    for x in mycursor:
        vysledek.append(x)
    return x[0]
    

def prihlas_studenta_na_statnice(student_prijmeni, datum, mycursor, uspech=0, table_name="statnice"):
    student_id = dej_mi_id_studenta_podle_prijmeni(student_prijmeni, mycursor)
    return f'insert into {table_name} (datum, uspech, student_idstudent) values ("{datum}", "{uspech}", "{student_id}");'

def zapis_vysledek_predmetu_studentovi(student_prijmeni, predmet_nazev, dosazene_skore, mycursor, table_name="vysledek"):
    student_id = dej_mi_id_studenta_podle_prijmeni(student_prijmeni, mycursor)
    predmet_id = dej_mi_id_predmetu_podle_nazvu(predmet_nazev, mycursor)
    return f'insert into {table_name} (student_idstudent, predmet_idpredmety, dosazene_skore) values ("{student_id}", "{predmet_id}", "{dosazene_skore}");'
