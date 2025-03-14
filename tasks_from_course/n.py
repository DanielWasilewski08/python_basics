import random
class Dice:
    def roll(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        return x,y
random_tuple = Dice()
print(random_tuple.roll())