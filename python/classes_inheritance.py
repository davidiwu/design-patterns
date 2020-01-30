
class Employee(object):

    # class variable
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        #self.email = first +'.' +last +'@company.com'
        Employee.num_of_emps += 1
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, lang = emp_str.split('-')
        return cls(first, last, pay, lang)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):   # 如果不需要访问self，和cls，就可以用static method
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    # dunder / magic function
    def __repr__(self): # for debugging
        return f'Employee({self.first},{self.last},{self.pay})'

    def __str__(self):  # readable representation of this class
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


#print(help(Developer))
print(Employee.num_of_emps)
emp_1 = Employee('david', 'wu', 50000)
print(emp_1.fullname)
print(emp_1.email)
emp_1.fullname = 'John Smith'
print('emp_1: ', emp_1)
print(repr(emp_1))
print(str(emp_1))


emp_2 = Developer.from_string('test-user-60000-Python')
print(Employee.num_of_emps)

print('emp_1 + emp_2: ', emp_1 + emp_2)
print('emp_1.raise_amount: ', emp_1.raise_amount)
print('emp_2.raise_amount: ', emp_2.raise_amount)
print(emp_1.__dict__)
print(emp_2.__dict__)


#print(Employee.__dict__)
# print(dir(Employee))
# print(dir(emp_1))
print(emp_1.fullname)
print(Employee.fullname)  # why fullname takes one argument self.

Employee.set_raise_amt(1.05)
print('Employee.raise_amount: ', Employee.raise_amount)
print('emp_1.raise_amount: ', emp_1.raise_amount)
print('emp_2.raise_amount: ', emp_2.raise_amount)

