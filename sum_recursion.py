# L1T16

# ========= Task 1: Sum Recursion =========

# Pseudo Code:
# Define the function adding_up_to that takes a list of integers ('numbers') and a single integer ('index') as arguments
# Define the base case
# Define the recursive call for any other value of 'index' than 0
# Use examples to check function

# Python Code: 

def adding_up_to(numbers,index):
    # Base case:if index is 0, return the element at index 0
    if index == 0:
        return numbers[0]
    # Recursive Call: sum of numbers up to 'index' is the sum of numbers up to 'index-1' plus the current number
    return numbers[index] + adding_up_to(numbers, index-1)
        
# Test cases
if __name__ == "__main__":
    print(adding_up_to([1,4,5,3,12,16],4))
    print(adding_up_to([4,3,1,5],1))


