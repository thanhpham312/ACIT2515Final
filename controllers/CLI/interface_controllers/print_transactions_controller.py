import getpass
from views.CLI.cli_interface import PrintTransactionInterface

class PrintTransactionsController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = PrintTransactionInterface()
        self.print_transactions()

    def print_transactions(self):
        # customer_id = input('Please enter an id of a customer to see transactions: ')
        # self.main_controller.cancel_check(customer_id)
        #
        # customer_id = input('Please enter an id of a customer to see transactions: ')
        # account_type = input('Please enter account type(1: for chequing or 2: for saving): ')
        # self.main_controller.customer_model.print_customer_transactions(customer_id, account_type)
        # while 1:
        #     continue_option = input('Press any key to continue: ')
        #     break
        # self.main_controller.change_controller('main_menu')

        success = False
        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account to create:\n\t1. Chequing\n\t2. Savings\n')
            account_type_choice = input()
            if self.main_controller.customer_model.print_customer_transactions(
                    self.main_controller.customer_model.current_customer_profile['customer_id'],
                    account_type_choice):
                success = True

        if success == True:
            while 1:
                input('Printing transactions successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Printing transactions failed! Press enter to continue.')
                break
            self.main_controller.reset_session()
