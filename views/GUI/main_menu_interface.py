from tkinter import *
from views.assets.constants import *

class MainMenuInterface():
    def __init__(self, master, account=None):
        self.master = master

        # Frames:
        self.row1 = Frame(self.master)
        self.row2 = Frame(self.master)
        self.row3 = Frame(self.master)
        self.row4 = Frame(self.master)

        # Elements:
        self.label1 = Label(self.row1, text='Choose an option:', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button1 = Button(self.row2, text='QUICK CASH', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button2 = Button(self.row2, text='WITHDRAW', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button3 = Button(self.row3, text='DEPOSIT', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button4 = Button(self.row3, text='CHECK BALANCE', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button5 = Button(self.row4, text='CHANGE PIN', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button6 = Button(self.row4, text='EXIT', font=('Courier', BASE_NORMAL_FONT_SIZE))

        # Gridding:
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.row1.rowconfigure(0, weight=1)
        self.row1.columnconfigure(0, weight=1)

        self.row2.rowconfigure(0, weight=1)
        self.row2.columnconfigure(0, weight=1, minsize=BUTTON_WIDTH)
        self.row2.columnconfigure(1, weight=1, minsize=BUTTON_WIDTH)

        self.row3.rowconfigure(0, weight=1)
        self.row3.columnconfigure(0, weight=1, minsize=BUTTON_WIDTH)
        self.row3.columnconfigure(1, weight=1, minsize=BUTTON_WIDTH)

        self.row4.rowconfigure(0, weight=1)
        self.row4.columnconfigure(0, weight=1, minsize=BUTTON_WIDTH)
        self.row4.columnconfigure(1, weight=1, minsize=BUTTON_WIDTH)

        self.row1.grid(row=0, column=0, sticky=N+S+E+W)
        self.row2.grid(row=1, column=0, sticky=N+S+E+W)
        self.row3.grid(row=2, column=0, sticky=N+S+E+W)
        self.row4.grid(row=3, column=0, sticky=N+S+E+W)

        self.label1.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.button1.grid(row=0, column=0, padx=30, pady=20, sticky=N+S+E+W)
        self.button2.grid(row=0, column=1, padx=30, pady=20, sticky=N+S+E+W)
        self.button3.grid(row=0, column=0, padx=30, pady=20, sticky=N+S+E+W)
        self.button4.grid(row=0, column=1, padx=30, pady=20, sticky=N+S+E+W)
        self.button5.grid(row=0, column=0, padx=30, pady=20, sticky=N+S+E+W)
        self.button6.grid(row=0, column=1, padx=30, pady=20, sticky=N+S+E+W)


if __name__ == '__main__':
    root = Tk()
    root.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
    MainMenuInterface(root)
    mainloop()