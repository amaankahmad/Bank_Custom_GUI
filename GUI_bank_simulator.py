from tkinter import *
import os
from PIL import ImageTk, Image

# Main screen
master = Tk()
master.title('Banking App')

# Functions 
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    #print(all_accounts)

    #print("Registration complete")

    if name == '' or age == '' or gender == '' or password == '':
        notif.config(fg = 'red', text = "*All fields are required*")
        return

    # Prevents duplicate account files, validation step
    for name_check in all_accounts:
        if name in all_accounts:
            notif.config(fg = "red", text = "Account already exists")
        else: 
            new_file = open(name.strip(), "w")
            new_file.write(name.strip()+'\n')
            new_file.write(age.strip()+'\n')
            new_file.write(gender.strip()+'\n')
            new_file.write(password.strip()+'\n')
            new_file.write('0')
            notif.config(fg = 'green', text = "Account created")


def register():
    # Create global variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif

    # Initialise variables
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    # Create Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    # Create labels
    Label(register_screen, text = 'Please enter your details below to register:', font = ('Calibri', 12)).grid(row = 0, sticky=N, pady=10)
    Label(register_screen, text = 'Name:', font = ('Calibri', 12)).grid(row = 1, sticky=W)
    Label(register_screen, text = 'Age:', font = ('Calibri', 12)).grid(row = 2, sticky=W)
    Label(register_screen, text = 'Gender:', font = ('Calibri', 12)).grid(row = 3, sticky=W)
    Label(register_screen, text = 'Password:', font = ('Calibri', 12)).grid(row = 4, sticky=W)
    notif = Label(register_screen, font = ('Calibri', 12))
    notif.grid(row = 6, sticky = N, pady = 10)

    # Create Entries
    Entry(register_screen, textvariable = temp_name).grid(row=1, column=1)
    Entry(register_screen, textvariable = temp_age).grid(row=2, column=1)
    Entry(register_screen, textvariable = temp_gender).grid(row=3, column=1)
    Entry(register_screen, textvariable = temp_password, show = "*").grid(row=4, column=1)

    # Create Buttons
    Button(register_screen, text = 'Register', command = finish_reg, font = ('Calibri', 12)).grid(row = 5, sticky=N, pady=10)


def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    # Check if login data is correct
    for name in all_accounts:
        # Check if name exists
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[3]
            # Check if password is correct
            if login_password == password:
                # Open account dashboard if login data is correct
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Account Dashboard')
                # Create account dashboard labels
                Label(account_dashboard, text = 'Account Dashboard:', font = ('Calibri', 12)).grid(row = 0, sticky=N, padx=10)
                Label(account_dashboard, text = 'Welcome, '+name, font = ('Calibri', 12)).grid(row = 1, sticky=N, padx=5)
                # Buttons 
                Button(account_dashboard, text = "Personal Details", font = ('Calibri', 12), width = 30, command = personal_details).grid(row = 2, sticky=N, padx=10)
                Button(account_dashboard, text = "Deposit", font = ('Calibri', 12), width = 30, command = deposit).grid(row = 3, sticky=N, padx=10)
                Button(account_dashboard, text = "Withdraw", font = ('Calibri', 12), width = 30, command = withdraw).grid(row = 4, sticky=N, padx=10)
                Button(account_dashboard, text = "Change Password",font = ('Calibri', 12), command = change_password).grid(row = 5, sticky = N, pady = 10)
                return
            else: 
                login_notif.config(fg = "red", text = "Password Incorrect.")
                return
    login_notif.config(fg = "red", text = "No Account Found.")


def personal_details():
    # Open account file
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    name = user_details[0]
    age = user_details[1]
    gender = user_details[2]
    balance = user_details[4]

    # Create personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")

    # Create labels
    Label(personal_details_screen, text = "Personal Details ", font = ('Calibri', 12)).grid(row = 0, sticky = N, pady=10)
    Label(personal_details_screen, text = "Name: "+name, font = ('Calibri', 12)).grid(row = 1, sticky = W, padx=5)
    Label(personal_details_screen, text = "Age: "+age, font = ('Calibri', 12)).grid(row = 2, sticky = W, padx=5)
    Label(personal_details_screen, text = "Gender: "+gender, font = ('Calibri', 12)).grid(row = 3, sticky = W, padx=5)
    Label(personal_details_screen, text = "Balance: £"+balance, font = ('Calibri', 12)).grid(row = 4, sticky = W, padx=5)

    # Create Button
    Button(personal_details_screen, text = "Change Password",font = ('Calibri', 12), command = change_password).grid(row = 5, sticky = N, pady = 5)


def change_password():
    # Create Variables
    global new_password
    global password_notif
    global current_password_label

    new_password = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    current_password = user_details[3]

    # Create Change Password Screen
    change_pass_screen = Toplevel(master)
    change_pass_screen.title('Change Password')

    # Create Labels
    Label(change_pass_screen, text = "Change Password ", font = ('Calibri', 12)).grid(row = 0, sticky = N, pady=10)
    current_password = Label(change_pass_screen, text = "Current Password: ", font = ('Calibri', 12)).grid(row = 1, stick = W)
    current_password_label = Label(change_pass_screen, text = current_password, font = ('Calibri', 12))
    current_password_label.grid(row = 1, sticky = W, column = 1)
    Label(change_pass_screen, text = "New Password: ", font = ('Calibri', 12)).grid(row = 2, sticky = W)
    password_notif = Label(change_pass_screen, font = ('Calibri', 12))
    password_notif.grid(row = 4, sticky = N, pady = 5)

    # Create Entry
    Entry(change_pass_screen, textvariable = new_password).grid(row = 2, column = 1)

    # Create Buttons
    Button(change_pass_screen, text = "Change Password",font = ('Calibri', 12), command = update_password).grid(row = 3, sticky = N, pady = 5)


def update_password():
    # Open file
    file = open(login_name, 'r+')
    file_data = file.read()
    user_details = file_data.split('\n')
    current_password = user_details[3]
    # Verify if password is the same
    if new_password.get() == current_password:
        current_password_label.config(fg = 'black', text = new_password.get())
        password_notif.config(fg = 'red', text = "Password already in use")
        return
    if new_password.get() == "":
        password_notif.config(fg = "red", text = "Invalid Password")
        return
    
    updated_password = new_password.get()
    file_data = file_data.replace(current_password, updated_password)
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_password_label.config(fg = 'black', text = updated_password)
    password_notif.config(fg = 'green', text = 'Password Updated')    


def deposit():
    # Create Variables
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    balance = user_details[4]
    
    # Create Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')

    # Create Labels
    Label(deposit_screen, text = "Deposit", font = ('Calibri', 12)).grid(row = 0, sticky = N, pady=10)
    current_balance_label = Label(deposit_screen, text = "Current Balance: £" + balance, font = ('Calibri', 12))
    current_balance_label.grid(row = 1, sticky = W)
    Label(deposit_screen, text = "Amount: ", font = ('Calibri', 12)).grid(row = 2, sticky = W)
    deposit_notif = Label(deposit_screen, font = ('Calibri', 12))
    deposit_notif.grid(row = 4, sticky = N, pady = 5)

    # Create Entry
    Entry(deposit_screen, textvariable = amount).grid(row = 2, column = 1)

    # Create Buttons
    Button(deposit_screen, text = "Deposit",font = ('Calibri', 12), command = finish_deposit).grid(row = 3, sticky = N, pady = 5)


def finish_deposit():
    # Verify amount is valid
    if amount.get() == "":
        deposit_notif.config(fg = 'red', text = "Amount is required!")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(fg = "red", text = "Invalid Amount")
        return
    
    # Make changes
    file = open(login_name, 'r+')
    file_data = file.read()
    user_details = file_data.split('\n')
    current_balance = user_details[4]
    updated_balance = float(current_balance) + float(amount.get())
    updated_balance = format(updated_balance, '.2f')
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(fg = 'black', text = 'Current Balance: £'+str(updated_balance))
    deposit_notif.config(fg = 'green', text = 'Balance Updated')


def withdraw():
    # Create Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    balance = user_details[4]
    
    # Create withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')

    # Create Labels
    Label(withdraw_screen, text = "Withdraw", font = ('Calibri', 12)).grid(row = 0, sticky = N, pady=10)
    current_balance_label = Label(withdraw_screen, text = "Current Balance: £" + balance, font = ('Calibri', 12))
    current_balance_label.grid(row = 1, sticky = W)
    Label(withdraw_screen, text = "Amount: ", font = ('Calibri', 12)).grid(row = 2, sticky = W)
    withdraw_notif = Label(withdraw_screen, font = ('Calibri', 12))
    withdraw_notif.grid(row = 4, sticky = N, pady = 5)

    # Create Entry
    Entry(withdraw_screen, textvariable = withdraw_amount).grid(row = 2, column = 1)

    # Create Buttons
    Button(withdraw_screen, text = "Withdraw",font = ('Calibri', 12), command = finish_withdraw).grid(row = 3, sticky = N, pady = 5)


def finish_withdraw():
    # Verify amount is valid
    if withdraw_amount.get() == "":
        withdraw_notif.config(fg = 'red', text = "Amount is required!")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(fg = "red", text = "Invalid Amount")
        return

    # Make changes
    file = open(login_name, 'r+')
    file_data = file.read()
    user_details = file_data.split('\n')
    current_balance = user_details[4]
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(fg = "red", text = "Insufficient funds")
        return
    updated_balance = float(current_balance) - float(withdraw_amount.get())
    updated_balance = format(updated_balance, '.2f')
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(fg = 'black', text = 'Current Balance: £'+str(updated_balance))
    withdraw_notif.config(fg = 'green', text = 'Balance Updated')


def login():
    # Create global variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    # Initialise variables
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Create login screen
    login_screen = Toplevel(master)
    login_screen.title('Login')

    # Create Labels
    Label(login_screen, text = 'Login to your account', font = ('Calibri', 12)).grid(row = 0, sticky=N, pady=10)
    Label(login_screen, text = 'Username:', font = ('Calibri', 12)).grid(row = 1, sticky=N)
    Label(login_screen, text = 'Password:', font = ('Calibri', 12)).grid(row = 2, sticky=N)
    login_notif = Label(login_screen, font = ('Calibri', 12))
    login_notif.grid(row = 4, sticky=N)

    # Create Entries
    Entry(login_screen, textvariable = temp_login_name).grid(row = 1, column = 1, padx=5)
    Entry(login_screen, textvariable = temp_login_password, show = "*").grid(row = 2, column = 1, padx=5)

    # Create Buttons
    Button(login_screen, text = 'Login', command = login_session, width = 15, font = ('Calibri', 12)).grid(row = 3, sticky=W, pady=5, padx = 5)

# Image import
img = Image.open('bank.jpeg')
img = img.resize((300,300))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text = "Customer Banking Beta", font = ('Calibri', 14)).grid(row = 0, sticky = N, pady=10)
Label(master, text = "Secure Bank", font = ('Calibri', 12)).grid(row = 1, sticky = N)
Label(master, image = img).grid(row=2, sticky=N, pady=15)

# Buttons
Button(master, text = 'Register', font = ('Calibri', 12), width = 20, command=register).grid(row=3, sticky=N)
Button(master, text = 'Login', font = ('Calibri', 12), width = 20, command = login).grid(row=4, sticky=N, pady=10)

master.mainloop()