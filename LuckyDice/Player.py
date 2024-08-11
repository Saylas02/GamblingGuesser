class Player:
    def __init__(self, player_name, player_capital):
        self.name = player_name
        self.capital = player_capital

    def place_bet(self, amount):
        if amount > self.capital:
            raise ValueError(f'Amount {amount} is greater than capital {self.capital}')
        self.capital -= amount
        return amount

    def win_bet(self, amount, winning_factor):
        self.capital += amount * winning_factor
        print(f"Congrats, you won {amount * winning_factor}. New capital: {self.capital}")
