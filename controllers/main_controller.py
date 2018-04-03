class MainController():
    def __init__(self, main_interface):
        self.main_interface = main_interface
        self.main_interface.current_frame.button3.bind('<Button-1>', lambda event: self.main_interface.draw_interface('deposit'))
        self.main_interface.current_frame.button4.bind('<Button-1>', lambda event: self.main_interface.draw_interface('check_balance'))