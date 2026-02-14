from savingAccount import SavingAccount
from checkingAccount import CheckingAccount

def main():
    #Checking Accounts 
    checkAccount_1 = CheckingAccount("John", 5360, 100, 11222687, 43219832 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number
    checkAccount_2 = CheckingAccount("Sam", 6350, 100, 11222690, 43219842 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number

    #Saving Accounts 
    savingAccount_1 = SavingAccount("John", 7500, 200, 11232612, 44019123) # self, customer_name, current_balance, minimum_balance, account_number, routing_number
    savingAccount_2 = SavingAccount("Sam", 8700, 200, 112326825, 44019247) # self, customer_name, current_balance, minimum_balance, account_number, routing_number