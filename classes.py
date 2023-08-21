class Employee:

# Class level variable
    emp_count = 0

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        Employee.emp_count += 1
    
    def fullName(self):
        # return self.firstname + ' ' + self.lastname
        return '{} {}'.format(self.firstname, self.lastname)

    @classmethod
    def fromString(cls, str):
        (fname, lname, age) = str.split('-')
        return cls(fname, lname, age)

    @staticmethod
    def isWorkDay(day):
        if day == 5 or day == 6:
            return False
        else:
            return True

    # THESE ARE SPECIAL DUNDER METHODS 
    # used by python for various operations
    # use by dev to debug
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.firstname, self.lastname, self.age)

    # toString() method
    def __str__(self):
        return "{} {} - {}".format(self.firstname, self.lastname, self.age)

    # used when performing addition on employees
    def __add__(self, other):
        return self.age +  other.age

# print(Employee.__dict__)
print('Employee count {}'.format(Employee.emp_count))
emp1 = Employee('Kunal', 'Patil', 47)
emp2 = Employee('Kunal2', 'Patil2', 47)
print('Employee count {}'.format(Employee.emp_count))
print(emp1.emp_count)

# print(emp1.firstname)
# print(emp1.age)
# print(emp1.fullName())

# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)

emp3 = Employee.fromString('john-smith-32')
print(emp3.firstname)

print(Employee.isWorkDay(3))

print(emp1) # uses __str__ to print object info
print(repr(emp1))
print(str(emp1))

# calls special __add___ dunder method on the employee class
print(emp1 + emp2)
