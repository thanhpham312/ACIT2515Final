import getpass
from views.CLI.cli_interface import AccountCreationInterface

class AccountCreationController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountCreationInterface()
        self.create_account()

    def create_account(self):
        customer_id = input("Enter the customer id: ")
        self.main_controller.cancel_check(customer_id)
        customer_id = input("Enter the customer id: ")
        account_type = input("Enter the account type: ")
        self.main_controller.customer_model.create_account(customer_id,account_type)
        self.main_controller.change_controller('main_menu')
        while 1:
            break
        self.main_controller.change_controller('main_menu')
