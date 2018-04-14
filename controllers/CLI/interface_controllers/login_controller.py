import getpass
import hashlib
from views.CLI.cli_interface import LoginInterface
from models.employee_model import EmployeeModel
from models.customer_model import CustomerModelForCLI

class LoginController():
    '''
    Login for the admin class. This is the first view's controller.
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.login_interface = LoginInterface()
        self.login()

    def login(self):
        '''
        Asks for user name and password, hashes the PIN, checks if matches in the json file for employees.
        :return:None
        '''
        while 1:
            username = input('Username: ')
            password = getpass.getpass(prompt='Password: ')
            self.main_controller.employee_model = EmployeeModel('./models/data/employees.json', username, hashlib.sha256(str.encode(password)).hexdigest())
            self.main_controller.employee_model._load_employee()
            if self.main_controller.employee_model.employee_id != None:
                self.main_controller.customer_model = CustomerModelForCLI('./models/data/customers.json')
                self.main_controller.reset_session()
                break
            else:
                while 1:
                    input('ERROR! The information you entered is incorrect. Please try again.')
                    break
                self.main_controller.logout()
