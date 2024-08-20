#L1T10

# ========= Task 1: Dob Task =========


# Pseudo Code: 

# Open the dob.txt file by using the f function
# The first argument is the text file, the second argument is the mode we open the file in 
# Pick r+ for the mode to open the file for reading and writing
# Create a variable for names - define it as an empty list 
# Create a variable for birthdates - define it as an empty list 
# Loop over the lines of the file with "for line in f"
# Create a variable "parts" and define it with the split function to split the line into parts
# Create a variable "name" define it with the join function joining the parts before the last 3 elements of the line (the last 3 elements are the birthdates)
# Use ' ' for the join function to make sure there is a space between the first and last name
# Use the append function to add the names to the names list 
# Create a variable "birthdate" and define it with the join function joining the last 3 elements of the line
# Use ' ' for the join function to make sure there is a space between the parts of the birthdates
# Use the append function to add the birthdates to the birthdates list
# Use the print function to print "Name:" and the list of names
# Use the print function to print "Birthdates:" and the list of birhtdates
# Use \n to ensure the input is printed as a list (listed) and not in a line 
# Close the file 



# Python Code: 

f = open('DOB.txt', 'r+')

names = []  # List to store names
birthdates = []   # List to store birthdates

for line in f:
    parts = line.split()   # Split line into parts 

    name = ' '.join(parts[:-3])    # Join the parts before the last 3 elements to form the name 
    names.append(name)     # Add names to the list 

    birthdate = ' '.join(parts[-3:])    # Join the last 3 elements to form birthdates
    birthdates.append(birthdate)    # Add the birthdate to the list


print("Name:")
print('\n'.join(names))

print("\nBirthdate:")
print('\n'.join(birthdates))

f.close()