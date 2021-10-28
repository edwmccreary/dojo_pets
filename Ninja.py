from Pet_Types import Cat, Bird


class Ninja:
    def __init__(self, fname, lname, pet, treats, pet_food):
        self.fname = fname
        self.lname = lname
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        print(f"{self.fname} takes {self.pet.name} for a walk.")
        self.pet.play()
        return self

    def feed(self):
        if self.hasEnough(self.pet_food):
            self.pet_food -= 1
            print(f"{self.fname} gives {self.pet.name} some food.")
            self.pet.eat()
        else:
            print(f"{self.fname} has no pet food left to give to {self.pet.name}.")
        return self

    def bathe(self):
        if self.hasEnough(self.treats, 2):
            self.treats -= 2
            print(f"{self.fname} gives {self.pet.name} a treat and places it in the bath.")
        else:
            print(f"{self.fname} tries to give {self.pet.name} a bath but {self.pet.name} won't calm down!")
        self.pet.make_noise()
        return self

    @staticmethod
    def hasEnough(item, change = 1):
        if item - change < 0:
            return False
        return True

Shigeru = Ninja("Shigeru","Miyamoto",Cat("Neko",100,100),2,10)
Kagome = Ninja("Kagome","Higerashi",Bird("Tori",50,200),4,4)

Kagome.walk().feed().bathe()
Shigeru.walk().feed().bathe()
