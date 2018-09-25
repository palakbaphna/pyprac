#reversing a string using loop

s = ('Python is the best programming language')

reversed_string = ''

for i in range(len(s)-1, -1, -1):
    reversed_string += s[i]

print("reversed string: ", reversed_string)

exit()

#The range() function has two sets of parameters, as follows:

#range(stop)

#stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
#range([start], stop[, step])

#start: Starting number of the sequence.
#stop: Generate numbers up to, but not including this number.
#step: Difference between each number in the sequence.