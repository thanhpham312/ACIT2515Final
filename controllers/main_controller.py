import sys
sys.path.append(sys.path[0] + "/..")

from views.main_interface import MainInterface
from controllers.pin_controller import PinController
from controllers.main_menu_controller import MainMenuController
from controllers.quick_cash_controller import QuickCashController
from controllers.withdraw_controller import WithdrawController
from controllers.deposit_controller import DepositController
from controllers.check_balance_controller import CheckBalanceController

class MainController():
    def __init__(self, root):
        self.root = root
        self.main_interface = MainInterface(self.root)
        self.current_controller = None

    # def reset_current_controller(self, main_interface):
    #     del self.current_controller
    #     if type(main_interface.current_frame) is PinInterface:
    #         self.current_controller = PinController(main_interface)
    #     elif type(main_interface.current_frame) is MainMenuInterface:
    #         self.current_controller = MainMenuController(main_interface)

    def change_controller(self, controller):
        self.main_interface.redraw_main_interface_frame()
        del self.current_controller
        if controller == 'pin':
            self.current_controller = PinController(self)
        elif controller == 'main_menu':
            self.current_controller = MainMenuController(self)
        elif controller == 'quick_cash':
            self.current_controller = QuickCashController(self)
        elif controller == 'withdraw':
            self.current_controller = WithdrawController(self)
        elif controller == 'deposit':
            self.current_controller = DepositController(self)
        elif controller == 'check_balance':
            self.current_controller = CheckBalanceController(self)

