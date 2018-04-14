from views.CLI.cli_interface import MainMenuInterface

class MainMenuController():
    '''
        Controller class for the MainMenuInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            main_menu_interface: the view this class controls

        Methods:
            check_option: re-initialize the current controller based on user input
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_menu_interface = MainMenuInterface(self.main_controller.employee_model.username)
        self.check_option()

    def check_option(self):

        while 1:
            option = input('Enter a number to continue: ')
            if option == "1":
                self.main_controller.change_controller('create_customer')
            elif option == "2":
                self.main_controller.change_controller('choose_customer_profile', next_controller='delete_customer')
            elif option == "3":
                self.main_controller.change_controller('choose_customer_profile', next_controller='create_account')
            elif option == "4":
                self.main_controller.change_controller('choose_customer_profile', next_controller='delete_account')
            elif option == "5":
                self.main_controller.change_controller('choose_customer_profile', next_controller='view_transactions')
            elif option == "6":
                self.main_controller.change_controller('choose_customer_profile', next_controller='print_transactions')
            elif option == "7":
                self.main_controller.logout()
            else:
                print('Invalid option, please choose a valid one.')
