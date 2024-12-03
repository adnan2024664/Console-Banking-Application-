from account import Account

class Customer:
    def __init__(self, customer_id, name, address, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = []

    def create_account(self, account_type, account_number):
        new_account = Account(account_number, 0, account_type, self.customer_id)
        self.accounts.append(new_account)
        return new_account

    def list_accounts(self):
        return [f"{acc.account_number} - {acc.account_type}" for acc in self.accounts]
