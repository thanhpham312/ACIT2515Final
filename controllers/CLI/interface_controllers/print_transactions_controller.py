import getpass
from views.CLI.cli_interface import PrintTransactionInterface

class PrintTransactionsController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.account_creation_interface = PrintTransactionInterface()
        self.print_transactions()

    def print_transactions(self):
        pass
