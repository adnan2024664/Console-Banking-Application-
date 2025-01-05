#Class to handle the user data and bank account

#bring in the class from the oAccount.py 
from account import Account

class Customer:
    def __init__(self, customer_number, name, address, contact_info):
        #Get all the details of the user 
        self.customer_number = customer_number
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = []

    #Function for creating a new account
    def create_account(self, type_of_account, account_number, initial_balance=0):
        #new account 
        new_account = Account(account_number,  type_of_account, self.customer_number, initial_balance)
        self.accounts.append(new_account)
        return new_account
        

    #Function to show accounts related to the customer 
    def list_accounts(self):
        return [f"{acc.account_number} - {acc.type_of_account}" for acc in self.accounts]
