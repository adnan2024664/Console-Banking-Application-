from bank import Bank

def show_menu():
    print("\n-- Banking System --")
    print("1. Create Account")
    print("2. Login")
    print("3. Check Balance")
    print("4. Fund Transfer")
    print("5. Exit")

def main():
    bank = Bank("My Bank", "123 Street", "contact@mybank.com")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            contact_info = input("Enter your contact info: ")
            customer = bank.add_customer(name, address, contact_info)
            account_type = input("Enter account type (savings/current/mortgage): ")
            account_number = bank.generate_account_number()
            customer.create_account(account_type, account_number)
            print(f"Account created with Account Number: {account_number}")
        
        elif choice == "2":
            account_number = input("Enter account number: ")
            customer = bank.find_customer_by_account(account_number)
            if customer:
                print(f"Welcome {customer.name}!")
            else:
                print("Account not found.")
        
        elif choice == "3":
            account_number = input("Enter account number: ")
            customer = bank.find_customer_by_account(account_number)
            if customer:
                for account in customer.accounts:
                    print(account.get_balance())
            else:
                print("Account not found.")
        
        elif choice == "5":
            print("Goodbye! see you soon")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
