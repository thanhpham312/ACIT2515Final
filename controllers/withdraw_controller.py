from views.withdraw_interface import WithdrawInterface

class WithdrawController():
    def __init__(self, main_controller, current_account):
        self.main_controller = main_controller
        self.withdraw_interface = WithdrawInterface(main_controller.main_interface.main_interface_frame)
        self.withdraw_interface.left_cancel_button.bind('<Button-1>', lambda event: self.main_controller.change_controller('main_menu'))