#By default, the function print() prints all its arguments separating them by a space and the puts a newline symbol after it.
# This behavior can be changed using keyword arguments sep (separator) and end.

print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ')
print(4, 5, 6, sep=', ', end='. ')
print()
print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')