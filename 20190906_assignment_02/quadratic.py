# Assignment #02
# Your Name
# September 6, 2019
import math
print("This program will find the solutions to a quadratic equation using the quadratic formula ")
a = float(input("Please enter the value of a"))
b = float(input("Please enter the value of b"))
c = float(input("Please enter the value of c"))
squareroot =(b**2)-(4*a*c)
squareroot = math.sqrt(squareroot)
finalValueOne= (-b+squareroot)/(2*a)
finalValueTwo= (-b-squareroot)/(2*a)
if finalValueOne == finalValueTwo:
    print("The Solution is: " + str(finalValueOne))
else:
    print("One Solution is " + str(finalValueOne))
    print("Another Solution is " + str(finalValueTwo))

print("Thank you for using my program please rate 5 stars on myspace")