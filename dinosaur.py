class Dinosaur:
    def __init__(self, name:str, attack_power:int):
        self.name= name
        self.attack_power= attack_power
        self.health= 95
        pass

    def attack(self, robot):
        robot.health= robot.health- self.attack_power
        pass
