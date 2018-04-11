from tkinter import *
from controllers.GUI.main_client_controller import MainClientController

class ATMSimulator():
    def __init__(self):
        self.root = Tk()
        self.main_controller = MainClientController(self.root)
        self.main_controller.change_controller('card_input')

if __name__ == '__main__':
    atm1 = ATMSimulator()
    mainloop()