import os
import csv


class ATM:
    # Loads data from data directory into list
    def __init__(self):
        self.users = []
        self.accounts = []
        self.transacting_account = None
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
        new_account = None
        for row in reader:
            if row["AccountType"] == "Cheque":
                new_account = ChequeAccount(row["AccountOwnerID"], row["AccountNumber"], row["OpeningBalance"])
            if row["AccountType"] == "Saving":
                new_account = SavingsAccount(row["AccountOwnerID"], row["AccountNumber"], row["OpeningBalance"])
            self.accounts.append(new_account)

    # Runs the ATM program
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
            if current_user is None:
                print("Wrong input. Invalid user ID")
                continue

            user_accounts = self.get_user_accounts(current_user)
            welcome_msg = """
    Welcome {}. Please enter an Option
        1 For Deposit
        2 For Withdraw
        3 For Balance
        q To Quit""".format(str(current_user))
            print(welcome_msg)
            choice = input()
            if choice == "1":
                self.deposit(user_accounts)
            elif choice == "2":
                self.withdrawal(user_accounts)
            elif choice == "3":
                self.balance(user_accounts)
            elif choice != "q":
                print("Wrong input. Invalid transaction option")
        if choice == "q":
            for account in user_accounts:
                print(str(account) + ":\t$" + str(account.balance))
            self.save_accounts()

    # Writes new account info back to file in original format
    def save_accounts(self):
        with open(os.path.join(os.getcwd(), '../data/OpeningAccountsData.txt'), "w") as load_file:
            load_file.write("AccountOwnerID|||AccountNumber|||AccountType|||OpeningBalance")
            for account in self.accounts:
                load_file.write("\n{0}|||{1}|||{2}|||{3}".format
                                (account.owner, account.number, account.type, account.balance))

    # returns list of accounts associated with current user
    def get_user_accounts(self, user):
        user_accounts = []
        for account in self.accounts:
            if user.id == account.owner:
                user_accounts.append(account)
        return user_accounts

    # Prints out all account options
    def get_account_options(self, accounts):
        account_options = ""
        n = 1
        for account in accounts:
            account_option = "\n\t {0} for {1}".format(n, str(account))
            account_options += account_option
            n += 1
        return account_options

    def deposit(self, accounts):
        account_options = self.get_account_options(accounts)
        deposit_msg = "Which account do you wish to deposit to:" + account_options
        print(deposit_msg)
        account_choice = int(input()) - 1
        # self.transacting_account = accounts[int(input()) - 1]
        if account_choice > len(accounts) - 1 or account_choice < 0:
            print("Wrong input. Invalid account choice")
        else:
            self.transacting_account = accounts[account_choice]
            self.deposit_amount()

    def deposit_amount(self):
        print("How much do you wish to deposit?")
        deposit_amount = float(input())
        self.transacting_account.balance += deposit_amount

    def withdrawal(self, accounts):
        account_options = self.get_account_options(accounts)
        withdrawal_msg = "Which account do you wish to withdraw from:" + account_options
        print(withdrawal_msg)
        account_choice = int(input()) - 1
        if account_choice > len(accounts) - 1 or account_choice < 0:
            print("Wrong input. Invalid account choice")
        else:
            self.transacting_account = accounts[account_choice]
            self.withdrawal_amount()

    def withdrawal_amount(self):
        print("How much do you wish to withdraw? Balance = $" + str(self.transacting_account.balance))
        withdrawal_amount = float(input())
        if withdrawal_amount > self.transacting_account.balance:
            print("Error: Wrong input. Amount entered (${0}) is greater than amount in account".format
                  (withdrawal_amount))
        else:
            self.transacting_account.balance -= withdrawal_amount
        print("Your new balance for " + str(self.transacting_account) + " is $" + str(self.transacting_account.balance))

    def balance(self, accounts):
        account_options = self.get_account_options(accounts)
        balance_msg = "Which account to you wish to view?" + account_options
        print(balance_msg)
        account_choice = int(input()) - 1
        if account_choice > len(accounts) - 1 or account_choice < 0:
            print("Wrong input. Invalid account choice")
        else:
            transacting_account = accounts[account_choice]
            print("Current balance for account " + str(transacting_account) + ": $" + str(transacting_account.balance))


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
    def __init__(self, owner_id, acct_no, balance):
        super().__init__(owner_id, acct_no, balance)
        self.type = "Cheque"


class SavingsAccount(Account):

    def __init__(self, owner_id, acct_no, balance):
        super().__init__(owner_id, acct_no, balance)
        self.type = "Saving"


ourATM = ATM()
ourATM.run()
