class Sword:
    sharpness = 20
    def sharpen(self, level):
        self.sharpness += level


mySword = Sword()

# print(f"My Sword {mySword.sharpness} % Before")
mySword.sharpen(30)
print(f"My Sword {mySword.sharpness}%  after")
yourSword = Sword()
# print(f"Your Sword {yourSword.sharpness} % Before")
yourSword.sharpen(20)
print(f"Your Sword {yourSword.sharpness}%  after")