class Account:
    def __init__(self, account_number, balance, account_type, customer_id):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.customer_id = customer_id

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. Balance now: {self.balance}"
        return "Amount should be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount should be positive."
        if amount > self.balance:
            return "Not enough balance."
        self.balance -= amount
        return f"Withdrew: {amount}. Remaining balance: {self.balance}"

    def get_balance(self):
        return f"Balance: {self.balance}"
