import getpass
from views.CLI.cli_interface import AccountCreationInterface

class AccountCreationController():
    '''
        Account Creating Controller
        This is the controller for customer account controller
        Parameter to pass in the main controller for the class
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountCreationInterface()
        self.create_account()

    def create_account(self):
        '''
        Fucntion, that creates an account for user
        Checks the validations for inputs
        :return:
            none
        '''

        success = False
        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account type to create:\n\t1. Chequing\n\t2. Savings\n')
            account_type_choice = input()
            if self.main_controller.customer_model.create_account(self.main_controller.customer_model.current_customer_profile['customer_id'], account_type_choice):
                success = True

        if success == True:
            while 1:
                input('Account creation successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Account creation failed! Press enter to continue.')
                break
            self.main_controller.reset_session()
