from views.main_interface import MainInterface
from controllers.pin_controller import PinController
from controllers.main_menu_controller import MainMenuController
from controllers.quick_cash_controller import QuickCashController
from controllers.withdraw_controller import WithdrawController
from controllers.deposit_controller import DepositController
from controllers.check_balance_controller import CheckBalanceController
from controllers.card_input_controller import CardInputController
from controllers.account_type_check_controller import AccountTypeCheckController

from models.user_model_for_client import UserModelForClient
from models.account_model_for_client import AccountModelForClient

class MainClientController():
    def __init__(self, root):
        self.root = root
        self.main_interface = MainInterface(self.root)
        self.current_interface_controller = None
        self.current_user_model = None
        self.current_account_model = None
        # self.current_user = UserModelForClient(user_file_name, username, password)
        # self.current_account = AccountModelForClient(account_file_name)
        # self.current_account._set_current_account(self.current_user.current_user_id)

    def change_controller(self, controller):
        self.main_interface.redraw_main_interface_frame()
        del self.current_interface_controller
        if controller == 'pin':
            self.current_interface_controller = PinController(self, self.current_account_model)
        elif controller == 'main_menu':
            self.current_interface_controller = MainMenuController(self, self.current_account_model)
        elif controller == 'quick_cash':
            self.current_interface_controller = QuickCashController(self, self.current_account_model)
        elif controller == 'withdraw':
            self.current_interface_controller = WithdrawController(self, self.current_account_model)
        elif controller == 'deposit':
            self.current_interface_controller = DepositController(self, self.current_account_model)
        elif controller == 'check_balance':
            self.current_interface_controller = CheckBalanceController(self, self.current_account_model)
        elif controller == 'card_input':
            self.current_interface_controller = CardInputController(self, self.current_account_model)
        elif controller == 'account_type_check':
            self.current_interface_controller = AccountTypeCheckController(self, self.current_account_model)

    def reset_session(self):
        self.current_interface_controller = None
        self.current_user_model = None
        self.current_account_model = None
        self.change_controller('card_input')