import getpass
from views.CLI.cli_interface import AccountDeletionInterface

class AccountDeletionController():
    '''
        Controller class for the AccountDeletionInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            account_deletion_interface: the view this class controls

        Methods:
            delete_account: delete one of the current customer's accounts
                using main controller's customer model
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_deletion_interface = AccountDeletionInterface()
        self.delete_account()

    def delete_account(self):

        success = False

        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account type to delete:\n\t1. Chequing\n\t2. Savings\n')
            account_type_choice = input()
            if self.main_controller.customer_model.delete_customer_account(self.main_controller.customer_model.current_customer_profile['customer_id'], account_type_choice):
                success = True

        if success == True:
            while 1:
                input('Account deletion successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Account deletion failed! Press enter to continue.')
                break
            self.main_controller.reset_session()
