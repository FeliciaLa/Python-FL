#L1T02

# ========= Task 2: Details =========

#Pseudo Code:
#Request and store the user name using the variable "name" and the input command "Enter your name:"
#Request and store the user age using the variable "age" and the input command "Enter your age:"
#Request and store the user's house number using the variable "house_number" and the input command "Enter your house number:"
#Request and store the user's street name using the variable "street_name" and the input command "Enter your street name:"
#Print out the sentence: ""name" is "age" years old and lives on street "street_name" in houser number "house_number"." using the .format function 

#Python Code: 
name= input("Enter your name: ")
age= input("Enter your age: ")
house_number= input("Enter your house number: ")
street_name= input("Enter your street name: ")
print("{} is {} years old and lives on street {} in house number {}.".format(name, age, street_name, house_number))

