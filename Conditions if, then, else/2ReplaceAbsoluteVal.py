#The else keyword with the false-block may be omitted in case nothing should be done if the condition is false.
#  For example, we can replace the variable x with its absolute value like this:

x = int(input())

if x < 0:
    x = -x

print(x)

# the variable x is assigned to -x only if x < 0.
#  In contrast, the instruction print(x) is executed every time,
#  because it's not indented, so it doesn't belong to the true-block.