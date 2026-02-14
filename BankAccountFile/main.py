from savingAccount import SavingAccount
from checkingAccount import CheckingAccount

def main():
    #Checking Accounts 
    checkAccount_1 = CheckingAccount("John", 5360, 100, 11222687, 43219832, 500 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit
    checkAccount_2 = CheckingAccount("Sam", 6350, 100, 11222690, 43219842, 600 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit

    #Saving Accounts 
    savingAccount_1 = SavingAccount("John", 2500, 50, 11232612, 44019123, 0.01) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate
    savingAccount_2 = SavingAccount("Sam", 8700, 200, 112326825, 44019247, 0.06) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate


    print("Scenario John opens a checking account and withdraws 200")
    checkAccount_1.print_customer_information()

    checkAccount_1.withdraw(200)                    #withdraw $x
    checkAccount_1.transfer(100)                    #testing transfer
    checkAccount_1.transfer(550)                    #testing transfer_limit, should fail

    checkAccount_1.print_customer_information()


    print("\nScenario testing Sam's checking account")
    checkAccount_2.print_customer_information()

    checkAccount_2.transfer(500)                    #testing transfer
    checkAccount_2.transfer(650)                    #testing transfer_limit, should fail
    checkAccount_2.withdraw(6300)                   #should fail as not enough for minimum_balance


    print("\n Saving account Interest testing")

    savingAccount_1.print_customer_information()
    savingAccount_1.add_interest()

    savingAccount_2.print_customer_information()
    savingAccount_2.add_interest()


if __name__ == "__main__":
    main()






