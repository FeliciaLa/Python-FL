# L1T11

# ========= Task 1: Student register =========

# Pseudo Code: 

# Create a variable for the number of students and define it by using the input function asking for the number of students 
# User int() to ensure it is an integer
# Create a variable for the list of student ids and define it as an empty list
# Use a for loop that runs for the number of students by defining the range with earlier created variable for number of students 
# Create the variable student id and define it with the input function asking the user for the student id
# Use the append funtcion to add the single student ids to the empty student id list
# Use + "..." to add ... after every student id
# Use with open () function and add a file called 'reg_form.txt' as the first argument and 'w' as the second argument 
# This will create the file re_form.txt once the code is run and will allow us to write to the file
# Use f.write() to write the list of student IDs to the file
# Use '\n' and join() to create the list with paragraphs
# Once run, the file reg_form.txt will then show up in our directory 

#Python Code: 

number_students = int(input("How many users are registering: "))

student_ids = []

for i in range(number_students): 
    student_id = input("Ask for student ID number: ")
    student_ids.append(student_id + "...")

with open('reg_form.txt', 'w') as f: 
    f.write('\n'.join(student_ids))


