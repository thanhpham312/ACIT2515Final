from tkinter import messagebox
from views.GUI.quick_cash_interface import QuickCashInterface

class QuickCashController():
    '''
        Controller class for the QuickCashInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            quick_cash_interface: the view this class controls

        Methods:
            withdraw_quick_cash: Take money out of user account using the customer model with a set amount
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Quick Cash')
        self.quick_cash_interface = QuickCashInterface(main_controller.main_interface.main_interface_frame)
        self.withdraw_quick_cash()
        # self.quick_cash_interface.left_cancel_button.bind('<Button-1>', lambda event: self.main_controller.change_controller('main_menu'))

    def withdraw_quick_cash(self, amount=40):
        if self.main_controller.customer_model.current_account.withdraw(amount) == True:
            messagebox.showwarning('Success', 'You have withdrawn {} from your account'.format(amount))
            self.main_controller.customer_model._save_to_file()
            self.main_controller.reset()
        else:
            messagebox.showwarning('Failed', 'You do not have enough money for this transaction')
            self.main_controller.reset()
