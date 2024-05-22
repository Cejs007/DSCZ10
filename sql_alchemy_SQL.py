from sqlalchemy import create_engine
from sqlalchemy import text
from sql_queries.sql_queries import search_people

engine = create_engine('mysql+pymysql://newuser:michal_007@localhost/car_rental')

first_name_start = input("Zadej začátek křestní:")
last_name_end = input("Zadej konec příjmení:")

with engine.connect() as con:
    query = search_people(first_name_start, last_name_end)
    rs = con.execute(text(query))

print(list(rs))

print("\n", query, "\n", text(query))