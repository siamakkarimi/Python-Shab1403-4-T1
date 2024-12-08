def zojyafard(num):
    zoj = []
    for item in num:
        if item % 2 == 0:
            zoj.append(item)
    return max(zoj)
            
#==================myProgram
# ==========solution1
maxZoj = zojyafard([1,2,3,4,5])
print(maxZoj)

#===============solution2
print(zojyafard([1,2,3,4,5]))