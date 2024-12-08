# Everything defined in python is Object
#هر چیزی که در پایتون تعریف میکنیم، یک شی است
# object is like a capsule or box 
# هر شی را می توان یک کپسول یا جعبه ابزار یا آرایش در نظز گرفت
# in every object(box or capsule), there are:
# 1)property(state or data)
# 2)Methods(functions)

# Methods are like functions but inside object(box or capsule)
# In other words, Methods are depends to their object
# but functions like print() and input() are independent(you can use everywhere)

#function: independent
# print("salam")
# input("Enter a number:")
 
#string(data type) is a Object 
# str = "siamak Najjar karimi"
# print(str.split())

# print(input("enter 3 number:").split())

# a, b, c = input("enter 3 number:").split()
# r = float(input("enteer shoa"))
a, b, c = map(float,input("enter 3 number:").split())
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