import random
list1 = ["McDonalds", "HomeDepot", "TacoBell"]
x = input("pick from: " + str(list1))
a = random.randrange(0,3)
if x == ("McDonalds"):
    menu1 = ["burger", "fries", "coke"]
    print (("I suggest the ") + str(menu1[a]))
elif x == ("HomeDepot"):
    menu2 = ["desk", "shovel", "chair"]
    print (("I suggest the ") + str(menu2[a]))
elif x == ("TacoBell"):
    menu3 = ["taco", "burrito", "nachos"]
    print (("I suggest the ") + str(menu3[a]))