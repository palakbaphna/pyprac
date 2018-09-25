#Example 5

menu = ['fruits', 'veggies', 'fries', 'oats', 'smoothie']
for food in menu:
    if food != "fries":
        print( "It is good to eat:" ,food)

    else:
        print("No Fries, as it is not healthy!!")

else:
    print("I ate all the healthy food ")

#example 6

menu = ['fruits', 'veggies', 'oats', 'smoothie']
for food in menu:
    if food != "fries":
        print( "It is good to eat:" ,food)

    else:
        print("No Fries, as it is not healthy!!")

else:
    print("I ate all the healthy food ")



#Example 7

print("THIS IS EXAMPLE 7")

food = ['Veggies', 'Fruits', 'Oats', 'Fries', 'Nuts', 'Salads']

for healthyFood in food:
    if (healthyFood == 'Fries'):
        print("Fries are very unhealthy for us.")
    else:
        print(healthyFood, " are very good for health!")
else:
    print("Let's eat only the healthy food!")
