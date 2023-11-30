import random
import math

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

class RPS:
    def __init__(self):
        self.figure = [rock, paper, scissors]

    def Compare(self, c1: int, c2: int):
        dif = c1 - c2
        if abs(dif) == 1:
            return dif < 0
        else:
            return dif > 0

    def Play(self):
        uChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors..: "))
        print(self.figure[uChoice])

        cChoice = random.randint(0, 2)
        print(self.figure[cChoice])
        #c = random.choice(self.figure)
        #print(c)

        if uChoice != cChoice:
            if self.Compare(uChoice, cChoice):
                print("You won")
            else:
                print("Computer won")
        else:
            print("Draw")

    
    
game = RPS()
game.Play()
