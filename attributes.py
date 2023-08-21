class Employee:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    @property
    def fullName(self):
        # return self.firstname + ' ' + self.lastname
        return '{} {}'.format(self.firstname, self.lastname)
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

emp1 = Employee('Kunal', 'Patil', 47)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.fullName)

emp1.fullName = 'John Smith'
print(emp1.firstname)
print(emp1.lastname)
print(emp1.fullName)
