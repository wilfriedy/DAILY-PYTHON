user = input("Pls enter your category : ")

match user.capitalize():
    case "Child":
        print('Cost is $10')
    case "Adult":
        print('Cost is $20')
    case "Senior":
        print('Cost is $15')
    case _:
        print("This category does not exist")