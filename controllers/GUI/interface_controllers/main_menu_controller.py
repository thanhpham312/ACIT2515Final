from tkinter import messagebox
from views.GUI.main_menu_interface import MainMenuInterface

class MainMenuController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Main Menu')
        self.main_menu_interface = MainMenuInterface(main_controller.main_interface.main_interface_frame)
        self.main_menu_interface.button1.config(command=self.withdraw_quick_cash)
        self.main_menu_interface.button2.config(command=self.withdraw)
        self.main_menu_interface.button3.config(command=self.deposit)
        self.main_menu_interface.button4.config(command=self.check_balance)
        self.main_menu_interface.button5.config(command=self.change_pin)
        self.main_menu_interface.button6.config(command=self.reset)

    def reset(self):
        self.main_controller.reset()

    def withdraw_quick_cash(self):
        self.main_controller.change_controller('account_choice', 'quick_cash')

    def withdraw(self):
        self.main_controller.change_controller('account_choice', 'withdraw')

    def deposit(self):
        self.main_controller.change_controller('account_choice', 'deposit')

    def check_balance(self):
        self.main_controller.change_controller('account_choice', 'check_balance')

    def change_pin(self):
        self.main_controller.change_controller('pin_change')
