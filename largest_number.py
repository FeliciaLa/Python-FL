#L1T16

# ========= Task 2: largest number =========

# Pseudo Code:
# Define function 'largest number'
# Define Base Case: If the list contains only one element, return that element. 
# Define Recursive call:
# Define 'max_of_rest' variable with the largest number function and a list of numbers excluding the first one
# Compare the first element of the list with the largest of the rest
# Use if else function to return bigger number
# Use examples to check function


# Python Code:

def largest_number(numbers):
    # Base case: If the list contains only one element, return the element
    if len(numbers) == 1:
        return numbers[0]
    
    # Recursive case: find the largest number in the rest of the list
    max_of_rest = largest_number(numbers[1:])

    # Compare the first element with the largest of the rest
    if numbers[0] > max_of_rest:
        return numbers[0]
    else: 
        return max_of_rest
    
# Examples: 
if __name__ == "__main__":
    print(largest_number([1, 4, 5, 3]))
    print(largest_number([3, 1, 6, 8, 2, 4, 5]))
