#A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are equal to its largest element.

a = []
counter = 0
n = int(input("Number of elements:"))

for i in range(0, n):
    num = int(input("Enter the number:"))
    a.append(num)

for i in range(0, n):
    if a[i] == (max(a)):
        counter += 1
print("Number of elements equal to largest number are:", counter)

################################using While loop
seq = []
counter = 0
m = int(input("number of elements:"))
while m > 0:
      a = int(input())
      seq.append(a)

      if a== 0:
          break

for i in range(0, m):
    if seq[i] == max(seq):
        counter += 1

print(counter)