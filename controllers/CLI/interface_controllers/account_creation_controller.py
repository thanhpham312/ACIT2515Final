import getpass
from views.CLI.cli_interface import AccountCreationInterface

class AccountCreationController():
    '''
        Controller class for the AccountCreationInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            account_creation_interface: the view this class controls

        Methods:
            create_account: Creates a new Chequing or Savings account for the current customer
                using main controller's customer model
    '''

    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountCreationInterface()
        self.create_account()

    def create_account(self):
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
