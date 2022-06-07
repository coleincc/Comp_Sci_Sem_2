x = 0
y = 1
name = input("What is your name? \n")
for i in range (0,len(name)):
    print(name[x:y])
    x = x + 1
    y = y + 1
if(name[x:y] == " "):
    print(name[x:len(name)])
    print(name[0:x])