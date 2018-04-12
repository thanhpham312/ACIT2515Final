import getpass
from views.CLI.cli_interface import AccountCreationInterface

class AccountCreationController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountCreationInterface()
        self.create_account()

    def create_account(self):
        pass
