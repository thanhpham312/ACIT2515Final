import sys
sys.path.append(sys.path[0] + "/..")

from .pin_controller import PinController
from .main_menu_controller import MainMenuController

from views.main_menu_interface import MainMenuInterface
from views.pin_interface import PinInterface
from views.withdraw_interface import WithdrawInterface
from views.check_balance_interface import CheckBalanceInterface
from views.deposit_interface import DepositInterface

class MainController():
    def __init__(self):
        self.current_controller = None

    def reset_current_controller(self, main_interface):
        del self.current_controller
        if type(main_interface.current_frame) is PinInterface:
            self.current_controller = PinController(main_interface)
        elif type(main_interface.current_frame) is MainMenuInterface:
            self.current_controller = MainMenuController(main_interface)