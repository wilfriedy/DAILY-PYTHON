secret = 10
guess = 0
chance = 2

while secret > 0:
    secret -= 1
    if secret % 3 == 0 :
        continue
    print(secret)



# while True :
#     print("Hello")
#     break

# while guess != secret:
#     guess = int(input("Guess the secret number : "))
#     if chance < 1:
#         break
#     chance -= 1
#     print(chance)
#
#     if guess < secret:
#         print("Guess is too small increase your option")
#     else:
#         print("Guess is too high")
# else:
#     print("You guessed the right number")