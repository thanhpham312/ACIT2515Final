import os
from controllers.CLI.interface_controllers.login_controller import LoginController
from controllers.CLI.interface_controllers.main_menu_controller import MainMenuController
from controllers.CLI.interface_controllers.customer_creation_controller import CustomerCreationController
from controllers.CLI.interface_controllers.customer_deletion_controller import CustomerDeletionController
from controllers.CLI.interface_controllers.account_creation_controller import AccountCreationController
from controllers.CLI.interface_controllers.account_deletion_controller import AccountDeletionController
from controllers.CLI.interface_controllers.view_transactions_controller import ViewTransactionsController
from controllers.CLI.interface_controllers.print_transactions_controller import PrintTransactionsController
from controllers.CLI.interface_controllers.choose_customer_profile_controller import ChooseCustomerProfileController

class MainCLIController():
    def __init__(self):
        self.current_interface_controller = None
        self.employee_model = None
        self.customer_model = None

    def change_controller(self, controller, next_controller=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.current_interface_controller = None
        if controller == 'main_menu':
            self.current_interface_controller = MainMenuController(self)
        elif controller == 'login':
            self.current_interface_controller = LoginController(self)
        elif controller == 'create_customer':
            self.current_interface_controller = CustomerCreationController(self)
        elif controller == 'delete_customer':
            self.current_interface_controller = CustomerDeletionController(self)
        elif controller == 'create_account':
            self.current_interface_controller = AccountCreationController(self)
        elif controller == 'delete_account':
            self.current_interface_controller = AccountDeletionController(self)
        elif controller == 'view_transactions':
            self.current_interface_controller = ViewTransactionsController(self)
        elif controller == 'print_transactions':
            self.current_interface_controller = PrintTransactionsController(self)
        elif controller == 'choose_customer_profile':
            self.current_interface_controller = ChooseCustomerProfileController(self, next_controller)

    def logout(self):
        self.current_interface_controller = None
        self.employee_model = None
        self.customer_model = None
        self.change_controller('login')

    def cancel_check(self, input_text):
        if input_text == ':q':
            self.reset_session()

    def reset_session(self):
        self.current_interface_controller = None
        self.customer_model.current_customer_profile = None
        self.change_controller('main_menu')