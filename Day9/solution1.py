n = 5
factorial = 1

# for i in range(n, 0, -1):
#     factorial *= i
#
# print(factorial)

while n > 0:
    factorial *= n
    n -=1
print(factorial)