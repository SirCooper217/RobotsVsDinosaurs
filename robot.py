from weapon import Weapon 

class Robot:
    def __init__(self, name:str):
        self.name= name
        self.health= [30]
        self.active_weapon= Weapon("Rifle", 5)
        pass

    def attack(self, dinosaur):
        dinosaur.health= dinosaur.health- self.active_weapon.attack_power
        pass
