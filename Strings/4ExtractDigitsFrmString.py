#Extract digits from a string

# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'

digits = []

for element in s:
    if '1234567890'.find(element) != -1:# whenever it does not fail
        digits.append(int(element))
print(digits)
