#Class to handle all the account related functions
class Account:

    def __init__(self, account_number, account_type, customer_id, balance=0):
        #operate the bank account details 
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.customer_id = customer_id
    
    #function to deposit the money into the account 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"You have Successfully deposited {amount}. Your new balance is: {self.balance}"
        else:
            return "Error! Invalid deposit amount. Please enter a number greater than ZERO."

    #Function to withdraw the money from the account 
    def withdraw(self, amount):
        if amount <= 0:
            return "Error1 Invalid withdrawal amount. Please enter a greater than ZERO."
        if amount > self.balance:
            return "Insufficient funds to withdraw."
        self.balance -= amount
        return f"You have successfully withdrawn the following ammount: {amount}. Your balance remaining: {self.balance}"
    
    #Functions to show represnation of object in account class
    def __str__(self):
        #account number and balance is returned 
        return f"Your Account Number is: {self.account_number}, Your Balance is: £{self.balance}"
    
    #Functions to show the current ballance of the account 
    def get_balance(self):
        #returns the current balance 
        return self.balance

