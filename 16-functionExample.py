#===========================Solution1
# def zojyafard(num):
#     if num % 2 == 0:
#         print("zoj")
#     else:
#         print("Fard")
#======================================myProgram
# ans = 'y'
# while ans == 'y':
#  num = int(input("Enter a number: "))
#  zojyafard(num)
#  ans = input("Mikhay Edame bedi(y/n): ")

#===========================Solution2
def zojyafard(num):
    return num % 2 == 0
#=============================myProgram     
ans = 'y'
while ans == 'y':
 num = int(input("Enter a number: "))
 if(zojyafard(num)):
    print("Zoj")
 else:
    print("Fard")
 ans = input("Mikhay Edame bedi(y/n): ")


