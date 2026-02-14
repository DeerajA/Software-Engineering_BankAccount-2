from savingAccount import SavingAccount
from checkingAccount import CheckingAccount

def main():
    
    #Checking Accounts 
    checkAccount_1 = CheckingAccount("John", 5360, 100, 11222687, 43219832, 500 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit
    checkAccount_2 = CheckingAccount("Sam", 6350, 100, 11222690, 43219842, 600 ) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit

    #Saving Accounts 
    savingAccount_1 = SavingAccount("John", 2500, 50, 11232612, 44019123, 0.01) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate
    savingAccount_2 = SavingAccount("Sam", 8700, 200, 112326825, 44019247, 0.06) # self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate


    print("\nScenario 1: John opens a checking account and withdraws 200")
    print("<------------------------------------------------------------------------------>\n")
    checkAccount_1.print_customer_information()

    print("Withdrawing 200: ")
    checkAccount_1.withdraw(200)                    #withdraw $x
    print("\Transfering 100: ")
    checkAccount_1.transfer(100)                    #testing transfer
    print("\nTransfering 550: ")
    checkAccount_1.transfer(550)                    #testing transfer_limit, should fail

    print("\nAfter testing: ")
    checkAccount_1.print_customer_information()


    print("\nScenario 2: testing Sam's checking account")
    print("<------------------------------------------------------------------------------> \n")
    checkAccount_2.print_customer_information()
    print("\n")

    print("Transfering 500: ")
    checkAccount_2.transfer(500)                    #testing transfer
    print("\nTransfering 650: ")
    checkAccount_2.transfer(650)                    #testing transfer_limit, should fail
    print("\nWithdrawing 6300: ")
    checkAccount_2.withdraw(6300)                   #should fail as not enough for minimum_balance


    print("\nSaving account Interest testing")
    print("<------------------------------------------------------------------------------>")

    print("Checking Instance 1: \n")
    savingAccount_1.print_customer_information()
    
    print("\n")
    savingAccount_1.add_interest()
    savingAccount_1.print_customer_information()
    print("\n")

    print("Checking Instance 2: \n")
    savingAccount_2.print_customer_information()
    
    print("\n")
    savingAccount_2.add_interest()
    savingAccount_2.print_customer_information()
    print("\n")


if __name__ == "__main__":
    main()






