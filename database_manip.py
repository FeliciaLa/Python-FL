import sqlite3
import os

db = sqlite3.connect('data/python_programming.db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (id INTEGER PRIMARY KEY, name TEXT,
                    grade INTEGER)
''')
db.commit()

cursor.execute('DELETE FROM python_programming') # clearing the table 
db.commit()

# Insert rows

cursor = db.cursor()
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99


student_list = [(id1,name1,grade1),(id2,name2,grade2),(id3,name3,grade3),(id4,name4,grade4),(id5,name5,grade5)]

cursor.executemany(''' INSERT INTO python_programming(id,name,grade) VALUES(?,?,?)''', student_list)

db.commit()

# Select all records with a grade between 60 and 80

cursor.execute ('''
        SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80
''')

records = cursor.fetchall()

for record in records: 
    print(record)

# change carl davis's grade to 65 

cursor.execute (''' 
    UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'
''')
db.commit()

# delete Dennis Fredrickson's row

cursor.execute (''' 
        DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'
''')
db.commit()

# Update the grade of all students with an id greater than 55 to a grade of 80

cursor.execute ('''
        UPDATE python_programming SET grade = 80 WHERE id > 55
''')
db.commit()

db.close()