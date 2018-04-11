from views.GUI.quick_cash_interface import QuickCashInterface

class QuickCashController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        main_controller.main_interface.master.title('Quick Cash')
        self.quick_cash_interface = QuickCashInterface(main_controller.main_interface.main_interface_frame)
        self.quick_cash_interface.left_cancel_button.bind('<Button-1>', lambda event: self.main_controller.change_controller('main_menu'))