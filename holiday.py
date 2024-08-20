#L1T13

# ========= Task 1: holiday =========

# Pseudo Code: 

# Use the options function to create a menu for the different holiday destinations
# create the variables city_flight, num_nights, and rental_days and define them by using the input function 
# prompting the user to input their destination, length of stay, and lenght of car rental respectively
# use int() to cast the response to an integer for num_nights and rental_days

# Calculate the hotel cost (settling for 100 euros per night) 
# by creating a function named hotel costs with num_night as argument and returning the total cost
# Store the result in the variable hotel_total
# Print "The hotel cost is (hotel_total) euros." using the format function

# Calculate the plane cost by creating a function hotel_costs with num_nigths as an argument 
# Use an if elif else statement to retrieve a price based on each city (set rome to 400, Pairs to 200, and London to 300) and return the total cost
# Return 0 for any other input and print "Invalid city"
# Store the result in a variable plane_total
# Print "The plane costs are (plane total) euros." using the format function

# Calculate the car rental cost (settling for 30 euros per night) 
# by creating a function named car_rental with rental_days as argument and returning the total cost
# Store the result in the variable car_total
# Print "The hotel cost is (car total) euros." using the format function

# Calculate the total holiday cost by creating a function holiday_costs with the arguments hotel_total, plane_total, car_total
# Create a variable total_cost, define it as the sum of the three arguments and return it
# Store the result in the variable cost_total
# Print "The total cost of the holiday is (cost total) euros." using the format function

# Python Code:


def options():
    print("Which city are you going to:")
    print("Rome")
    print("Paris")
    print("London")

options()

city_flight = input("Please enter your choice (Please capitalise the first letter): ")
num_nights = int(input("How many days are you staying there?: "))
rental_days = int(input("How many days will you rent a car for?: "))

# Hotel cost for 100 euros per night 

def hotel_costs (num_nights):
    y = num_nights * 100
    return y

hotel_total = hotel_costs(num_nights)

print("The hotel cost is {} euros.".format(hotel_total))

# Plane cost

def plane_costs (city_flight):
    if city_flight == "Rome":
        return 400
    elif city_flight == "Paris":
        return 200
    if city_flight == "London":
        return 300
    else:
        print("Invalid city")
        return 0
    
plane_total = plane_costs(city_flight)
    
print("The plane costs are {} euros.".format(plane_total))

# Car rental for 30 euros per day

def car_rental (rental_days):
    y = rental_days * 30
    return y

car_total = car_rental(rental_days)

print("The rental costs are {} euros.".format(car_total))

# holiday costs

def holiday_costs (hotel_total, plane_total, car_total):
    total_cost = hotel_total + plane_total + car_total
    return total_cost

cost_total =  holiday_costs (hotel_total, plane_total, car_total)

print ("The total cost of the holiday is {} euros.".format(cost_total))

