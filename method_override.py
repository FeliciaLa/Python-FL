# L2T02

# ========= Compulsory Task 2: Method Override =========

name = input("What is your name?: ")
age = int(input("How old are you?: "))
hair_colour = input("What colour is your hair?: ")
eye_colour = input("What colour are your eyes?: ")

# Create class:

class Adult: 
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour   # Create attributes

    def can_drive(self):   # create can drive method
        print("The person is called {} and is old enough to drive.".format(self.name))
        
# Create Subclass:

class Child(Adult): 
    def can_drive(self):
        print("The person is called {} and too young to drive.".format(self.name))
       

# Create Object and determine if older than 18:

if age >= 18:
    person = Adult(name,age,hair_colour,eye_colour)
else:
    person = Child(name,age,hair_colour,eye_colour)

# Call can_drive method: 

person.can_drive()

