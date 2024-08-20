#L1T03

# ========= Task 2: Manipulation =========

#Pseudo Code:
#Step 1:
#create the variable str_manip
#define the variable by using the input function to request the user to enter a sentence 
#the user's input is the value of the variable 

#Step2:
#calculate the length of the variable by using the len()function
#define the length as the variable "str_manip_lenth"
#print the variable "str_manip_length" 

#Step 3:
#Create a new variable "last_letter"
#Define the value of the variable by using the [-1:]-function for the input
#Print the last letter (optional)

#Step 4:
#Replace the occurrence of the last letter with @ by using the replace function
#Print the outcome by using the print function 

#Step 5:
#Print the last three letters of str_manip backwards by using the [-1:-4:-1] function

#Step 6:
#Create a 5 letter word consisting of the first 3 letters of str_manip and the last 2 letters
#Define the first 3 letters with [:3] and the last 2 letters with [-2:]
#Print the sum of both 



#Python Code:

#Request Input 
str_manip = input("Enter a sentence: ")

#Calculate and display length
str_manip_length = len(str_manip)
print(str_manip_length)

#Find last letter, replace occurrence with @
last_letter = str_manip[-1:]
print(last_letter)

#replace occurrence with @
print(str_manip.replace(last_letter, "@"))

#print the last 3 characters in str_manip backwards 
print(str_manip[-1:-4:-1])

#create a 5 letter word (first 3 charcaters + last 2 characters)
print(str_manip[:3]+str_manip[-2:])