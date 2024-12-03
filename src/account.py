class Account:
    def __init__(self, account_number, balance, account_type, customer_id):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.customer_id = customer_id

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.balance}"

    def check_balance(self):
        return f"Current balance: {self.balance}"
