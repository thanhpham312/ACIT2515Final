from tkinter import *
from views.assets.constants import *

class MainInterface():
    def __init__(self, master):
        self.master = master
        self.master.title('Bank ATM')
        self.master.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))


        # Menu:
        # self.main_menu = Menu(self.master)
        # self.master.config(menu=self.main_menu)
        # self.file_menu = Menu(self.main_menu)
        #
        # self.main_menu.add_cascade(label='File', menu=self.file_menu)
        # self.file_menu.add_command(label='Quit', command=self.master.quit)

        # Frames:
        self.main_interface_frame = Frame(self.master)

        # Gridding:
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.main_interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky=N + S + E + W)

    def redraw_main_interface_frame(self):
        self.main_interface_frame.destroy()
        self.main_interface_frame = Frame(self.master)
        self.main_interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky=N + S + E + W)

if __name__ == '__main__':
    root = Tk()
    root.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
    new_window = MainInterface(root)
    mainloop()