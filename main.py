
import logging


logging.basicConfig(filename='employee.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info('created Employee:{} -{}'.format(self.fullname,self.email))
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)







emp_1=Employee('john','smith')
emp_2=Employee('johhny','smithon')
