# GUESS THE NUMBER

import random
target =random.randint(1,50)


while True:
    user=int(input("Guess a number:-"))
    if (user==target):
        print ('You have guess the correct Number')
        break

    elif(user<target):
        print("Your guessed number is lower than the actual number")
        

    else:
        print("Your guessed number is Higher than the actual number")
        

print ("------GAME OVER------")