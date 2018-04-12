import getpass
from views.CLI.cli_interface import AccountDeletionInterface

class AccountDeletionController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountDeletionInterface()
        self.delete_account()

    def delete_account(self):
        pass
