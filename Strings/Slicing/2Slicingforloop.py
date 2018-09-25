#to avoid change in the oringinal list/ tuple, to get the original output in the end, we use slice operator

color = ['purple']

for n in color[:]:              #slicing here makes sure "all elements of array, which at this point is only purple!
    if n == 'purple':
        color += ['yellow']     #yellow is added to the array color, as the statement is true
    if n == 'yellow':           #color array as defined by slice operator carries only value of purple and no yellow
        color += ['Green']      # as it has no yellow element, green wont get added
print(color)
