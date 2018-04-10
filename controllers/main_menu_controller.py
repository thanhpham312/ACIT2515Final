from views.main_menu_interface import MainMenuInterface

class MainMenuController():
    def __init__(self, main_controller, current_account):
        self.main_controller = main_controller
        self.main_menu_interface = MainMenuInterface(main_controller.main_interface.main_interface_frame)
        self.main_menu_interface.button1.bind('<Button-1>', lambda event: self.main_controller.change_controller('quick_cash'))
        self.main_menu_interface.button2.bind('<Button-1>', lambda event: self.main_controller.change_controller('withdraw'))
        self.main_menu_interface.button3.bind('<Button-1>', lambda event: self.main_controller.change_controller('deposit'))
        self.main_menu_interface.button4.bind('<Button-1>', lambda event: self.main_controller.change_controller('check_balance'))
        self.main_menu_interface.button6.bind('<Button-1>', lambda event: exit())