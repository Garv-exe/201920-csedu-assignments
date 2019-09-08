# Assignment #02
# Gyungchae Han
# September 6, 2019

print("Welcome to Quadratic Solver!")

a = int(input("Please enter value for a = "))
b = int(input("Please enter value for b = "))
c = int(input("Please enter value for c = "))

x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)

print("x = " + str(x1))if x1 == x2 else print("x = " + str(x1) + " and x = " + str(x2))