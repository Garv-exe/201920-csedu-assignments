# Assignment #02
# Your Name
# September 6, 2019

# quadratic formula
def quadraticFunction(a, b, c): 
    disc = (b ** 2 - 4 * a * c) ** 0.5
    # remove duplicate by list(dict.fromkeys()) when squared = 0
    return list(dict.fromkeys([(-b + disc) / (2 * a), (-b - disc) / (2 * a)]))

print("Quadratic Equation Solver for y = ax^2 + bx + c")

# inputs
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# calculation
ans = quadraticFunction(a, b, c)

print("Answer(s):", end=" ")
# *ans iterates over list
print(*ans, sep=" and ")