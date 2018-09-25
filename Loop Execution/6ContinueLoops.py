#Finding an even number

for num in range(2, 10):
    if num % 2 == 0:
        print(num, "is an even number")
        continue #skips all the remaining instructions and proceeds to the next iteration

    #else:
    print(num, "is an odd num")