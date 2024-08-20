# L1T07

# ========= Task 1: Stars =========

# Pseudo Code:

# Create a for loop
# Include i as index variable to define the repetitions of the loop
# Set the range for (1,10) since we need 9 lines 
# Create an if statement for i being smaller or equal to 5
# Use the indented print function to print a star sign multiplied by i 
# Consequently when i = 1 -> 1 star, i = 2-> 2 stars, ... until i = 5 -> 5 stars
# Create an else statement 
# Use the indented print function to print the star sign multiplied by (10-i)
# Consequently when i = 6 -> ((10-6) * "*") = 4 stars ... until i = 9 -> 1 star 



# Python Code: 

for i in range(1,10):
    if i <= 5:
        print("*" * i )
    else:
        print ("*"*(10-i))