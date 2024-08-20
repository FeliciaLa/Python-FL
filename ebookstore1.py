#L2T07

# ========= Capstone Project =========

# Create table 

import sqlite3
import os

db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_table (
        id INTEGER PRIMARY KEY, 
        title TEXT,
        author TEXT, 
        qty INTEGER
    )
''')
db.commit()

# Clear table

cursor.execute('DELETE FROM book_table') 
db.commit()

# Insert rows

cursor = db.cursor()

book_list = [
       (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
       (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
       (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
       (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
       (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]
cursor.executemany('''
        INSERT INTO book_table(id, title, author, qty) 
        VALUES (?,?,?,?)
        ''', 
        book_list
)
db.commit()
                   
# Create menu

while True:
    print("\nMenu:")
    print("1.Enter book")
    print("2.Update book")
    print("3.Delete book")
    print("4.Search book")
    print("0.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        id = int(input("Enter book id: "))
        cursor.execute('SELECT*FROM book_table WHERE id = ?', (id,))
        if cursor.fetchone():
            print(
                "A book with this id already exists."
                "Please enter a different id."
            )
        else:
            title = input("Enter book title: ")
            author = input ("Enter book author: ")
            qty = int(input ("Enter quantity: "))
            cursor.execute('''
                INSERT INTO book_table(id,title,author,qty)
                VALUES (?,?,?,?)
            ''', (id,title,author,qty))
            db.commit()
            print("Book added succesfully.")
    
    elif choice == '2':
        id = int(input("Enter book id to update: "))
        column = input("Enter the column to update (title/author/qty): ").lower()
        new_value = input ("Enter the new value for {}: ".format(column))
        if column == "qty": 
            new_value = int(new_value)
        query = "UPDATE book_table SET {} = ? WHERE id = ?".format(column)
        cursor.execute(query, (new_value, id))
        db.commit()
        print("Book updated successfully.")

    elif choice == '3':
        id = int(input("Enter book id to delete: "))
        cursor.execute('''
            DELETE FROM book_table
            WHERE id = ?
        ''', (id,))
        db.commit()
        print("Book deleted successfully.")

    elif choice == '4':
        id = int(input("Enter book id to search: "))
        cursor.execute('''
            SELECT * FROM book_table 
            WHERE id = ? 
        ''', (id,))
        book = cursor.fetchone()
        if book: 
            print(
                "id = {}, title = {}, author = {}, qty = {}".format(
                    book[0],book[1],book[2],book[3]
                )
            )
        else:
            print("Book not found.")

    elif choice == "0":
        break
    
    else:
        print("Invalid choice. Please try again.")

db.close()
