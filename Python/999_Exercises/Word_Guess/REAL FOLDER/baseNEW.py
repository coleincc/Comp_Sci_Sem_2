import random
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

num = random.randrange(0,12972)
answer = word_list[num]
print(answer)

for i in range(0,6):
    guess = input("Guess a word!" )
    if guess == answer:
        print("You won!")
        a = 1
        break
    else:
        ("Guess again!")

if a == 0:    
    print("You lose! The answer was " + answer)
    
f.close()

