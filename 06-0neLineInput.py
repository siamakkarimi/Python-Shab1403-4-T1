# Everything defined in python is Object
# object is like a capsule or box
# in every object(box or capsule), there are Methods
# Methods are like functions but inside object(box or capsule)
# In other words, Methods are depends to their object but functions like print are independent

#function: independent
# print("salam")
# input("Enter a number:")
 
#str is a Object 
# str = "siamak karimi"
# print(str.split())

# print(input("enter 3 number:").split())

a, b, c = input("enter 3 number:").split()
print(f"a = {a}, b = {b}, c = {c}")








# from math import sqrt

# a = float(input("enter a:"))
# b = float(input("enter b:"))
# c = float(input("enter c:"))

# delta = b ** 2 - 4 * a * c
# if delta > 0:
#     x1= -b + sqrt(delta) / 2 * a
#     x2= -b - sqrt(delta) / 2 * a
#     print(f"there are two roots: x1 = {x1} and x2 = {x2}")
# elif delta == 0:
#     x1 = -b / 2 * a
#     print(f"there is a root: x1 = {x1}")
# else:
#     print("There is No Root!")