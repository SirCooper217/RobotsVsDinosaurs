from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur= Dinosaur("Randy", 15)
        self.robot= Robot("Tobot")
        pass

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print("\nIt's a GOD DANG Dinosaur vs Robot fight! \nLet's get ready to RUMBLLLLLE\n")
        pass

    def battle_phase(self):
        while self.dinosaur.health> 0 and self.robot.health> 0:
            self.dinosaur.attack(self.robot)
            print(f"\nDino attacks Robo for {self.dinosaur.attack_power} damage! \n Robo has {self.robot.health} remaining!")
            if self.robot.health> 0:
                self.robot.attack(self.dinosaur)
                print(f"\nRobo attacks Dino for {self.robot.active_weapon.attack_power} damage! \n Dino has {self.dinosaur.health} remaining!")
        if self.dinosaur.health<= 0:
            self.winner= self.robot.name
            print("Robo time")
        else:
            self.winner= self.dinosaur.name
            print("Dino time")
        pass

    def display_winner(self):
        print(f"\nIt's a GOD DANG Dinosaur vs Robot fight! \nAnd it looks like {self.winner} wins!\n")
        pass