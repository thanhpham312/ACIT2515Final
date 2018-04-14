import getpass
from views.CLI.cli_interface import AccountCreationInterface

class AccountCreationController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = AccountCreationInterface()
        self.create_account()

    def create_account(self):
        # customer_id = input("Enter the customer id: ")
        # self.main_controller.cancel_check(customer_id)
        # account_type = input("Enter the account type: 1-chequing; 2-saving: ")
        # self.main_controller.customer_model.create_account(customer_id,account_type)
        # while 1:
        #     break
        # self.main_controller.change_controller('main_menu')

        success = False
        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account to create:\n\t1. Chequing\n\t2. Savings\n')
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
