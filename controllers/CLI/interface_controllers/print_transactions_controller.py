import getpass
from views.CLI.cli_interface import PrintTransactionInterface

class PrintTransactionsController():
    '''
        Controller class for the PrintTransactionInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            print_transactions_interface: the view this class controls

        Methods:
            print_transactions: print the current customer's transaction log to a txt file
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.print_transactions_interface = PrintTransactionInterface()
        self.print_transactions()

    def print_transactions(self):

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
