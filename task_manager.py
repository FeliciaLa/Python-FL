# L1T17

# ========= Task 1: Capstone Project: Part 1 =========

#=====importing libraries===========
import datetime
import os

#====Login Section====

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

def load_users():
    users = {}
    with open('user.txt', 'r') as f:
        for line in f:
            username, password = line.strip().split(', ')
            users[username] = password
        return users
    
def login(users):
    while True: 
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password: 
            print("Successfully logged in!")
            return username
        else:
            print("Username or Password not correct. Please try again.")

# Write functions for the different menu options

# 1: Define function to register user


def register_user(users):
    while True: 
        new_username = input ("Enter a new user name: ")
        if new_username in users: 
            print("Username already exists. Please try another one")
        else:
            break 

    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open('user.txt', 'a') as f:
            f.write(f"{new_username}, {new_password}\n")
        print("User registered")
    else: 
        print("Passwords don't match. User not registered")


# 2: Define function to add a task

def add_task():
    username = input("Who is the task assigned to?: ")
    title = input("What is the title of that person?: ")
    description = input("Describe the task: ")
    due_date = input("When is the task due (YYYY-MM-DD): ")
    assigned_date = datetime.datetime.now().strftime("%Y-%m-%d")
    completed = "No"

    with open('tasks.txt', 'a') as f:
        f.write(f"\n{username}, {title}, {description}, {assigned_date}, {due_date}, {completed}\n")
    print("Task added.")

# 3: Define function to view all tasks

def view_all_tasks():
    with open('tasks.txt', 'r') as f: 
        for line in f:
            username, title, description, assigned_date, due_date, completed = line.strip().split(', ')
            print("Task: {}\nAssigned to: {}\nDate Assigned: {}\nDue Date: {}\nTask Complete? {}\nDescription: {}\n".format(
                title, username, assigned_date, due_date, completed, description))

# 4: Define function to view my tasks 

def view_my_tasks(current_user):
    with open('tasks.txt', 'r') as f:
        for line in f: 
             username, title, description, assigned_date, due_date, completed = line.strip().split(', ')
             if username == current_user: 
                 print("Task: {}\nAssigned to: {}\nDate Assigned: {}\nDue Date: {}\nTask Complete? {}\nDescription: {}\n".format(
    title, username, assigned_date, due_date, completed, description))
                 
# Define main function
                 
def main():
    users = load_users()
    current_user = login(users)
    
    while True:
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

        if menu == 'r':
            register_user(users)
            print(f"Updated users: {users}")

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all_tasks()

        elif menu == 'vm':
            view_my_tasks(current_user)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()
    
        else:
            print("You have entered an invalid input. Please try again")

# Call main function

if __name__== "__main__":
    main()