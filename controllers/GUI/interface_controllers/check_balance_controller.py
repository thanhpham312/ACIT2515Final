from views.GUI.check_balance_interface import CheckBalanceInterface

class CheckBalanceController():
    '''
        Controller class for the CheckBalanceInterface view.

        Attributes:
            main_controller: a reference to the main controller object
            check_balance_interface: the view this class controls

        Methods:
            ok: proceed to confirm transaction and promt user to continue or logout
    '''
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Check Balance')
        self.check_balance_interface = CheckBalanceInterface(main_controller.main_interface.main_interface_frame)

        # self.check_balance_interface.button1.config()
        self.check_balance_interface.button2.config(command=self.ok)

        self.check_balance_interface.label2.config(text='${}'.format(self.main_controller.customer_model.current_account.balance))

    def ok(self):
        self.main_controller.change_controller('confirm', message='Transaction completed')