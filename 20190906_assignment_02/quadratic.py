# Assignment #02
# Your Name
# September 6, 2019

def quadraticFunction(a, b, c): 
    squared = (b ** 2 - 4 * a * c) ** 0.5
    # remove duplicate by list(dict.fromkeys())
    return list(dict.fromkeys([(-b + squared) / (2 * a), (-b - squared) / (2 * a)]))

print("Quadratic Equation Solver for y = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

ans = quadraticFunction(a, b, c)
# *ans iterates over list
print(*ans, sep=" and ")