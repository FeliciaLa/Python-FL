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

menu = ['coffee', 'croissant', 'baguette', 'milk']
stock = {
        "coffee": 3,
        "croissant": 2,
        "baguette": 5,
        "milk": 1
        }
price_in_euro = {
        "coffee": 2,
        "croissant": 3,
        "baguette": 7,
        "milk": 2
        }

total_stock_worth = 0

for item in menu:
    item_stock = stock[item]
    item_price = price_in_euro[item]
    item_value = item_stock * item_price
    total_stock_worth += item_value

print("The total stock value is: {} euros".format(total_stock_worth))