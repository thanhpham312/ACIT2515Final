from tkinter import messagebox
from views.account_type_check_interface import AccountTypeCheckInterface

class AccountTypeCheckController():
    def __init__(self, main_controller, current_account):
        self.main_controller = main_controller
        self.current_account = current_account
        self.account_type_check_interface = AccountTypeCheckInterface(main_controller.main_interface.main_interface_frame)

        self.account_type_check_interface.bottom_savings_button.config(command=lambda:
                                                                       self.select_account('saving'))
        self.account_type_check_interface.bottom_chequing_button.config(command=lambda:
                                                                        self.select_account('chequing'))

    def select_account(self, type):
        self.main_controller.customer_model._set_current_account(type)
        if self.main_controller.customer_model.current_account != None:
            self.main_controller.change_controller('main_menu')
        else:
            messagebox.showwarning("Error", "You don't have a {} account.\nPlease select another one.".format(type))