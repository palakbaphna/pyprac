#Write a boolean function to find if a number is divisible by another one

def isDivisible(x ,y ):
    if x % y == 0:
        result = True
    else:
        result = False
    return result

print(isDivisible(20,10))

