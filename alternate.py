# L1T09

# ========= Task 1: Alternate =========

# Pseudo Code: 

# Part 1 - Alternating characters

# Create a variable example_string and define it with the input function asking the user to enter a sentence
# Create a variable for a modified version of the example string and define it as ""
# Create a for loop for index variable i in the range of the length of the example_string using the len function
# Create an if statement for i % 2 = 0 - this will filter out only even indexed characters
# Create an indented statement that adds the i indexed character of the example_string to the modified example string 
# Use the upper() function to convert the added character into upper case letters
# Create an else statement
# Create an indented statement that adds the i indexed character of the example_string to the modified example string 
# This time, use the lower() function to ensure that the added character is lower case
# Use the print function to print the modified example string

# Part 2 - Alternating words with split and joint function

# Create another variable single_words for a compilation of the single words (substrings) of the example_string-input
# Define it by using the split() function for the example string
# Create a for loop for index variable i the range of the lenght of the single_words variable using the len() function
# Create an if statement for i % 2 == 0 - this will filter out only every second word
# Create an indented statement that adds the i indexed word to the single_word variable
# Use the upper() function to convert the word into upper case letters
# Create an else statement
# Create an indented statement that adds the i indexed word to the single_word variable
# Use the lower() function to convert the word into lower case letters
# Create a new variable for the modified string 
# Define this variable as "" and add the join function for the single_words variable to create one string out of the list of strings
# Use the print function to print the variable for the modified string



# Python Code: 

# Alternating characters

example_string = input("Enter an example sentence: ")

example_string_modified = ""

for i in range(len(example_string)):
    if i % 2 == 0:
        example_string_modified += example_string[i].upper()
    else:
        example_string_modified += example_string[i].lower()

print(example_string_modified)

# Alternating words using split and join function

single_words = example_string.split()

for(i) in range(len(single_words)):
    if i % 2 == 0:
        single_words[i] = single_words[i].upper()
    else: 
        single_words[i] = single_words[i].lower()

modified_string_2 = " ".join(single_words)

print(modified_string_2)