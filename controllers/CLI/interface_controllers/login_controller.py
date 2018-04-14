import getpass
import hashlib
from views.CLI.cli_interface import LoginInterface
from models.employee_model import EmployeeModel
from models.customer_model import CustomerModelForCLI

class LoginController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.login_interface = LoginInterface()
        self.login()

    def login(self):
        while 1:
            username = input('Username: ')
            password = getpass.getpass(prompt='Password: ')
            self.main_controller.employee_model = EmployeeModel('./models/data/employees.json', username, hashlib.sha256(str.encode(password)).hexdigest())
            self.main_controller.employee_model._load_employee()
            if self.main_controller.employee_model.employee_id != None:
                self.main_controller.customer_model = CustomerModelForCLI('./models/data/customers.json')
                self.main_controller.change_controller('main_menu')
                break
            else:
                while 1:
                    input('ERROR! The information you entered is incorrect. Please try again.')
                    break
                self.main_controller.logout()
