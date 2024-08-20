# L1T06

# ========= Task 1: While =========

# Pseudo Code:

# Create variable num_random
# Define variable by asking user to input a random numer - using input() and float()
# Create variable total_sum to define the sum of all numbers
# Set total_sum to 0
# Create a variable total_num to define the total of all numbers
# Set total_num to 0

# Create while loop
# Create while statement to repeat unless num_random is -1
# Create indented statement to add each number to total_sum (as long as num_random is not -1)
# Create indented statement to add +1 to the total_num everytime a number is input (as long as num_random is not -1)
# Create indented statement to ask user for another number - use input() and float() function 
# Create if statement for num_random being -1
# Create indented break statement to execute when num_random is -1 to break the loop

# Check if the user has input more than one number.
# If they havn't the input was -1 (which is excluded from the sum and num calculation) and we can't get an average. 
# Create an if statement for total_num > 0
# Create indented statement to calculate the sum_average by dividing the total_sum by total_num 
# Use the indented print function to print: The average of the numbers entered is + sum_average
# Create else statement 
# Use the indented print function to print: No number except -1 was entered. So there is no average.

# Python Code:

num_random = float(input("Please enter a random number: "))

total_sum = 0
total_num = 0

while (num_random) != -1:
    total_sum += num_random
    total_num += 1
    num_random = float(input("Please enter another number: "))
    if num_random == -1:
        break

# Checking if total_num is greater than 0 - avoid "ZeroDivision"-outcome

if(total_num)> 0:
    sum_average = (total_sum/total_num)
    print("The average of the numbers entered is {}".format(sum_average))
else:
    print("No number except -1 was entered. So there is no average.")

