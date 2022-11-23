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
            print(f"\n{self.dinosaur.name} attacks {self.robot.name} for {self.dinosaur.attack_power} damage! \n {self.robot.name} has {self.robot.health} remaining!")
            if self.robot.health> 0:
                self.robot.attack(self.dinosaur)
                print(f"\n{self.robot.name} attacks {self.dinosaur.name} for {self.robot.active_weapon.attack_power} damage! \n {self.dinosaur.name} has {self.dinosaur.health} remaining!")
        if self.dinosaur.health<= 0:
            self.winner= self.robot.name
            self.loser= self.dinosaur.name
            print(f"{self.winner} drove {self.loser} to EXTINCTION!!")
        else:
            self.winner= self.dinosaur.name
            self.loser= self.robot.name
            print(f"{self.winner} drove {self.loser} to EXTINCTION!!")
        pass

    def display_winner(self):
        print(f"\nIt's a GOD DANG Dinosaur vs Robot fight! \nAnd it looks like {self.winner} wins! Better luck next time, {self.loser}!\n")
        pass