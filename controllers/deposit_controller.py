from views.deposit_interface import DepositInterface

class DepositController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.deposit_interface = DepositInterface(main_controller.main_interface.main_interface_frame)
        self.deposit_interface.bottom_cancel_button.bind('<Button-1>', lambda event:
            self.main_controller.change_controller('main_menu'))
        self.deposit_interface.bottom_continue_button.bind('<Button-1>', lambda event:
            self.main_controller.change_controller('main_menu'))