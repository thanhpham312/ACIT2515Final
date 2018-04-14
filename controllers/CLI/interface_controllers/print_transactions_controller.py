import getpass
from views.CLI.cli_interface import PrintTransactionInterface

class PrintTransactionsController():
    """
    Controller to print transactions to a separate file in the /models/data directory.
    """
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = PrintTransactionInterface()
        self.print_transactions()

    def print_transactions(self):
        '''
        Controller to print all transaction logs for specific user and specific account.
        :return:None
        '''

        success = False
        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account type to print transactions:\n\t1. Chequing\n\t2. Savings\n')
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
