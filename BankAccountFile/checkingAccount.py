from BankAccountFile.BankAccountPart2 import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):

        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

        self.transfer_limit = transfer_limit