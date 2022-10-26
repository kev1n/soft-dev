#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


def courses_to_db():
    with open('courses.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        db.execute("DROP TABLE if exists courses;")
        c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);")
        for row in reader:
            c.execute(f'INSERT INTO courses VALUES("{row.get("code")}", {row.get("mark")}, {row.get("id")});')

def students_to_db():
    with open('students.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        db.execute("DROP TABLE if exists students")
        c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);")
        for row in reader:
            c.execute(f'INSERT INTO students VALUES("{row.get("name")}", {row.get("age")}, {row.get("id")});')

courses_to_db()
students_to_db()
c.execute("SELECT * FROM courses;")
#print(c.fetchall())
c.execute("SELECT * FROM students;")
#print(c.fetchall())

#==========================================================
db.execute(f'SELECT id FROM students WHERE name="{"alison"}"')
print(c.fetchone())

#def name_to_id(name):




db.commit() #save changes
db.close()  #close database
