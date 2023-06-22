products = {"Juice":2.50, "Soda":2.00, "Water": 1, "Chips":1.50}
prodToBuy = input("Enter the product you want to buy : ")

if prodToBuy.capitalize() in products:
    money = int(input("How much do you have : "))
    if money < products[prodToBuy.capitalize()]:
        print("Insufficient funds")
    elif money > products[prodToBuy.capitalize()]:
        change = money - products[prodToBuy.capitalize()]
        print(f"Your change is ${change}")
else:
    print("We dont have this")
