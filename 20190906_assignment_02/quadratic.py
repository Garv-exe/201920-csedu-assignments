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

#**Questions:**

# 1. What does python do if you provide the value 0 for *a*?
# It shows a zerodivision error meaning that the float can't be divided by zero.
# 2. What does python do if $b^2 - 4ac < 0$?
# It shows a value error(Math domain error) meaning that the square root can't happen since the value is negative.
# 3. What does python do if you provide a value for *a*, *b*, or *c* that cannot be converted to a number?
# It shows a value error(could not convert string to float) since the inputed data isn't a number.
# 4. Handling each of the above problems is an aspect of **data validation**. 
# This is the process of ensuring data meets general specifications for a problem. 
# Why is this process important when creating programs such as this one?
# This is an important process when creating programs as it makes sure that the program runs smoothly and there are no errors in the data given. 
# This proves that the program actually works. When these errors occur, the program should print invalid data or no solution.