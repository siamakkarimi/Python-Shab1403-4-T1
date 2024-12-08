def tax(hogog):
    return 0.1 * hogog

def bime(hogog):
    return 0.07 * hogog

#=================myProgram
hogog = int(input("Enter Hogog:"))
daryafti = hogog - (tax(hogog) + bime(hogog))
print(f"daryafti shoma: {daryafti}")