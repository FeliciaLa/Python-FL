#L1T12

# ========= Task 1: Cafe =========

# Pseudo Code

# Create a list called menu and add 4 items 
# Create a dictionary called stock with the keys being the items and the values being the number of items
# Create another dictionary called price_in_euros with the keys being the items and the values being the price of the items
# Create a variable for the total stock and define it as 0
# Create a loop to iterate over every item in the menu list 
# Create a variable for the item stock and retrieve its value from the stock dictionary 
# Create a variable for the item prices and retrieve its value from the price_in_euros dictionary
# Create a variable for the total item values and define it as the item stock multiplied by the item prices
# Add the total item values to the total stock worth
# Print the result as "The total stock value is (total stock worth) euros" using the format function. 

# Python Code

# Define the menu with 4 items
menu = ['coffee', 'croissant', 'baguette', 'milk']

# Define the stock level for each item
stock = {
        "coffee": 3,
        "croissant": 2,
        "baguette": 5,
        "milk": 1
        }

# Define the price of each item in euros
price_in_euro = {
        "coffee": 2,
        "croissant": 3,
        "baguette": 7,
        "milk": 2
        }

# Initialise the total_stock_worth variable
total_stock_worth = 0

# Loop through each item in the menu to calculate the total stock value
for item in menu:
    item_stock = stock[item]
    item_price = price_in_euro[item]
    total_item_value = item_stock * item_price
    total_stock_worth += total_item_value

# Print the total stock worth in euros
print("The total stock value is: {} euros".format(total_stock_worth))
