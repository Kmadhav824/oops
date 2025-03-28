import random
# print("Hello, World!")
a = 0
b = 1
# Continue the game until either player reaches 15 points
while (a < 15 and b < 15):
    snum1=random.randint(1,6)
    snum2=random.randint(1,6)

    if (snum1 > snum2):
        a+=1
    elif (snum1 < snum2):
        b+=1

if (a > b):
    print('Player 1 wins')

else :
    print('Player 2 wins')