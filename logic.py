#L1T08

# ========= Task 2: Logic =========

# Pseudo Code

# Create a variable "name" and define it by asking the user to input their name
# Create a varibale "residence" and define it by asking the user to input their residence 
# Create a variable "hobby" and define it by asking the user to input their favourite hobby
# Use the print function to print "Hello, my name is x, I live in x, and my favourite hobbs is x"
# Use the format function to fill in x but list the variables in the wrong order so the sentence does not make sense. 

# Python Code

name = input("Enter your name: ")
residence = input("Enter the city you live in: ")
hobby = input("Enter your favourite hobby: ")

print("Hello, my name is {}, I live in {}, and my favourite hobby is {}.".format(hobby, name, residence))