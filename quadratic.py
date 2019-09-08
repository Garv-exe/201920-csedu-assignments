# Assignment #02
# Sunkwan Kim
# September 6, 2019
import math
print("Quadratic Calculator")
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))
d = float(((b**2)-(4*a*c))**0.5)
output1 = (-b + d)/(2*a)
output2 = (-b - d)/(2*a)
print("x is ", end = '')
print(output1, end = ' ')
print("or ", end = '')
print(output2, end = '')

#Questions:
#1. What does python do if you provide the value 0 for a?
#   ZeroDivisoinError: float division by zero
#2. What does python do if b^2 - 4ac < 0?
#   TypeError: can't convert complex to float
#3. What does python do if you provide a value for a, b, or c that cannot be converted to a number?
#   ValueError: could not convert string to float
#4. Handling each of the above problems is an aspect of data validation. 
#This is the process of ensuring data meets general specifications for a problem. 
#Why is this process important when creating programs such as this one?
#   This process is important because if some data gets processed like dividing by zero, 
#   the computer might freeze and crash.