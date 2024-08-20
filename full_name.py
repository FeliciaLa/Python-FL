#L1T04

# ========= Task 1: Full Name =========

#Pseudo Code 

#Create a variable "full_name"
#Define the value of the variable with the input function asking for their name

#Create an if-elif-else statement 
#Create an if statement including the len() function to define the length of the input
#State: If length of variable == 0. 
#Create indented print function to print "You haven't entered anything. Please enter your full name:" (if True)
#If the input is 0, the statement will be printed
#If the input is not 0, the statement is False and the next statement will be checked. 
#Create elif statement for length of varibale < 4
#Create indented print function for "You have entered less than 4 characters. Please make sure that you have entered your name and surname." (if True)
#Create next elif statement for length of variable >25
#Create indented print function for "You have entered more than 25 characters. Please make sure that you have only entered your full name." (if True)
#Create else statement
#Create indented print function for "Thank you for entering your name." (if True)

#Python Code:
full_name = input("Enter your full name: ")

if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")

