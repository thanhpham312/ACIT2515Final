from tkinter import *
from views.main_interface import MainInterface
from controllers.main_controller import MainController

class ATMSimulator():
    def __init__(self):
        self.root = Tk()
        self.main_controller = MainController(self.root)
        self.main_controller.change_controller('pin')

if __name__ == '__main__':
    atm1 = ATMSimulator()
    mainloop()