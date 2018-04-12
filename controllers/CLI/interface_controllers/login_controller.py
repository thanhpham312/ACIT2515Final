import getpass
from views.CLI.cli_interface import LoginInterface
from models.employee_model import EmployeeModel

class LoginController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.login_interface = LoginInterface()
        self.login()

    def login(self):
        while 1:
            username = input('Username: ')
            password = getpass.getpass(prompt='Password: ')
            self.main_controller.employee_model = EmployeeModel('./models/data/employees.json', username, password)
            self.main_controller.employee_model._load_employee()
            if self.main_controller.employee_model.employee_id != None:
                self.main_controller.change_controller('main_menu')
                break
            else:
                print('ERROR! The information you entered is incorrect. Please try again')
                self.main_controller.logout()
