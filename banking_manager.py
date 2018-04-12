from tkinter import *
from controllers.CLI.main_controller import MainCLIController

class BankingManager():
    def __init__(self):
        self.main_controller = MainCLIController()
        self.main_controller.change_controller('login')


if __name__ == "__main__":
    banking_manager = BankingManager()
    # admin = CLITellerSimmulator('./models/data/customers.json')
    # admin._cli_main_controller._add_new_account("20")
    #admin._cli_main_controller._change_account_holder_name("2",'Stacy')
    #admin._cli_main_controller._delete_account("55")
    # admin._cli_main_controller._view_account_transaction_log("1")
