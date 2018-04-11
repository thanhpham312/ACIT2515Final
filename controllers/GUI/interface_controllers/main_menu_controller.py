from tkinter import messagebox
from views.GUI.main_menu_interface import MainMenuInterface

class MainMenuController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        main_controller.main_interface.master.title('Main Menu')
        self.main_menu_interface = MainMenuInterface(main_controller.main_interface.main_interface_frame)
        self.main_menu_interface.button1.config(command=self.withdraw_quick_cash)
        self.main_menu_interface.button2.bind('<Button-1>', lambda event: self.main_controller.change_controller('withdraw'))
        self.main_menu_interface.button3.bind('<Button-1>', lambda event: self.main_controller.change_controller('deposit'))
        self.main_menu_interface.button4.config(command=self.check_balance)
        self.main_menu_interface.button6.config(command=self.reset_session)

    def reset_session(self):
        self.main_controller.reset_session()

    def withdraw_quick_cash(self):
        self.main_controller.change_controller('account_choice', 'quick_cash')

    def check_balance(self):
        self.main_controller.change_controller('account_choice', 'check_balance')