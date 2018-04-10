from views.check_balance_interface import CheckBalanceInterface

class CheckBalanceController():
    def __init__(self, main_controller, current_account):
        self.main_controller = main_controller
        self.current_account = current_account
        self.check_balance_interface = CheckBalanceInterface(main_controller.main_interface.main_interface_frame)
        
        self.check_balance_interface.button1.bind('<Button-1>', lambda event:
            self.main_controller.change_controller('main_menu'))
        self.check_balance_interface.button2.bind('<Button-1>', lambda event:
            self.main_controller.change_controller('main_menu'))

        self.check_balance_interface.label2.config(text=self.current_account.current_account.balance)