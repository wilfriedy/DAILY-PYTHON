tempInF = int(input("Enter a Fahrenheit temp : "))
tempInC = ((tempInF -32) * 5) / 9

if tempInC < 0 :
    print("temperature is below freezing")