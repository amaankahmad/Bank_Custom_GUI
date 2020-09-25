# Stores details about the amount
# Parent Class: User
class User():
    # Holds details about each user
    def __init__(self, name, age, gender):
        """" 
        Inputs: 
        name -> String, name for each user
        age -> Int, age for each user
        gender -> String, either Male / Female
        """
        self.name = name
        self.age = age
        self.gender = gender

    # Has a function to show user details
    def show_user_details(self):
        """
        Function shows the user details 
        """
        print("Personal Details:")
        print(" User Name:", self.name)
        print(" User Age:", self.age)
        print(" User Gender:", self.gender)

# Child Class: Bank
class Bank(User):
    # Holds details about each user
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender) # Invert from superclass
        self.balance = 0 # Stores details about the account balance
    
    # Allows for deposits, withdraws, view_balance
    def deposit(self, amount):
        self.balance += amount # Changes applied to balance
        print("Account balance has been updated to: £"+str(self.balance))
    def deposit(self, amount):
        if amount > self.balance:
            print("Insufficient funds... Balance available is: £"+str(self.balance))
        else:
            self.balance -= amount # Changes applied to balance
            print("Account balance has been updated to: £"+str(self.balance))
    def view_balance(self):
        self.show_user_details()
        print(" Account balance: £"+str(self.balance))
