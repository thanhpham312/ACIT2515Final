import getpass
from views.CLI.cli_interface import CustomerDeletionInterface

class CustomerDeletionController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = CustomerDeletionInterface()
        self.delete_customer()

    def delete_customer(self):
        pass
