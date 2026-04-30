class Player:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def can_bet(self, amount):
        return amount <= self.balance

    def update_balance(self, amount):
        self.balance += amount