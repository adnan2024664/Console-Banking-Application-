from bank import Bank

def main_menu():
    print("\nWelcome to Console Banking!")
    print("1. Create Account")
    print("2. Login")
    print("3. Check Balance")
    print("4. Fund Transfer")
    print("5. Exit")

def main():
    bank = Bank("MyBank", "123 Main Street", "contact@mybank.com")
    
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            contact_info = input("Enter your contact information: ")
            customer = bank.add_customer(name, address, contact_info)
            account_type = input("Enter account type (savings/current/mortgage): ")
            account_number = bank.generate_account_number()
            account = customer.create_account(account_type, account_number)
            print(f"Account created successfully! Account Number: {account.account_number}")
        
        elif choice == "5":
            print("Thank you for using Console Banking. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
