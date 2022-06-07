L = int(input("enter length "))
hv = input("vertical or horizontal ")
if hv=="h":
    for L in range (0,L):
        print("&",end=" ")
elif hv=="v":
    for L in range (0,L):
        print("&"," ")