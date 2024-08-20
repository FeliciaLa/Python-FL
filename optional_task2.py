#L1T03

# ========= Optional Task 2 =========

#Pseudo Code: 
#Create variable "string_fav" and define it by using the input function asking user to enter favourite restaurant 
#Make sure to use str() function to identify variable as string

#Create variable "int_fav" and and define it by using the input function asking user to enter favourite number
#Make sure to use int() function to identify variable as integer

#print "string_fav"
#print "int_fav"

#Python Code: 
string_fav=str(input("What is your favourite restaurant: "))
int_fav=int(input("What is your favourite number: "))

print("string_fav:{}".format(string_fav))
print("int_fav:{}".format(int_fav))


#cast string_fav to an integer using int() function 
#Function would be: print(int(string_fav))
#Result: error message 
#Why?: string fav is defined as string -> cannot be turned into a number (string_fav's characters can't be interpreted as integers)

