#Assignment 02
#Seongmin Jeong
#2019 Sep 8th

print ("Solve the Quatratic Fuction!")
a = float(input("Enter the value a: "))
b = float(input("Enter the value b: "))
c = float(input("Enter the value c: "))

x1value = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2value = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print (x1value)
print (x2value)