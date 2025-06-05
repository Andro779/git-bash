print("Hello mother facka")
import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               mjor TEXT
               
               
               
               )
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               intructor TEXT
               
               )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREGIN KEY (student_id) REFERENCES students(id),
               FOREGIN KEY (course_id) REFERENCES courses(course_id),
               PRIMARY KEY (student_id, course_id)
               
               )
''')



while True:
    print("1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати курси")
    print("5. Зареєструвати на курс")
    print("6. Показаи студентів на курсі")
    print("7. Вийти")

    choice = input("Оберіть від 1 до 7")

    if choice =="1":
        name = input("Введіть імя студента")
        age = int(input("Введіть вік"))