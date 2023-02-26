import os
import csv
class ATM:
    def __init__(self):
        self.users = []
        self.accounts = []
        # for every user create an instance of User
        with open(os.path.join(os.getcwd(), '../data/UserInfo.txt')) as load_file:
            reader = csv.DictReader(load_file, delimiter=",")
            for row in reader:
                new_user = User(row["FirstName"], row["Surname"], row["Mobile"], row["AccountOwnerID"])
                self.users.append(new_user)

        raw_accounts = []
        with open(os.path.join(os.getcwd(), '../data/OpeningAccountsData.txt')) as load_file:
            for line in load_file:
                line = line.replace("|||", "|")
                raw_accounts.append(line)

        reader = csv.DictReader(raw_accounts, delimiter="|")
        for row in reader:
            if row["AccountType"] == "Cheque":
                new_account = ChequeAccount(row["AccountOwnerID"], row["AccountNumber"], row["OpeningBalance"])
            if row["AccountType"] == "Saving":
                new_account = SavingsAccount(row["AccountOwnerID"], row["AccountNumber"], row["OpeningBalance"])
            self.accounts.append(new_account)

    # iterate through users
    ## for each user check id matches input id
    ### if id matches set that as the current user and break loop
    def run(self):
        choice = None
        while choice != "q":
            print("Please enter your User ID:")
            userid = input()
            current_user = None
            for user in self.users:
                if userid == user.id:
                    current_user = user
                    break
                    # Handle if ID is invalid

            user_accounts = self.get_accounts(current_user)
            welcome_msg = """
    Welcome %s. Please enter an Option
        1 For Deposit
        2 For Withdraw
        3 For Balance
        q To Quit"""
            print(welcome_msg % (str(current_user)))
            choice = input()
            if choice == "1":
                self.deposit(user_accounts)
            elif choice == "2":
                self.withdraw(user_accounts)
            elif choice == "3":
                self.balance(user_accounts)
            elif choice != "q":
                print ("Wrong input. ") ## fix error
        if choice == "q":

            # print(self.accounts)


            for account in user_accounts:
                print(str(account) + ":\t$" + str(account.balance))

            # write the result to your file OpeningAccountsData.txt
            self.save_accounts()

    def get_accounts(self, user):
        user_accounts = []
        for account in self.accounts:
            if user.id == account.owner:
                user_accounts.append(account)
        return user_accounts

    def save_accounts(self):
        # get current acct balances
        # open file for writing
        # write header
        # for each acct, write info
        with open(os.path.join(os.getcwd(), '../data/OpeningAccountsData.txt'), "w") as load_file:
            load_file.write("AccountOwnerID|||AccountNumber|||AccountType|||OpeningBalance")
            for account in self.accounts:
                load_file.write("\n{0}|||{1}|||{2}|||{3}".format(account.owner,account.number, account.type, account.balance))


    def deposit(self, accounts):

        # print accounts
        # allow user to choose account
        # prompt user to enter deposit amt
        # add deposited amount to balance

        deposit_msg = "Which account do you wish to deposit to:"
        n = 1
        for account in accounts:
            account_option = "\n\t{0} for {1}".format(n, str(account))
            n += 1
            deposit_msg += account_option
        print(deposit_msg)
        account_choice = accounts[int(input())-1]
        # handle errors
        print("How much do you wish to deposit?")
        deposit_amount = float(input())
        account_choice.balance += deposit_amount


    def withdraw(self, accounts):

        # print accounts
        # allow user to choose account
        # prompt user to enter withdrawal smt
            #check withdrawal amt is not greater than current balance
            # remove withdrawn amount from balance

        withdrawal_msg = "Which account do you wish to withdraw from:"
        n = 1
        for account in accounts:
            account_options = "\n\t {0} for {1}".format(n, str(account))
            withdrawal_msg += account_options
            n += 1
        print(withdrawal_msg)
        account_choice = accounts[int(input())-1]
        print("How much do you wish to withdraw? Balance = $" + str(account_choice.balance))
        withdrawal_amount = float(input())
        if withdrawal_amount > account_choice.balance:
            # return error message and go back to start
            print("Error: Wrong input. Amount entered (${0}) is greater than amount in account".format(withdrawal_amount))
        else:
            account_choice.balance -= withdrawal_amount
        print("Your new balance for " + str(account_choice) + " is $" + str(account_choice.balance))

    def balance(self, accounts):
    # print accounts
    # allow user to choose account
    # display current balance
        n = 1
        balance_msg = "Which account to you wish to view?"
        for account in accounts:
            account_options = "\n\t {0} for {1}".format(n, str(account))
            balance_msg += account_options
            n += 1
        print(balance_msg)
        user_input = input()
        account_choice = accounts[int(user_input)-1]
        print("Current balance for account " + str(account_choice) + ": $" + str(account_choice.balance))






class User:
    def __init__(self, first_name, last_name, mobile, owner_id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = owner_id
        self.mobile = mobile

    # translating object into str for printing (repr needed for lists)
    def __str__(self):
        return self.first_name + " " + self.last_name
    def __repr__(self):
        return self.__str__()
class Account:
    def __init__(self, owner_id, acct_no, balance):
        self.owner = owner_id
        self.number = acct_no
        self.balance = float(balance)
    def __str__(self):
        return self.number + " (" + self.type + ")"
    def __repr__(self):
        return self.__str__()


class ChequeAccount(Account):
    # translating object into str for printing (repr needed for lists)
    def __init__(self, owner_id, acct_no, balance):
        super().__init__(owner_id, acct_no, balance)
        self.type = "Cheque"


class SavingsAccount(Account):
    # translating object into str for printing (repr needed for lists)
    def __init__(self, owner_id, acct_no, balance):
        super().__init__(owner_id, acct_no, balance)
        self.type = "Saving"


ourATM = ATM()
ourATM.run()



