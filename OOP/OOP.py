class Sword:
    sharpness = 20
    def __init__(self, brand, yearMade, color):
        self.brand = brand
        self.yearMade = yearMade
        self.color = color
    def sharpen(self, level):
        self.sharpness += level


mySword = Sword('Excalibur', 1500, 'Silver')
print(f"My sword brand is {mySword.brand}")

yourSword = Sword('Masamune', 1300, 'red')
print(f"Your sword brand is {yourSword.brand}")

