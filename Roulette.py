import random

class Roulette:
    def __init__(self):
        self.numbers = list(range(0, 37))
        self.colors = {
            0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black',
            9: 'red', 10: 'black', 11: 'red', 12: 'black', 13: 'red', 14: 'black', 15: 'red', 16: 'black', 17: 'red',
            18: 'black', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black',
            27: 'red', 28: 'black', 29: 'red', 30: 'black', 31: 'red', 32: 'black', 33: 'red', 34: 'black', 35: 'red',
            36: 'black'
        }

    def spin_table(self):
        return random.choice(self.numbers)

    def get_color(self, number):
        return self.colors.get(number)


class Player:
    def __init__(self, name, asset):
        self.name = name
        self.asset = asset

    def bet(self, amount, number):
        if amount <= self.asset:
            self.asset -= amount
            return Bet(self, amount, number)
        else:
            print(f"You only have {self.asset}, you cannot afford a bet of {amount}!")


class Bet:
    def __init__(self, player, amount, number):
        self.player = player
        self.amount = amount
        self.number = number

    def win_amount(self):
        #TODO: see what the winning values are for bets
        return
