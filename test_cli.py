from controllers.main_cli_controller import CLIModelController
class CLITellerSimmulator():
    def __init__(self, file_name):
        self._cli_main_controller = CLIModelController(file_name)


if __name__ == "__main__":
    admin = CLITellerSimmulator('./models/data/accounts.json')
    #admin._cli_main_controller._add_new_account(1)
    #admin._cli_main_controller._change_account_holder_name("2",'Sten')
    #admin._cli_main_controller._delete_account("2")
    admin._cli_main_controller._view_account_transaction_log("1")
