import random
import Player
import Bet


class Game:
    def __init__(self, player):
        self.player = player
        self.symbol_to_dict = ["officer", "car", "train", "ring", "bulb", "faucet"]

    def roll_dice(self):
        i = 0
        arr_rolled_numbers = []
        while i < 3:
            arr_rolled_numbers.append(random.randint(1, 6))
            i += 1
        return arr_rolled_numbers

    def play_round(self):
        try:
            number = int(input("Place your bet on a number (1-6): "))
            if number < 1 or number > 6:
                print("Number must be between 1 and 6")
                return
            amount = int(input(f"How much do you want to bet? (Balance: {self.player.capital}): "))
            bet = Bet.Bet(number, self.player.place_bet(amount))

            arr_rolled_numbers = self.roll_dice()
            print(f"The dice rolled: {arr_rolled_numbers}")

            if arr_rolled_numbers.count(bet.number) > 0:
                winning_factor = arr_rolled_numbers.count(bet.number) + 1
                self.player.win_bet(bet.amount, winning_factor)
            else:
                print(f"Sorry, you lost. Your new balance is {self.player.capital}.")
        except ValueError as e:
            print(e)

    def start_game(self):
        while self.player.capital > 0:
            self.play_round()
        print(f"Game over! Your final balance is {self.player.capital}.")


player_name = input("Enter your name: ")
player_capital = int(input("Enter your starting balance: "))
player = Player.Player(player_name, player_capital)
game = Game(player)
game.start_game()



