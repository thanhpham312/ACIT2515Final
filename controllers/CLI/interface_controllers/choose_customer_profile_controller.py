import hashlib
import getpass
from views.CLI.cli_interface import ChooseCustomerProfileInterface

class ChooseCustomerProfileController():
    '''
        Controller class for the ChooseCustomerProfileInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            next_controller: determines the next controller that is going to replace the current one
            choose_customer_profile_interface: the view this class controls

        Methods:
            choose_customer_profile: gets customer profile information
                using main controller's customer model
    '''
    def __init__(self, main_controller, next_controller):
        self.main_controller = main_controller
        self.next_controller = next_controller
        self.choose_customer_profile_interface = ChooseCustomerProfileInterface()
        self.choose_customer_profile()

    def choose_customer_profile(self):

        customer_card_number = input('Enter the customer card number: ')
        self.main_controller.cancel_check(customer_card_number)
        pin = getpass.getpass(prompt='Please enter pin: ')
        self.main_controller.cancel_check(pin)
        pin_retype = getpass.getpass(prompt='Please enter pin again: ')
        self.main_controller.cancel_check(pin_retype)

        dict_of_users = self.main_controller.customer_model.customers_dict
        success = False

        if pin == pin_retype:
            hashed_pin = hashlib.sha256(str.encode(pin)).hexdigest()

            for customer_id, customer_profile in dict_of_users.items():
                if customer_profile['card_number'] == customer_card_number and hashed_pin == customer_profile['pin']:
                    # customer_card_number = customer_profile['card_number']
                    self.main_controller.customer_model.current_customer_profile = {
                        'customer_id': customer_id,
                        'customer_profile': customer_profile
                    }
                    success = True
                    break

        if success == True:
            while 1:
                input('Authentication successful! Press enter to continue.')
                break
            self.main_controller.change_controller(self.next_controller)
        else:
            while 1:
                input('Authentication failed! Press enter to continue.')
                break
            self.main_controller.change_controller('main_menu')