menu={
    'Vada Pav' : 20,
    'Dabeli' : 20,
    'Pani Puri' : 30,
    'Bhel Puri' : 40,
    'Dahi Puri' : 60 ,
    'Pizza' : 80,
    'Pasta' : 50,
    'Burger' : 60,
    'Sandwich' : 70,
    'Salad' : 50,
    'Juice' : 50,
    'Tea' : 10,
    'Coffee' : 15,
    'Milk Shake' : 70,
    }
print("-----WELCOME TO PYTHON RESTAURANT-----")
print("\nHere is our menu :-\nVada Pav - Rs10\nDabeli- Rs20\nPani Puri - Rs30\nBhel Puri - Rs40\nDahi Puri - Rs60\nPizza - Rs80\nPasta - Rs50\nBurger - Rs60\nSandwich - Rs70\nSalad - Rs50\nJuice - Rs50\nTea - Rs10\nCoffee - Rs15\nMilk Shake - Rs70")

print("Please select your order by typing the name of the dish")
amount = 0
order1=input("Enter your order:-")
if order1 in menu.keys():
    amount += menu[order1]
    print("Your order is accepted. The price of",order1,"is Rs",menu[order1])
else:
    print("Sorry, we don't have",order1,"in our menu")

while True:
    order2=input("Do you want to order something else? (Yes/No):- ")
    if order2.lower()=="yes":
        order3=input("Enter your order:-")
        if order3 in menu.keys():
            amount += menu[order3]
            print("Your order is accepted. The price of",order3,"is Rs",menu[order3])
        else:
            print("Sorry, we don't have",order3,"in our menu")  
    elif order2.lower()=="no":
        break
    else:
        print("Invalid input. Please enter Yes or No")
        

print(f"The total amount of your's is Rs {amount}")