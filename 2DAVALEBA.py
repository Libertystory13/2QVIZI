import sqlite3

connection = sqlite3.connect('morty.db')
DB = connection.cursor()

DB.execute("CREATE TABLE if not exists dogs(name text, age integer , color text)")
connection.commit()


def read_db():
    DB.execute("SELECT * FROM dogs")
    for i in DB.fetchall():
        print(f"{i[0]} | {i[1]} | {i[2]}")
    get_answer()


def add_dog():
    name = input("მიუთითეთ სახელი: ")
    while len(name) < 2:
        name = input("მიუთითეთ სახელი: ")
    age = input("მიუთითეთ ასაკი: ")
    while not age.isnumeric():
        age = input("მიუთითეთ ასაკი: ")
    color = input("მიუთითეთ ფერი: ")
    while len(color) < 3:
        color = input("მიუთითეთ ფერი: ")
    DB.execute(f"insert into dogs values ('{name}', '{age}', '{color}')")
    connection.commit()
    get_answer()


def get_answer():
    answer = input("აირჩიეთ მოქმედება add / read / finish ").lower()
    if answer == 'read':
        read_db()
    elif answer == 'add':
        add_dog()
    elif answer == 'finish':
        connection.close()
    else:
        get_answer()


get_answer()