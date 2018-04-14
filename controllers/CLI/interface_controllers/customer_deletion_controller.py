import getpass
import hashlib
from views.CLI.cli_interface import CustomerDeletionInterface

class CustomerDeletionController():
    '''
    Deletes profile for customer
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = CustomerDeletionInterface()
        self.delete_customer()

    def delete_customer(self):
        '''
        Fucntion deletes the profile of customer with all transactions logs. Checks for customer PIN mathc
        :return: None
        '''
        success = False
        if self.main_controller.customer_model.current_customer_profile != None:
            if self.main_controller.customer_model.delete_customer(self.main_controller.customer_model.current_customer_profile['customer_id']):
                success = True
        if success == True:
            while 1:
                input('Customer deletion successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Customer deletion failed! Press enter to continue.')
                break
            self.main_controller.reset_session()
