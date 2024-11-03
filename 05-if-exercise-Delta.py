# ax2 + bx + c = 0

# Input: a, b ,c
# delta = b2 - 4ac --> sqrt from library math
# output: x1, x2

# from math import sqrt

# a = float(input("enter a:"))
# b = float(input("enter b:"))
# c = float(input("enter c:"))

# delta = b * b - 4 * a * c
# if delta > 0:
#     x1= -b + sqrt(delta) / 2 * a
#     x2= -b - sqrt(delta) / 2 * a
#     print(f"there are two roots: x1 = {x1} and x2 = {x2}")
# elif delta == 0:
#     x1 = -b/2*a
#     print(f"there is a root: x1 = {x1}")
# else:
#     print("There is No Root!")

from math import sqrt

a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

delta = b ** 2 - 4 * a * c
if delta > 0:
    x1= -b + sqrt(delta) / 2 * a
    x2= -b - sqrt(delta) / 2 * a
    print(f"there are two roots: x1 = {x1} and x2 = {x2}")
elif delta == 0:
    x1 = -b / 2 * a
    print(f"there is a root: x1 = {x1}")
else:
    print("There is No Root!")



