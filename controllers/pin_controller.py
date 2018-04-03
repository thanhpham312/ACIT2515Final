class PinController():
    def __init__(self, main_interface):
        self.main_interface = main_interface
        self.main_interface.current_frame.pin_pad_OK.bind('<Button-1>', lambda event:
            self.main_interface.draw_interface('main_menu'))
        self.main_interface.current_frame.pin_pad_cancel.bind('<Button-1>', lambda event: exit())