import getpass
from views.CLI.cli_interface import AccountDeletionInterface

class AccountDeletionController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountDeletionInterface()
        self.delete_account()

    def delete_account(self):
        while 1:
            customer_id = input("Enter the customer id: ")
            self.main_controller.customer_model.delete_customer(customer_id)
            self.main_controller.change_controller('main_menu')
