class BankAccount:
    # This is the class attributes
    BankTitle = "Bank Title"

    # This is the Instance Attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # The deposit method that allows users to add to the current balance
    def deposit(self, amount):
        self.current_balance += amount

    # The withdraw method that allows users to withdraw money if they have enough money left
    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
        else:
            print("You can't withdraw money")

    # This prints all the information about the customer including their name, current balance, and the title of their bank
    def print_customer_information(self):
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Bank Title" + self.BankTitle)

# These are the two accounts that I tested with
Instance1 = BankAccount("John", 100, 100)
Instance2 = BankAccount("Alex", 200, 100)

# This shouldn't be allowed to happen, so I am testing if it does or not
Instance1.withdraw(900)

# This should be allowed to happen, so I am testing if it does or not
Instance2.deposit(200)

# I am testing the printing to make sure that everything worked correctly
Instance1.print_customer_information()
Instance2.print_customer_information()