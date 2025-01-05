#Get the customer classs form customer.py 
from customer import Customer

#Handle the customers accounts
class Bank:
    def __init__(self, bank_name, address, contact_email):
        #Gather all of the bank details 
        self.bank_name = bank_name
        self.address = address
        self.contact_email= contact_email
        self.customers = {}

    #Function to get a rare account number 
    def generate_account_number(self):
        #produces a random integer 
        from random import randint
        #ensure the account number is a 6 digit number bwtween two values 
        return f"{randint(100000, 999999)}"

    #Function to add a new memeber to the bank 
    def add_customer(self, name, address, contact_email):
        #gives a rare customer-ID number 
        customer_number = f"{len(self.customers) + 1}"
        latest_customer = Customer(customer_number, name, address, contact_email)
        #Creates a new instance for the new customer 
        self.customers[customer_number] = latest_customer
        #return new customer 
        return latest_customer
    
    #Function to look for a customer by entering the acoount number 
    def find_customer_by_account(self, account_number):
        #look into all of the customers 
        for customer in self.customers.values():
            #look for each account related to the specific cutomer 
            for account in customer.accounts:
                #verify if the account number alligns with target 
                if account.account_number == account_number:
                    #If found, return the matching customer 
                    return customer
        #if no match is found, return none 
        return None
