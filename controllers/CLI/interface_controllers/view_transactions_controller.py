import getpass
from views.CLI.cli_interface import ViewTransactionInterface

class ViewTransactionsController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = ViewTransactionInterface()
        self.view_transactions()

    def view_transactions(self):
        pass
