from tkinter import messagebox
from views.card_input_interface import CardInputInterface
from models.user_model_for_client import UserModelForClient
from models.account_model_for_client import AccountModelForClient

class CardInputController():
    def __init__(self, main_controller, current_account):
        self.main_controller = main_controller
        self.current_account = current_account
        self.card_input_interface = CardInputInterface(main_controller.main_interface.main_interface_frame)

        self.card_input_interface.bottom_cancel_button.config(command=exit)
        self.card_input_interface.bottom_continue_button.config(command=self.log_in)

    def log_in(self):
        if self.card_input_interface.card_entry.get() != '' or self.card_input_interface.pin_entry.get() != '':
            self.main_controller.current_user_model = UserModelForClient('./models/data/users.json', self.card_input_interface.card_entry.get(), self.card_input_interface.pin_entry.get())
            self.main_controller.current_account_model = AccountModelForClient('./models/data/accounts.json')
            # self.main_controller.current_account_model._set_current_account(self.main_controller.current_user_model.current_user_id)

            if self.main_controller.current_user_model.current_user_id != None:
                self.main_controller.change_controller('account_type_check')
            else:
                messagebox.showwarning("Error", "The account information you entered is incorrect.\nPlease try again.")
        else:
            messagebox.showwarning("Error", "Please do not leave any of the fields blank.")