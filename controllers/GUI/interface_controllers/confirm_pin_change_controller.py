import hashlib
from views.GUI.confirm_pin_change_interface import ConfirmPinChangeInterface

class ConfirmPinChangeController():
    def __init__(self, main_controller, new_pin):
        self.new_pin = new_pin
        self.main_controller = main_controller
        self.main_controller.main_interface.master.title('Confirm PIN Change')
        self.confirm_pin_change_interface = ConfirmPinChangeInterface(main_controller.main_interface.main_interface_frame)

        self.confirm_pin_change_interface.bottom_cancel_button.config(command=self.cancel)
        self.confirm_pin_change_interface.bottom_continue_button.config(command=self.proceed)

    def cancel(self):
        self.main_controller.reset_session()

    def proceed(self):
        confirm_pin = self.confirm_pin_change_interface.pin_entry.get()
        try:
            int(confirm_pin)
            confirm_pin = hashlib.sha256(str.encode(confirm_pin)).hexdigest()
            if self.new_pin == confirm_pin:
                print(self.new_pin, confirm_pin)
                print(self.main_controller.customer_model.customer_id)
                self.main_controller.customer_model.change_pin(self.new_pin)
                self.main_controller.change_controller('confirm', message='PIN change successful')
            else:
                self.main_controller.change_controller('confirm', message='PINs do not match')
        except:
            self.main_controller.change_controller('confirm', message='PIN change failed')
