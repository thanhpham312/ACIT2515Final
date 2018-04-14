from views.GUI.main_interface import MainInterface
from controllers.GUI.interface_controllers.main_menu_controller import MainMenuController
from controllers.GUI.interface_controllers.quick_cash_controller import QuickCashController
from controllers.GUI.interface_controllers.withdraw_controller import WithdrawController
from controllers.GUI.interface_controllers.withdraw_other_controller import WithdrawOtherController
from controllers.GUI.interface_controllers.deposit_controller import DepositController
from controllers.GUI.interface_controllers.check_balance_controller import CheckBalanceController
from controllers.GUI.interface_controllers.card_input_controller import CardInputController
from controllers.GUI.interface_controllers.account_choice_controller import AccountChoiceController
from controllers.GUI.interface_controllers.confirm_controller import ConfirmController
from controllers.GUI.interface_controllers.change_pin_controller import ChangePinController
from controllers.GUI.interface_controllers.confirm_pin_change_controller import ConfirmPinChangeController


class MainClientController():
    '''
        Master controller class for the interface controllers.

        Attributes:
            root: main tkinter window
            main_interface: The interface this controller controls
            customer_model: the model for interacting with customer data

        Methods:
            change_controller: Change the current controller
            reset: returns the class attribute to the initial state and change controller to login
            reset_session: reset partial data and return user to the main menu
    '''
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('./views/assets/icons/favicon.ico')
        self.main_interface = MainInterface(self.root)
        self.current_interface_controller = None
        self.customer_model = None
        # self.current_user = UserModelForClient(user_file_name, username, password)
        # self.current_account = AccountModelForClient(account_file_name)
        # self.current_account._set_current_account(self.current_user.current_user_id)

    def change_controller(self, controller, next_screen = None, message='', new_pin=None):
        self.main_interface.redraw_main_interface_frame()
        del self.current_interface_controller
        if controller == 'main_menu':
            self.current_interface_controller = MainMenuController(self)
        elif controller == 'quick_cash':
            self.current_interface_controller = QuickCashController(self)
        elif controller == 'withdraw':
            self.current_interface_controller = WithdrawController(self)
        elif controller == 'withdraw_other':
            self.current_interface_controller = WithdrawOtherController(self)
        elif controller == 'deposit':
            self.current_interface_controller = DepositController(self)
        elif controller == 'check_balance':
            self.current_interface_controller = CheckBalanceController(self)
        elif controller == 'card_input':
            self.current_interface_controller = CardInputController(self)
        elif controller == 'account_choice':
            self.current_interface_controller = AccountChoiceController(self, next_screen)
        elif controller == 'confirm':
            self.current_interface_controller = ConfirmController(self, message)
        elif controller == 'pin_change':
            self.current_interface_controller = ChangePinController(self)
        elif controller == 'pin_change_confirm':
            self.current_interface_controller = ConfirmPinChangeController(self, new_pin)

    def reset(self):
        self.current_interface_controller = None
        self.current_user_model = None
        self.current_account_model = None
        self.change_controller('card_input')

    def reset_session(self):
        self.current_interface_controller = None
        self.current_account_model = None
        self.change_controller('main_menu')