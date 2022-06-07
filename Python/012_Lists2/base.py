import random
print("-=-=-=-=-=- Random in Python -=-=-=-=-=-")
x = int(input("how many random numbers would you like? "))
thislist = []
for i in range(0,x):
    thislist.append(print(random.randrange(0,9)))