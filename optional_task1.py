import math
#L1T03

# ========= Optional Task 1 =========

#Pseudo Code:

#create variable "side1"
#define variable "side1" by using input function asking user to enter lenght of side 1 of the triangle
#make sure to include float()to mark the input as a number

#create variable "side2"
#define variable "side2" by using input function asking user to enter lenght of side 2 of the triangle
#make sure to include float()to mark the input as a number

#create variable "side3"
#define variable "side3" by using input function asking user to enter lenght of side 3 of the triangle
#make sure to include float()to mark the input as a number

#create a variable s_triangle and define it by using the formula s_triangle= (side1 + side2 + side3)/2 

#create a variable area_triangle and define it by using the the formula area_triangle = √(s_triangle(s_triangle-side1)*(s_triangle-side2)*(s_triangle-side3))

#print variable "area_triangle"


#Python Code:

side1=float(input("Enter the lenght of the first side of the triangle: "))
side2=float(input("Enter the lenght of the second side of the triangle: "))
side3=float(input("Enter the lenght of the third side of the triangle: "))

s_triangle = (side1+side2+side3)/2

area_triangle = math.sqrt(s_triangle*(s_triangle-side1)*(s_triangle-side2)*(s_triangle-side3))

print(area_triangle)


