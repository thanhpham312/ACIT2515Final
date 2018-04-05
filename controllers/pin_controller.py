from tkinter import *
from views.pin_interface import PinInterface

class PinController():
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.pin_interface = PinInterface(main_controller.main_interface.main_interface_frame)

        self.pin_interface.pin_pad_OK.bind('<Button-1>', lambda event:
            self.main_controller.change_controller('main_menu'))
        self.pin_interface.pin_pad_cancel.bind('<Button-1>', lambda event: exit())