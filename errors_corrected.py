# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")   # Syntax error: missing the parenthesis
print ("\n") # Syntax error: The print line is unneccessarily indented + missing the parenthesis

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax error: == instead of =
age = int(age_Str) 
print("I'm {} years old.".format(age_Str))   # Syntax error: missing format function and brackets

    # Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Syntax error: corrected to an integer # Logic error: corrected to 3.5 - We want to know how old I am in 3 years and 6 months rather than 3 years 
total_years = age + years_from_now

print("The total number of years: {}".format(total_years)) # Syntax: missing the parenthesis + mssing format function and brackets

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Logic error: corrected calculation: to get the total amount of months you need to multiply the total amount of years times 12
print("In 3 years and 6 months, I'll be {} months old".format(total_months)) # Syntax: missing parenthesis + missing format function and brackets

#HINT, 330 months is the correct answer

