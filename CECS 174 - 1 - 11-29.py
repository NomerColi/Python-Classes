import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

class RPS:
    def __init__(self):
        self.figure = [rock, paper, scissors]
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def compare(self, uChoice: int, cChoice: int):
        dif = uChoice - cChoice
        if abs(dif) == 1:
            return dif > 0
        else:
            return dif < 0

    def play(self):
        uChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors.. or 4 to quit: "))
        
        if uChoice == 4:
            return -1
        
        print(self.figure[uChoice])

        cChoice = random.randint(0, 2)
        print(self.figure[cChoice])

        if uChoice != cChoice:
            if self.compare(uChoice, cChoice):
                print("You won")
                self.wins += 1
            else:
                print("Computer won")
                self.losses += 1
        else:
            print("Draw")
            self.ties += 1

        return 1
    
    def calculate_results(self):
        total = self.wins + self.losses + self.ties
        print(f"You played RPS {total} times total")
        winRate = self.wins / total * 100
        print(f"You won {self.wins} times which is {winRate:.1f}%")
        loseRate = self.losses / total * 100
        print(f"You lost {self.losses} times which is {loseRate:.1f}%")
        tieRate = self.ties / total * 100
        print(f"You ties {self.ties} times which is {tieRate:.1f}%")
    
game = RPS()
result = 0
while result != -1:
    result = game.play()
game.calculate_results()