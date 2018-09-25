#sum the integers from 1 to n inclusively

sum = 0
n = int(input(" n=?"))

for i in range(1, n+1):
    sum += i

print(sum)
