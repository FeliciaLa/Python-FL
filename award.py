# L1T05

# ========= Task 1: Award =========

# Pseudo Code

# Create variable "t_swimming"
# Define the value of the variable with the input function asking for the participant's completion time for the swimming part of the triathlon
# Use the float() function to ensure that the variable is defined as float
# Repeat this process for the variables "t_cycling" and "t_running" asking for participant's completion time for the cycling and running part of the triathlon (respectively)
# Create variable "t_total" and define its value as the sum of the first 3 variables
# Create an if-elif-else statement 
# Start with the if statement: if t_total is smaller or equal to 100 (the qualifying time for awards)
# Use indented print function to print: "The participant will receive the following award: Provincial Colours" (if true)
# Continue with elif statement for t_total being smaller or equal to 105 (the qualifying time + 5 extra minutes)
# Use indented print function to print: "The participant will receive the following award: Provincial Half Colours" (if true)
# Continue with elif statement for t_total being smaller or equal to 110 (the qualifying time + 10 extra minutes)
# Use indented print function to print: "The participant will receive the following award: Provincial Scroll" (if true)
# Use else statement 
# Use indented print function to print: "The participant will receive no award"

# Python Code 

t_swimming = float(input("Enter the participant's completion time for swimming (in minutes): "))
t_cycling = float(input("Enter the participant's completion time for cycling (in minutes): "))
t_running = float(input("Enter the participant's completion time for running (in minutes): "))

t_total = t_swimming + t_cycling + t_running

if t_total <= 100:
    print("The participant will receive the following award: Provincial Colours")
elif t_total <= 105:
    print("The participant will receive the following award: Provincial Half Colours")
elif t_total <= 110:
     print("The participant will receive the following award: Provincial Scroll")
else:
     print("The participant will receive no award")