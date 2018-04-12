from views.CLI.cli_interface import MainMenuInterface

class MainMenuController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.login_interface = MainMenuInterface(self.main_controller.employee_model.username)
        self.check_option()

    def check_option(self):
        while 1:
            option = input('Enter a number to continue: ')
            if option == "1":
                self.main_controller.change_controller('create_customer')
            elif option == "2":
                self.main_controller.change_controller('delete_customer')
            elif option == "3":
                self.main_controller.change_controller('create_account')
            elif option == "4":
                self.main_controller.change_controller('delete_account')
            elif option == "5":
                self.main_controller.change_controller('view_transactions')
            elif option == "6":
                self.main_controller.change_controller('print_transactions')
            elif option == "7":
                self.main_controller.logout()
            else:
                print('Invalid option, please choose a valid one.')
