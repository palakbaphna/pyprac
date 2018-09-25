# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
digits = []
for elem in s:
    if '1234567890'.find(elem) != -1: # == -1 means NOT found , so != -1 means found
        digits.append(int(elem))

print(digits)

