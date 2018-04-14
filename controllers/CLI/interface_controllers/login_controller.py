import getpass
import hashlib
from views.CLI.cli_interface import LoginInterface
from models.employee_model import EmployeeModel
from models.customer_model import CustomerModelForCLI

class LoginController():
    '''
        Controller class for the LoginInterface view.
        Initialize customer and employee model for the main controller

        Attributes:
            main_controller: a reference to the main controller object
            login_interface: the view this class controls

        Methods:
            login: log user into the system and create appropriate models for the main controller
    '''
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
                self.main_controller.reset_session()
                break
            else:
                while 1:
                    input('ERROR! The information you entered is incorrect. Please try again.')
                    break
                self.main_controller.logout()
