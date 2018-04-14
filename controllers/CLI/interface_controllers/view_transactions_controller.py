import getpass
from views.CLI.cli_interface import ViewTransactionInterface

class ViewTransactionsController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = ViewTransactionInterface()
        self.view_transactions()

    def view_transactions(self):


        transaction_string = ''

        if self.main_controller.customer_model.current_customer_profile != None:
            print('Pick an account type to view transactions:\n\t1. Chequing\n\t2. Savings\n')
            account_type_choice = input()
            transaction_string = self.main_controller.customer_model.view_customer_transactions(
                self.main_controller.customer_model.current_customer_profile['customer_id'], account_type_choice)
            print(transaction_string)

        if transaction_string != '':
            while 1:
                input('Viewing transactions successful! Press enter to continue.')
                break
            self.main_controller.reset_session()
        else:
            while 1:
                input('Viewing transactions failed! Press enter to continue.')
                break
            self.main_controller.reset_session()
