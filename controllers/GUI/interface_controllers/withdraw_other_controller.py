from tkinter import messagebox
from views.GUI.withdraw_other_interface import WithdrawOtherInterface

class WithdrawOtherController():
    '''
        Controller class for the WithdrawOtherController view.

        Attributes:
            main_controller: a reference to the main controller object
            withdraw_interface: the view this class controls

        Methods:
            withdraw: user inputs amount of money to take out from the customer model
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Deposit')
        self.withdraw_interface = WithdrawOtherInterface(main_controller.main_interface.main_interface_frame)
        self.withdraw_interface.bottom_cancel_button.config(command=lambda:
            self.main_controller.change_controller('confirm', message='Transaction cancelled'))
        self.withdraw_interface.bottom_continue_button.config(command=lambda:
            self.withdraw(self.withdraw_interface.middle_amount_box.get()))

    def withdraw(self, amount=0):
        try:
            amount = float(amount)
            if amount%20 == 0:
                if self.main_controller.customer_model.current_account.withdraw(amount) == True:
                    messagebox.showwarning('Success', 'You have withdrawn {} from your account'.format(amount))
                    self.main_controller.customer_model._save_to_file()
                    self.main_controller.change_controller('confirm', message='Withdrawal successful')
                else:
                    messagebox.showwarning('Failed', 'You do not have enough money for this transaction')
                    self.main_controller.change_controller('confirm', message='Withdrawal unsuccessful')
            else:
                messagebox.showwarning('Failed', 'Incorrect amount')
                self.main_controller.change_controller('confirm', message='Withdrawal unsuccessful')
        except:
            messagebox.showwarning('Failed', 'Incorrect amount')
            self.main_controller.change_controller('confirm', message='Withdrawal unsuccessful')
