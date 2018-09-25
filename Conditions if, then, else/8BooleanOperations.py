#check that at least one of the two numbers ends with 0:

a = int(input())
b = int(input())

if a % 10 == 0 or b % 10 == 0 :
    result = True
else:
    result = False

print(result)


p = int(input())
q = int(input())

if p % 10 == 0 or q %10 == 0:
    print("Yes, atlest one of the number is divisible by 10.")
else:
    print("No. None of the numbers are divisible by 10.")
