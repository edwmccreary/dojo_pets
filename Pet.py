from random import randint

class Pet:
    def __init__(self, name, tricks, health, energy):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = f"{self.name} looks at you"

    def sleep(self, amt = 25):
        self.energy += amt
    
    def eat(self, energy = 5, health = 10):
        self.energy += energy
        self.health += health
    
    def play(self, health = 5):
        self.health += health
        print(f"{self.name} does a trick: {self.tricks[randint(0,len(self.tricks)-1)]}")

    def make_noise(self):
        print(self.noise)
