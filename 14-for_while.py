#برنامه ای بنویسید که معدل دانشجو را بدون در نظر گرفتن نمرات زیر 10 محاسبه نماید(نکته:تعداد درس هر دانشجو نامشخص است)

n = int(input("Enter the number of courses:"))
nomarat = []
for i in range(n):
    nomre = float(input("Enter your nomre:")) 
    if(nomre >= 10):
        nomarat.append(nomre)
print(nomarat)        
ave = sum(nomarat)/len(nomarat)
print(f"your average is: {ave}")

# ===============While==============
ans = 'y'
nomarat = []
while ans == 'y':
    nomre = float(input("Enter your nomre:")) 
    if(nomre >= 10):
        nomarat.append(nomre)
    ans = input("Do you want to continue(y/n):")

ave = sum(nomarat)/len(nomarat)
print(f"your average is: {ave}")


