#Range() can define an empty sequence, like range(-5) or range(7, 3). In this case the for-block won't be executed:

for i in range(-5):
    print("Hello World")

for i in range(7, 3):
    print("Hello World")
    