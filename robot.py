from weapon import Weapon 

class Robot:
    def __init__(self, name:str):
        self.name= name
        self.health= 155
        self.active_weapon= Weapon("Rifle", 20)
        pass

    def attack(self, dinosaur):
        dinosaur.health= dinosaur.health- self.active_weapon.attack_power
        pass
