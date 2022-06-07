import datetime
import random
ppl_list = []

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        ppl_list.append(l)

ppl = random.randrange(0,12)
answer = ppl_list[ppl]

com_list = []

with open('Compliment.txt') as x:
    for line in x:
        p = line.strip()
        com_list.append(p)

com = random.randrange(0,5)
ans = com_list[com]
print(answer + " " + ans)

f.close()
