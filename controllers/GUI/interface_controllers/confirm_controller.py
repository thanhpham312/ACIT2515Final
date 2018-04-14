from views.GUI.confirm_interface import ConfirmInterface

class ConfirmController():
    '''
        Controller class for the ConfirmInterface view.
        Promt user to continue or logout

        Attributes:
            main_controller: a reference to the main controller object
            confirm_interface: the view this class controls
    '''
    def __init__(self, main_controller, message='Transaction completed'):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Withdrawal')
        self.confirm_interface = ConfirmInterface(main_controller.main_interface.main_interface_frame)
        self.confirm_interface.top_label.config(text=message)
        self.confirm_interface.bottom_yes_button.config(command=self.main_controller.reset_session)
        self.confirm_interface.bottom_no_button.config(command=self.main_controller.reset)
