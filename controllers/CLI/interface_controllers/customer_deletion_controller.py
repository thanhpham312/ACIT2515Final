import getpass
from views.CLI.cli_interface import CustomerDeletionInterface

class CustomerDeletionController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = CustomerDeletionInterface()
        self.delete_customer()

    def delete_customer(self):
        customer_id = input('Enter the customer id: ')
        account_type = input('Choose a account type: ')
        self.main_controller.customer_model.delete_customer_account(customer_id, account_type)
        print('Customer deletion successful!')
        self.main_controller.change_controller('main_menu')
