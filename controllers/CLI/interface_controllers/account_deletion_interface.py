import getpass
from views.CLI.cli_interface import AccountDeletionInterface

class AccountDeletionController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountDeletionInterface()
        self.delete_account()

    def delete_account(self):
        customer_id = input('Please enter a customer id: ')
        account_type = input('Enter the account type: 1-chequing; 2-saving: ')
        self.main_controller.customer_model.delete_customer_account(customer_id, account_type)
        print('Customer deletion successful!')
        self.main_controller.change_controller('main_menu')