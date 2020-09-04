

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




class Developer(Employee):
    raise_amount = 2.04


    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        


dev_1 = Developer('venky','raj',10000, 'Python')
dev_2 = Developer('ramu','ra0',40000, 'java')


mgr_1 = Manager('amu','ra0',90000, [dev_1])
print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))



#mgr_1. add_emp(dev_2)
#mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()
#print(mgr_1.email)
#print(dev_1.prog_lang)
#print(dev_2.email)
