from controllers.main_cli_controller import CLIModelController
class CLITellerSimmulator():
    def __init__(self, file_name):
        self._cli_main_controller = CLIModelController(file_name)


if __name__ == "__main__":
    admin = CLITellerSimmulator('./models/data/accounts.json')
    admin._cli_main_controller._add_new_account(1)
