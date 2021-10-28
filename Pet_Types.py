from Pet import Pet

class Cat(Pet):
    def __init__(self, name, health, energy):
        self.tricks = ["roll over for belly rubs","chase string","walks on keyboard"]
        super().__init__(name, self.tricks, health, energy)
        self.noise = "meow"

    def purr():
        print("purrrrr")

class Bird(Pet):
    def __init__(self, name, health, energy):
        self.tricks = ["says: Hi!","land on finger","says: Whatcha doin??"]
        super().__init__(name, self.tricks, health, energy)
        self.noise = "screech"

    def fly(self):
        self.energy -= 2
        print(f"{self.name} flies around the room")
