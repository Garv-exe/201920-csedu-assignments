# Lesson #01: Input & Output

#print("Hello, Stranger")
#print ("This is Min")

#print("Waht is your Name?")
#d
#name = input()
#string concatenation: +
#print("Hi, " + name + ", my name is Green")

#variable Rules:
# - can hold a number of types of data
#   -- string: Text/Series of words or symbols
#   -- integer: +/- whole number including 0
#   -- float: +/- "real" numbers including 0
#   -- boolean: True of False
# - Once a variable holds a type of data, 
#   it can only hold that type of data
# ** The behaviour of operations depends on the type of data. **

#a = 4
#print(a+3)
#b = "4"
#print(b+3)
#semantic error: syntax (grammar) and commands (vocabular) make 
#sense but not in context

#type conversion:
#   - int(...): converts to an integer
#   - str(...): converts to a string
#   - float(...): converts to a floating point number
#print(int(b) +3)

# Linear Equation Solver
print("Solve Equations in the Form: ax + n = m")
a = int(input("Enter the value for a: "))
n = int(input("Enter the value for n: "))
m = int(input("Enter the value for m: "))

answer = (m - n) / a 
print(answer)

# Math Operations
#  +, -, /, *
#  **: exponentiation (ex 2 ** 3 = 8)
#  n ** 0.5: square root
