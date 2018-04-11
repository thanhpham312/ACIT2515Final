from views.GUI.main_interface import MainInterface
from controllers.GUI.interface_controllers.pin_controller import PinController
from controllers.GUI.interface_controllers.main_menu_controller import MainMenuController
from controllers.GUI.interface_controllers.quick_cash_controller import QuickCashController
from controllers.GUI.interface_controllers.withdraw_controller import WithdrawController
from controllers.GUI.interface_controllers.deposit_controller import DepositController
from controllers.GUI.interface_controllers.check_balance_controller import CheckBalanceController
from controllers.GUI.interface_controllers.card_input_controller import CardInputController
from controllers.GUI.interface_controllers.account_choice_controller import AccountChoiceController


class MainClientController():
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('./views/assets/icons/favicon.ico')
        self.main_interface = MainInterface(self.root)
        self.current_interface_controller = None
        self.customer_model = None
        # self.current_user = UserModelForClient(user_file_name, username, password)
        # self.current_account = AccountModelForClient(account_file_name)
        # self.current_account._set_current_account(self.current_user.current_user_id)

    def change_controller(self, controller, next_screen = None):
        self.main_interface.redraw_main_interface_frame()
        del self.current_interface_controller
        if controller == 'pin':
            self.current_interface_controller = PinController(self)
        elif controller == 'main_menu':
            self.current_interface_controller = MainMenuController(self)
        elif controller == 'quick_cash':
            self.current_interface_controller = QuickCashController(self)
        elif controller == 'withdraw':
            self.current_interface_controller = WithdrawController(self)
        elif controller == 'deposit':
            self.current_interface_controller = DepositController(self)
        elif controller == 'check_balance':
            self.current_interface_controller = CheckBalanceController(self)
        elif controller == 'card_input':
            self.current_interface_controller = CardInputController(self)
        elif controller == 'account_choice':
            self.current_interface_controller = AccountChoiceController(self, next_screen)

    def reset_session(self):
        self.current_interface_controller = None
        self.current_user_model = None
        self.current_account_model = None
        self.change_controller('card_input')