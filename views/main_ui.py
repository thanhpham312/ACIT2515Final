from tkinter import *
from .check_balance_ui import CheckBalance

class MainUI():
    def __init__(self, master):
        self.master = master
        self.master.title('Bank ATM')

        # Menu:
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)

        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Quit', command=self.master.quit)

        # Frames:
        self.upper_interface_frame = Frame(self.master)
        self.bottom_buttons_frame = Frame(self.master)

        self.check_balance = CheckBalance(self.middle_interface_frame)
        # Gridding:

        self.upper_interface_frame.grid(row=0, column=0, padx=20, pady=10)
        self.bottom_buttons_frame.grid(row=1, column=0, padx=20, pady=10)

if __name__ == '__main__':
    root = Tk()
    MainUI(root)
    mainloop()