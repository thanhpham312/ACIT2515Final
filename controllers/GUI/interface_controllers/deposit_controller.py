from tkinter import messagebox
from views.GUI.deposit_interface import DepositInterface

class DepositController():
    '''
        Controller class for the DepositInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            deposit_interface: the view this class controls

        Methods:
            deposit: Put money into user account using the customer model
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Deposit')
        self.deposit_interface = DepositInterface(main_controller.main_interface.main_interface_frame)
        self.deposit_interface.bottom_cancel_button.config(command=lambda:
            self.main_controller.change_controller('confirm', message='Transaction cancelled'))
        self.deposit_interface.bottom_continue_button.config(command=lambda:
            self.deposit(self.deposit_interface.middle_amount_box.get()))

    def deposit(self, amount=0):
        if self.main_controller.customer_model.current_account.deposit(amount) == True:
            messagebox.showwarning('Success', 'You have deposit {} into your account'.format(amount))
            self.main_controller.customer_model._save_to_file()
            self.main_controller.change_controller('confirm', message='Deposit successful')
        else:
            messagebox.showwarning('Failed', 'Amount incorrect')
            self.main_controller.change_controller('confirm', message='Deposit unsuccessful')