from tkinter import *
from .constants import *
from .main_menu_interface import MainMenuInterface
from .pin_interface import PinInterface
from .withdraw_interface import WithdrawInterface
from .check_balance_interface import CheckBalanceInterface
from .deposit_interface import DepositInterface

class MainInterface():
    def __init__(self, master):
        self.master = master
        self.master.title('Bank ATM')
        self.master.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))


        # Menu:
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)

        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Quit', command=self.master.quit)

        # Frames:
        self.main_interface_frame = Frame(self.master, bg='green')
        self.current_frame = MainMenuInterface(self.main_interface_frame, PhotoImage(file="views/assets/images/protect_pin.gif"))
        # self.bottom_buttons_frame = Frame(self.master, bg='black')

        # self.check_balance = CheckBalance(self.upper_interface_frame)
        # Gridding:
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.main_interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky=N + S + E + W)
        # self.bottom_buttons_frame.grid(row=1, column=0, padx=20, pady=10,  sticky=N+S+E+W)

    def redraw_main_interface_frame(self):
        self.main_interface_frame.destroy()
        self.main_interface_frame = Frame(self.master, bg='green')
        self.main_interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky=N + S + E + W)
        del self.current_frame


    def draw_interface(self, interface):
        # self.current_frame = CheckBalance(self.upper_interface_frame)
        # self.current_frame = depositInterface(self.upper_interface_frame)
        if interface == 'pin':
            self.redraw_main_interface_frame()
            self.current_frame = PinInterface(self.main_interface_frame)
        elif interface == 'main_menu':
            self.redraw_main_interface_frame()
            self.current_frame = MainMenuInterface(self.main_interface_frame)
        elif interface == 'quick_cash':
            self.redraw_main_interface_frame()
            self.current_frame = WithdrawInterface(self.main_interface_frame)
        elif interface == 'withdraw':
            self.redraw_main_interface_frame()
            self.current_frame = WithdrawInterface(self.main_interface_frame)
        elif interface == 'check_balance':
            self.redraw_main_interface_frame()
            self.current_frame = CheckBalanceInterface(self.main_interface_frame)
        elif interface == 'deposit':
            self.redraw_main_interface_frame()
            self.current_frame = DepositInterface(self.main_interface_frame)

if __name__ == '__main__':
    root = Tk()
    # root.geometry('600x450')
    new_window = MainInterface(root)
    # new_window.draw_interface()
    mainloop()