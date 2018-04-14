import getpass
import hashlib
from views.CLI.cli_interface import CustomerDeletionInterface

class CustomerDeletionController():
    '''
        Controller class for the CustomerDeletionInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            customer_deletion_interface: the view this class controls

        Methods:
            delete_customer: delete a customer profile
                using main controller's customer model
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.customer_deletion_interface = CustomerDeletionInterface()
        self.delete_customer()

    def delete_customer(self):

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
