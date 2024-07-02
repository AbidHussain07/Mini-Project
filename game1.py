import random

display = ("GAME \n 1= Stone \n 2 = Paper \n 3 = Scissor ")
print(display)
choice = random.randint(1,3)
# a= "Stone"
# b= "Paper"
# c = "Scissor"
a=1
b=2
c=3
user=int(input("Enter any Number from 1 to 3 :- "))
print("Computer choose's :-",choice)
if (user==choice):
    print("It's draw")

elif(user==a and choice==b):
    print("Computer Win")

elif(user==a and choice==c):
    print("You Win")

elif(user==b and choice==a):
    print("You Win")

elif(user==b and choice==c):
    print("Computer Win")

elif(user==c and choice==a):
    print("Computer Win")

else:
    print("You Win")