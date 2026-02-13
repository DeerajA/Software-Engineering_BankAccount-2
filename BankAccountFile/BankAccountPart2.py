class BankAccount:
    # This is the class attributes
    BankTitle = "Bank Title"

    # This is the Instance Attributes
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number

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