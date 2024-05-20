import mysql.connector
from sql_queries.sql_queries import add_member, retrieve_table
from faker import Faker

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb",
    autocommit=True
)

fake = Faker()

jmeno = fake.first_name()
telefon = fake.phone_number()
email = fake.email()
adresa = fake.address()

print(jmeno, telefon, email, adresa)

mycursor = mydb.cursor()

mycursor.execute(add_member(jmeno, telefon, email, adresa))
mycursor.execute(retrieve_table("member"))

for x in mycursor:
    print(x)

