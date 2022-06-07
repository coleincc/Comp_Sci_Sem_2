print("$ cash register $")
print()
total = 0
a = int(input("how many items would you like to buy?\n"))
for z in range (0,a):
    b = input("what item are you buying?\n")
    c = int(input("what is the cost of the item?\n"))
    total = total + c 
    
print("Your total is: " + str(total))
