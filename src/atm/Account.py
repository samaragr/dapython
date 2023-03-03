class Account:
    def __init__(self, owner_id, acct_no, balance):
        self.owner = owner_id
        self.number = acct_no
        self.balance = float(balance)
        self.type = 'Unspecified'

    def __str__(self):
        return self.number + " (" + self.type + ")"

    def __repr__(self):
        return self.__str__()
