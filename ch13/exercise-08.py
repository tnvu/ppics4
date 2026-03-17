# Find the rules to an interesting dice game and write an interactive program
# to play it. Some examples are craps, yacht, greed, and skunk.

import random

class TextUI:
    def __init__(self):
        pass

    def promptPassLineBet(self, maxBet):
        while True:
            try:
                bet = float(input("How much to put on the pass line? "))
                if bet <= 0 or bet > maxBet:
                    raise ValueError
                return bet
            except ValueError:
                print("Invalid bet. Please try again")

    def setMoney(self, amt):
        print(f"You have ${amt:0.2f}.")

    def displayDice(self, dice):
        print(f"Dice = {dice}")

    def displayPoint(self, point):
        print(f"The point is: {point}")

    def promptPlayAgain(self):
        ans = input("Play again (Y/n)? ").strip()
        return ans in ['y', 'Y'] or ans == ""
    
    def displayResult(self, amt):
        if amt > 0:
            print(f"You won ${amt:0.2f}")
        else:
            print(f"You lost ${abs(amt):0.2f}")
                         
class Dice:
    def __init__(self):
        self.dice = [0] * 2
        self.roll()

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1, 6)
        return sum(self.dice)
    
    def values(self):
        return self.dice[:]

class CrapsApp:
    def __init__(self, ui):
        self.ui = ui
        self.dice = Dice()
        self.money = 100

    def run(self):
        while True:
            self.ui.setMoney(self.money)
            bet = self.ui.promptPassLineBet(self.money)
            self.money = self.money - bet
            self.ui.setMoney(self.money)
            # Come-Out Roll
            total = self.dice.roll()
            self.ui.displayDice(self.dice.values())
            if total in [7, 11]:
                win = True
            elif total in [2, 3, 12]:
                win = False
            else:
                # Point Phase
                point = total
                self.ui.displayPoint(point)
                while True:
                    total = self.dice.roll()
                    self.ui.displayDice(self.dice.values())
                    if total == point:
                        win = True
                        break
                    elif total == 7:
                        win = False
                        break
            if win:
                self.money = self.money + 2*bet
                self.ui.displayResult(bet)
            else:
                self.ui.displayResult(-1.00 * bet)

            if not (self.money > 0 and self.ui.promptPlayAgain()):
                self.ui.setMoney(self.money)
                break

def main():
    app = CrapsApp(TextUI())
    app.run()

main()