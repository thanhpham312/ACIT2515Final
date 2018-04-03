from tkinter import *
from views.main_interface import MainInterface
from controllers.main_controller import MainController

class ATMSIMULATOR():
    def __init__(self):
        self.root = Tk()
        self.main_interface = MainInterface(self.root)
        self.main_controller = MainController(self.main_interface)

if __name__ == '__main__':
    atm1 = ATMSIMULATOR()
    mainloop()