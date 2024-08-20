# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax error: needs to be indicated as string
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {}. It is a {} and it has {} teeth.".format(animal, animal_type, number_of_teeth) # Sytnax error: Missing format function and brackets; # Logic error: number of teeth and animal type need to be interchanged

print(full_spec) #Syntax error: missing parenthesis 

