import hashlib
from views.GUI.change_pin_interface import ChangePinInterface

class ChangePinController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Change PIN')
        self.change_pin_interface = ChangePinInterface(main_controller.main_interface.main_interface_frame)

        self.change_pin_interface.bottom_cancel_button.config(command=self.cancel)
        self.change_pin_interface.bottom_continue_button.config(command=self.proceed)

    def cancel(self):
        self.main_controller.reset_session()

    def proceed(self):
        new_pin = self.change_pin_interface.pin_entry.get()
        try:
            int(new_pin)
            new_pin = hashlib.sha256(str.encode(new_pin)).hexdigest()
            self.main_controller.change_controller('pin_change_confirm', new_pin=new_pin)
        except:
            self.main_controller.change_controller('confirm', message='PIN change failed')