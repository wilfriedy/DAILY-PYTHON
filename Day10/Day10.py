n = 5
factorial = 1
userInput = int(input("Enter a number : "))

if userInput >= 2:
    for i in range(userInput, 0, -1):
        factorial *= i
    print(factorial)
elif userInput <= 1 :
    for i in range(n, 0, -1):
        factorial *= i
    print(factorial)



# def ourFirstFunc (name, age, height = "170cm") :
#     """
#     This function prints greetings
#     :param name:
#     :param age:
#     :param height:
#     :return:
#     """
#     template = f"Hello {name}, age : {age}, height : {height}"
#     return template
    # print(f"Hello {name}, age : {age}, height : {height}")

# ourFirstFunc("Jake", 23, "150cm")
# result = ourFirstFunc("Jake", 23, "180cm")
# print(result)

# print(help(ourFirstFunc))
# ourFirstFunc("Jake", 23, "150cm")
# ourFirstFunc("Mo", 40)
# ourFirstFunc("Mikey", 24)



