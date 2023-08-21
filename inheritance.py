
class Employee:

    raise_amount = 1.04

    def __init__(self, firstname, lastname, age, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary
    
    def fullName(self):
        # return self.firstname + ' ' + self.lastname
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


class Developer(Employee):
    # Developer can their own raise percent
    raise_amount = 1.10

    # developer class can have it's own constructor
    def __init__(self, firstname , lastname, age, salary, prog_lang):
        super().__init__(firstname, lastname, age, salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstname , lastname, age, salary, employees=None):
        super().__init__(firstname, lastname, age, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    
    def print_employees(self):
        for emp in self.employees:
            print(' --> ', emp.fullName())


# MAIN ROUTINE STARTS HERE

emp1 = Employee('Kunal', 'Patil', 47, 5000)
emp2 = Employee('Kunal2', 'Patil2', 47, 6000)

dev1 = Developer('Alice', 'Wonder', 22, 5000, 'Python')
dev2 = Developer('Jane', 'Doe', 34, 6000, 'Java')

mgr1 = Manager('John', 'Smith', 56, 11000, [dev1, dev2])

print('Alice salary: {}'.format(dev1.salary))
dev1.apply_raise()
print('Alice salary after raise: {}'.format(dev1.salary))

# print(help(Developer))

print('Alice full name {}'.format(dev1.fullName()))

print(isinstance(dev1, Developer))

print(issubclass(Manager, Employee))