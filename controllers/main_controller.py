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
<<<<<<< HEAD
    def __init__(self):
        self.current_controller = None

    def reset_current_controller(self, main_interface):
        del self.current_controller
        if type(main_interface.current_frame) is PinInterface:
            self.current_controller = PinController(main_interface)
        elif type(main_interface.current_frame) is MainMenuInterface:
            self.current_controller = MainMenuController(main_interface)
=======
    def __init__(self, main_interface):
        self.main_interface = main_interface
        self.main_interface.current_frame.button1.bind('<Button-1>', lambda event: self.main_interface.draw_interface('withdraw'))
        self.main_interface.current_frame.button3.bind('<Button-1>', lambda event: self.main_interface.draw_interface('deposit'))
        self.main_interface.current_frame.button4.bind('<Button-1>', lambda event: self.main_interface.draw_interface('check_balance'))
        self.main_interface.current_frame.button6.bind('<Button-1>', lambda event: exit())
>>>>>>> d4352eeae965b01082a58b3fc88d3654ce06ed41
