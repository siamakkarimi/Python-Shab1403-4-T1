# grade = int(input("Enter a grade(0-20): "))
# if grade > 18:
#     print("A")
# elif grade >= 17:
#     print("B")
# elif grade >= 15:
#     print("c")
# elif grade >= 12:
#     print("d")
# else:
#     print("Mashrot")   


# grade = int(input("Enter a grade(0-20): "))

# if grade > 20 or grade < 0:
#     print("your gradeber is out of range!!!")
# elif grade > 18:
#     print(f"your entered grade is: {grade} and your academic grade is: A")
# elif grade >= 17:
#     print(f"your entered grade is: {grade} and your academic grade is: B")
# elif grade >= 15:
#     print(f"your entered grade is: {grade} and your academic grade is: C")
# elif grade >= 12:
#     print(f"your entered grade is: {grade} and your academic grade is: D")
# else:
#     print("Mashrot")   

grade = int(input("Enter a grade(0-20): "))
letter_academic = 'Mashroot'

if grade > 20 or grade < 0:
    print("your gradeber is out of range!!!")
elif grade > 18:
   letter_academic = 'A'   
elif grade >= 17:
   letter_academic = 'B'    
elif grade >= 15:
   letter_academic = 'C'   
elif grade >= 12:
   letter_academic = 'D'   

print(f"your entered grade is: {grade} and your academic grade is: {letter_academic}")