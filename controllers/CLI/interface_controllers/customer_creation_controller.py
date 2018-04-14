import getpass
from views.CLI.cli_interface import CustomerCreationInterface

class CustomerCreationController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = CustomerCreationInterface()
        self.create_customer()

    def create_customer(self):
        success = False
        name = input('Please enter a name for new customer: ')
        self.main_controller.cancel_check(name)
        pin = input('Choose a pin: ')
        self.main_controller.cancel_check(pin)
        try:
            int(pin)
            self.main_controller.customer_model.create_customer(name, pin)
            success = True
        except:
            success = False

        if success == True:
            while 1:
                input('Customer creation successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Customer creation failed! Press enter to continue.')
                break
            self.main_controller.reset_session()

