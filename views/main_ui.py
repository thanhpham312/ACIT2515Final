from tkinter import *
from constants import *
from check_balance_ui import CheckBalance

class MainUI():
    def __init__(self, master):
        self.master = master
        self.master.title('Bank ATM')
        self.master.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))

        self.current_frame = NONE

        # Menu:
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)

        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Quit', command=self.master.quit)

        # Frames:
        self.upper_interface_frame = Frame(self.master, bg='green')
        # self.bottom_buttons_frame = Frame(self.master, bg='black')

        # self.check_balance = CheckBalance(self.upper_interface_frame)
        # Gridding:
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.upper_interface_frame.grid(row=0, column=0, padx=20, pady=20,  sticky=N+S+E+W)
        # self.bottom_buttons_frame.grid(row=1, column=0, padx=20, pady=10,  sticky=N+S+E+W)

    def draw_interface(self):
        self.current_frame = CheckBalance(self.upper_interface_frame)

if __name__ == '__main__':
    root = Tk()
    # root.geometry('600x450')
    new_window = MainUI(root)
    new_window.draw_interface()
    mainloop()