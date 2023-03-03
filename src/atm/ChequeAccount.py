from Account import Account


class ChequeAccount(Account):
    def __init__(self, owner_id, acct_no, balance):
        super().__init__(owner_id, acct_no, balance)
        self.type = "Cheque"
