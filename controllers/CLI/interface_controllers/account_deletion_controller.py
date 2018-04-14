import getpass
from views.CLI.cli_interface import AccountDeletionInterface

class AccountDeletionController():
    '''
    Controller to delete account
    Parameter - main controller
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountDeletionInterface()
        self.delete_account()

    def delete_account(self):
        '''
        Function deletes the account,
        checks for input validations
        :return: None
        '''
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
