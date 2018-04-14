import getpass
from views.CLI.cli_interface import CustomerCreationInterface

class CustomerCreationController():
    '''
        Controller class for the CustomerCreationInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            account_creation_interface: the view this class controls

        Methods:
            create_customer: create a new customer profile
                using main controller's customer model
    '''
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

