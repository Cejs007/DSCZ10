def filter_by_total_amount(min, max):
    return f"select * from bookings where total_amount between {min} and {max};"


def search_people(first_name_start, last_name_end):
    return f'select first_name, last_name from clients where first_name like "{first_name_start}%" and last_name like "%{last_name_end}";'


def add_member(jmeno, tel_cislo, email, adresa):
    return f'insert into member (name, phone, email, address) values ("{jmeno}", "{tel_cislo}", "{email}", "{adresa}");'


def retrieve_table(table, limit=10):
    return f"select * from {table} LIMIT {limit};"
