from tkinter import messagebox
from views.GUI.account_choice_interface import AccounChoiceInterface

class AccountChoiceController():
    def __init__(self, main_controller, next_screen):
        self.main_controller = main_controller
        self.next_screen = next_screen
        main_controller.main_interface.master.title('Choose Account')
        self.account_type_check_interface = AccounChoiceInterface(main_controller.main_interface.main_interface_frame)

        self.account_type_check_interface.bottom_savings_button.config(command=lambda:
                                                                       self.select_account('savings'))
        self.account_type_check_interface.bottom_chequing_button.config(command=lambda:
                                                                        self.select_account('chequing'))

    def select_account(self, type):
        self.main_controller.customer_model._set_current_account(type)
        if self.main_controller.customer_model.current_account != None:
            self.main_controller.change_controller(self.next_screen)
        else:
            messagebox.showwarning("Error", "You don't have a {} account.\nPlease select another one.".format(type))