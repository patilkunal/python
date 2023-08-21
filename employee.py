class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@nowhere.com'.format(self.firstname, self.lastname)
    @property
    def fullName(self):
        # return self.firstname + ' ' + self.lastname
        return '{} {}'.format(self.firstname, self.lastname)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.firstname, self.lastname, self.age)
