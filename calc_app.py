# L1T14

# ========= Task 15: Calculator =========

# Pseudo Code:

# Create 3 equations one for the calculation (simple_equation), one to print the previous equations (print_all_calculations), and one to offer the user the choice to pick one (main)

# define simple_equation to perform calculation
# use try_except block to make sure input is valid
# create variables "num1", "operation", and "num2", ask user for input and use float() to turn the input into floats
# use if-elif-else statement to create 4 different equations based on the operation input.
# make sure, when operation is "/"", num2 is not 0. If so, print error message
# create and print variable "equation" and define it as "num1 operation num2 = result"
# write equation to file "equations.txt" using open(), with statement, and file.write()
# print invalid input for except block (ValueError)

# define print_all_calculations to print the previous calculations
# use try-except block to make sure there are previous calculations
# open file "equations.txt", read file, and assign content to variable "content"
# use if-else statement: if content is there, print content. if content is not there, print error message.
# print error message for except block (FileNotFoundError)

# define main function
# prompt user to choose between 1. a calculation and 2. printing all calculations and store the answer in variable "choice"
# use if-elif-else statement to call the respective equation depending on the user choice or print an error message if the input is neither 1 or 2
# call the main function



# Python Code:

# Function to calculate 

def simple_equation():
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Don't divide by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Pick one of the following: +, -, *, /")
            return
        
        equation = "{} {} {} = {}".format(num1,operation,num2,result)
        print(equation)

        # Write equation to file
        with open("equations.txt", "a") as file:    # create or open file
            file.write(equation + "\n")     # write to file 
    
    except ValueError:
        print("Invalid input.")


# Function to print previous calculations

def print_all_calculations():
    try:
        with open("equations.txt", "r") as file:     # opening file in read mode
            content = file.read()     # read content of file
            if content:    # check that list is not empty
                print("Previous calculations: ")
                print(content)
            else:
                print("No previous calculation found.")
    except FileNotFoundError:
        print("No previous calculation found.")

# Main function

def main():
    while True:
        print("Please choose one of the following options:")
        print("1. Perform a calculation")
        print("2. Print all calculations")
        choice = input("Please answer with 1 or 2: ")

        if choice == '1':
            simple_equation()
        elif choice == '2':
            print_all_calculations()
        else:
            print("Invalid choice. Please choose 1 or 2")

main()