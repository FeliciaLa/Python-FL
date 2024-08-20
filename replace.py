#L1T03

# ========= Task 1: Replace =========

#Pseudo Code:
#Create a variable "long_string" and define its value as “The!quick!brown!fox!jumps!over!the!lazy!dog.”
#Create a new variable "long_string1" and define its value using the replace function to replace all !s with tabs
#Print the variable description ans its value by using the print function
#Create a new variable "long_string2" and define its value using the upper function to reprint the sentence in all upper case letters
#Print the variable description ans its value by using the print function
#Create a new variable "long_string3" and define its value using the [::-1] formula to rephrase the sentence backwards
#Print the variable description ans its value by using the print function



#Python Code: 

long_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#Replace

long_string1 = long_string.replace("!", " ")
print("long_string.replace(""!"", " "): {}".format(long_string1))

#Upper Case Letters

long_string2 = long_string1.upper()
print("long_string.upper():{}".format(long_string2))

#Reverse

long_string3 = long_string1[::-1]
print("long_string3:{}".format(long_string3))

      
