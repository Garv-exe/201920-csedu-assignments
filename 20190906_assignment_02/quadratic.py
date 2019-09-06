# Assignment #02
# Your Name
# September 6, 2019

print("Quadratic Equation Solver for y = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def quadraticFunction(a, b, c): 
    return (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)

ans = quadraticFunction(a, b, c)
print("Answer: " + str(ans))

aoeuaoeu