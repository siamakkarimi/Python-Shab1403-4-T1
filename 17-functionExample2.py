def zojyafard(num):
    for item in num:
        if item % 2 == 0:
            print(f"{item} is Zoj")
        else:
            print(f"{item} is Frad")

#==================myProgram
zojyafard([1,2,3,4,5])