#L1T08

# ========= Task 2: Optional =========

# Write a program with two compilation errors (Syntax), a runtime error and a logical error.

# Pseudo Code:

# Create two variables and assign them the values "Good morning" and "Good night"
# Syntax error 1: Leave out the quotation marks 
# Syntax error 2: Use a double == instead of a single = 
# Create a variable for the time of the day and define it by using the input function and int()
# Create an if statement for the time being between 6 and 16
# Use indented print function to print the "Good night"-variable 
# Instead of using the whole varibale, print a range 
# Running error 1: Print the range starting with 1 -> this will leave out the first letter
# Create an else stament
# Use indented print function to print "Good morning"-variable 
# Logic error 1: The program is going to print good morning during night time 
# Logic error 2: The program will also print good night if the input is higher than 24 or lower than 0 despite the instruction


# Python Code: 


greeting_morning = Good morning   # Syntax error 1: Corrected: "Good morning" (indicates string)
greeting_night == "Good night"   # Syntax error 2: Corrected: = instead of ==

time_of_the_day = int(input("Enter what time it is (0-24): "))

if 6 <= time_of_the_day <=16:
    print(greeting_night[1:10])   # Running error 1: running it 1-12 is going to exclude the first letter (O is counted when giving a range)
else:
    print(greeting_morning)     # Logic error 1: the program is going to print "good morning" after 4pm and before 6 am - non sensical # Logic error 2: It is also going to give results for after 24 and below 0



