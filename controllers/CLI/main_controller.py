from controllers.CLI.interface_controllers.login_controller import LoginController
from controllers.CLI.interface_controllers.main_menu_controller import MainMenuController

class MainCLIController():
    def __init__(self):
        self.current_interface_controller = None
        self.employee_model = None
        self.customer_model = None

    def change_controller(self, controller, next_screen=None, message=''):
        self.current_interface_controller = None
        if controller == 'main_menu':
            self.current_interface_controller = MainMenuController(self)
        elif controller == 'login':
            self.current_interface_controller = LoginController(self)

    def logout(self):
        self.current_interface_controller = None
        self.employee_model = None
        self.customer_model = None
        self.change_controller('login')