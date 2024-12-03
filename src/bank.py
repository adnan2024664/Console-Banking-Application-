from customer import Customer

class Bank:
    def __init__(self, bank_name, address, contact_info):
        self.bank_name = bank_name
        self.address = address
        self.contact_info = contact_info
        self.customers = {}

    def generate_account_number(self):
        from random import randint
        return f"AC{randint(1000, 9999)}"

    def add_customer(self, name, address, contact_info):
        customer_id = f"C{len(self.customers) + 1}"
        new_customer = Customer(customer_id, name, address, contact_info)
        self.customers[customer_id] = new_customer
        return new_customer

    def find_customer_by_account(self, account_number):
        for customer in self.customers.values():
            for account in customer.accounts:
                if account.account_number == account_number:
                    return customer
        return None
