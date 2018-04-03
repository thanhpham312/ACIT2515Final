from tkinter import *
from tkinter import font
from constants import *

class CheckBalance():
    def __init__(self, master, account=None):
        self.master = master

        # Frames:
        self.info_screen = Frame(self.master)
        self.buttons_frame = Frame(self.master)

        # Elements:
        self.label1 = Label(self.info_screen, text='Your account balance is:', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.label2 = Label(self.info_screen, text='$0', font=('Courier', BASE_TITLE_FONT_SIZE))
        self.button1 = Button(self.buttons_frame, text='CANCEL', font=('Courier', BASE_NORMAL_FONT_SIZE))
        self.button2 = Button(self.buttons_frame, text='OK', font=('Courier', BASE_NORMAL_FONT_SIZE))

        # Gridding:
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.info_screen.rowconfigure(0, weight=1)
        self.info_screen.rowconfigure(1, weight=1)
        self.info_screen.columnconfigure(0, weight=1)

        self.buttons_frame.rowconfigure(0, weight=1)
        self.buttons_frame.rowconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)

        self.info_screen.grid(row=0, column=0, sticky=N+S+E+W)
        self.buttons_frame.grid(row=1, column=0, sticky=N+S+E+W)

        self.label1.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.label2.grid(row=1, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.button1.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.button2.grid(row=0, column=1, padx=20, pady=20, sticky=N+S+E+W)


if __name__ == '__main__':
    root = Tk()
    CheckBalance(root)
    mainloop()