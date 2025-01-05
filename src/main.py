#Main system code for the Console banking application

#Import tinker for the User interface 
import tkinter as tk
#Interface as a simple user interaction with messagboxes 
from tkinter import simpledialog, messagebox

#Bring the bank class from bank.py
from bank import Bank

#determine the bank, whcih will manage the GUI
class ConsoleBankingApp:
    def __init__(self, master):
        #Determine the main app window 
        self.master = master
        #Title of the main window 
        self.master.title("MyBank Banking System")
        self.bank = Bank("MyBank", "28 Bank St", "ContactMyBank@gmail.com")
        
        #The method whcih will display the widgets 
        self.create_widgets()

    #Create widgets for each section/btton 
    def create_widgets(self):
        #customised colours, fonts and sizes for buttons and text 
        heading_font = ("Adiro", 25, "bold") #heading Font 
        subheading_font = ("adiro, 20") #subheading font 
        button_font = ("Arial", 16, "bold") #Button Font
        button_color = "#ADD8E6"  #Colour of the button
        button_text_color = "black" #Text Colour
        
        #Main heading style 
        self.label = tk.Label(
            self.master,
            #Title: Welcome message 
            text="Hi! Welcome to MyBank Banking App",
            font=heading_font,
            fg="#00008B"
        )
        self.label.pack(pady=10)

        #Subheading style 
        self.subheading = tk.Label(
            self.master,
            #Subheading text message 
            text="To proceed, please choose an option from below:",
            font=subheading_font,
            fg="red"
        )
        self.subheading.pack(pady=5)


        #Create an account button style 
        self.open_account_button = tk.Button(
            self.master,
            #open account button text
            text="1. Open an Account",
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            command=self.open_account
        )
        self.open_account_button.pack(pady=5)

        #Login button style 
        self.login_button = tk.Button(
            self.master,
            #log in to account button text 
            text="2. Login to My Account",
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            command=self.login
        )
        self.login_button.pack(pady=5)

        # Check user balance button style 
        self.check_balance_button = tk.Button(
            self.master,
            #Check balance button text 
            text="3. Check my Balance",
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            command=self.check_balance
        )
        self.check_balance_button.pack(pady=5)

        # Transfer funds button style 
        self.transfer_funds_button = tk.Button(
            self.master,
            #Transfer funds button text 
            text="4. Transfer Funds",
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            command=self.transfer_funds
        )
        self.transfer_funds_button.pack(pady=5)

        # Exit the system button style 
        self.exit_button = tk.Button(
            self.master,
            #Exit system button text 
            text="5. Exit the application",
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            command=self.exit_app
        )
        self.exit_button.pack(pady=5)

    #Functions to creat/opne an account 
    def open_account(self):
        #user input 
        name = simpledialog.askstring("Input", "What is your name:")
        address = simpledialog.askstring("Input", "Please enter your address:")
        contact_email = simpledialog.askstring("Input", "What is your email address:")
        account_type = simpledialog.askstring("Input", "Enter account type (savings/current/mortgage):")
        #Saves new customer details
        customer = self.bank.add_customer(name, address, contact_email)
        #Creates a unique number for the user 
        account_number = self.bank.generate_account_number()
        #Amount in each account when created 
        initial_balance = 100
        #Creates cutomer account 
        customer.create_account(account_type, account_number, initial_balance)
        #Message box pop up to verify account has been created 
        messagebox.showinfo("Account Created", f"Your account has been created. Your Account Number is: {account_number}. Please save this number to log in to your account!")

    #Functions to manage the login for users with account number 
    def login(self):
        #Asks user to enter the number generated 
        account_number = simpledialog.askstring("Input", "Please input your account number:")
        #Look for the customer related to the account number
        customer = self.bank.find_customer_by_account(account_number)

        if customer:
            #If successful, show message box of successful message 
            messagebox.showinfo("Login has been Successful", f"Welcome {customer.name}!")
        else:
            #If unnsuccessful, show message box of error message
            messagebox.showerror("Error", "Unfortunately, the account has not been found.")

    #Functions to check account balance of the customer 
    def check_balance(self):
        #User Input for account number 
        account_number = simpledialog.askstring("Input", "Please input your account number:")
        #Finds customer related to the account number 
        customer = self.bank.find_customer_by_account(account_number)
        #If customer found display message box that shows the account balance 
        if customer:
            balances = "\n".join(f"Your account balance is: £{account.get_balance()}" for account in customer.accounts)
            messagebox.showinfo("Account Balance", balances)
            #Notify throught error message box when account not found 
        else:
            messagebox.showerror("Error", "The account has not been found.")

    #Functions to transfer funds through accounts 
    def transfer_funds(self):
        #user input of sender account 
        from_account_number = simpledialog.askstring("Input", "Please input your account number:")
        #User input of receiver account 
        to_account_number = simpledialog.askstring("Input", "Please input the receiver's account number:")
        
        try:
            #User input for amount to transfer (float number like 50)
            amount = float(simpledialog.askstring("Input", "Please input the amount you would like to transfer: "))
        except ValueError:
            #Dislpalys error message box if wrong number or input is entered 
            messagebox.showerror("Invalid Input", "Invalid number has been entered. Please try again.")
            return
        
        #Check for the account of the sender
        sender = self.bank.find_customer_by_account(from_account_number)
        #Check for the account of the receiver 
        receiver = self.bank.find_customer_by_account(to_account_number)
        
        #verify the sender and and receiver accounts have been found in Accounts 
        if sender and receiver:
            #Finds the sender's account number in Accounts 
            from_account = next((acc for acc in sender.accounts if acc.account_number == from_account_number), None)
            #Finds the reciever's account number 
            to_account = next((acc for acc in receiver.accounts if acc.account_number == to_account_number), None)
            #Verify that there is enough in senders account to transfer 
            if from_account and to_account:
                if from_account.get_balance() >= amount:
                    #Withdraws the given amount from the senders account 
                    from_account.withdraw(amount)
                    #Puts the amount into the receivers account 
                    to_account.deposit(amount)

                     #Displays success message in a message box once done
                    messagebox.showinfo("The Transfer is Successful", f"You have transferred £{amount} from {from_account_number} to {to_account_number}.")
                else:
                    #if insufficient balance, it displays an error message box with unssuccesful message
                    messagebox.showerror("The Transfer has Failed", "Unfortunately, the sender's account balance is insufficient.")
            else:
                #If accounts have not been found, it displays a message box with error message 
                messagebox.showerror("Error", "Either one or both accounts have not been located.")
        
    #Functions to exit the application 
    def exit_app(self): 
        #Displays a message box with the following message
        messagebox.showinfo("Goodbye", "Thank you for using MyBank. Goodbye! Hope to see you soon.")
        self.master.quit()

#Functions to run the application 
if __name__ == "__main__":
    #executes the main window 
    root = tk.Tk()
    #sets up the application 
    app = ConsoleBankingApp(root)
    #Handles the loop of the main event 
    root.mainloop()