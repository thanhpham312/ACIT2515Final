from tkinter import messagebox
from views.GUI.withdraw_interface import WithdrawInterface

class WithdrawController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        main_controller.main_interface.master.title('Withdrawal')
        self.withdraw_interface = WithdrawInterface(main_controller.main_interface.main_interface_frame)
        self.withdraw_interface.right_amount_20_button.config(command=lambda: self.withdraw(20))
        self.withdraw_interface.right_amount_40_button.config(command=lambda: self.withdraw(40))
        self.withdraw_interface.right_amount_80_button.config(command=lambda: self.withdraw(80))

        self.withdraw_interface.left_amount_100_button.config(command=lambda: self.withdraw(100))
        self.withdraw_interface.left_amount_200_button.config(command=lambda: self.withdraw(200))
        self.withdraw_interface.left_amount_400_button.config(command=lambda: self.withdraw(400))

        self.withdraw_interface.right_amount_other_button.config(command=self.cancel)
        self.withdraw_interface.left_cancel_button.config(command=self.cancel)

    def withdraw(self, amount = 0):
        if self.main_controller.customer_model.current_account.withdraw(amount) == True:
            messagebox.showwarning('Success', 'You have withdrawn {} from your account'.format(amount))
            self.main_controller.customer_model._save_to_file()
            self.main_controller.change_controller('confirm', message='Withdrawal successful')
        else:
            messagebox.showwarning('Failed', 'You do not have enough money for this transaction')
            self.main_controller.change_controller('confirm', message='Withdrawal unsuccessful')

    def cancel(self):
        self.main_controller.change_controller('confirm', message='You have canceled withdrawal')