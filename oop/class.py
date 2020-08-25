" In this we will learn of Regular method(instance),calssmethod,Staticmethod"


class Employee():

    raise_amount = 1.04
    no_of_emp = 0
   
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.no_of_emp += 1


    def fullname(self):
        return '{} {}'.format(self.first,self.last)

   

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """ class methods """
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    
    """ staticmethod don't take instance or class of the first argument. """
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True





#print(Employee.no_of_emp)
emp_1 = Employee('venky','raj',10000)
emp_2 = Employee('vicky','raj',20000)
#Employee.set_raise_amount(1.05)
import datetime
my_date = datetime.date(2020, 3, 07)

print(Employee.is_workday(my_date))




#emp_str_1 = 'venky-raj-12000'
#emp_str_2 = 'divya-raj-14000'

#new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)
#print(new_emp_1.pay)

#print(emp_1.email)
#print(emp_1.pay)
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
#print(emp_1.raise_amount)
#print(Employee.__dict__)
#print(Employee.no_of_emp)


