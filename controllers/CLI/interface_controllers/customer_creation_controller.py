import getpass
from views.CLI.cli_interface import CustomerCreationInterface

class CustomerCreationController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = CustomerCreationInterface()
        self.create_customer()

    def create_customer(self):
        name = input('Please enter a name for new customer: ')
        pin = input('Choose a pin: ')
        self.main_controller.customer_model.create_customer(name, pin)
        print('Customer creation successful!')
        self.main_controller.change_controller('main_menu')
