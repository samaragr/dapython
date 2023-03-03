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
