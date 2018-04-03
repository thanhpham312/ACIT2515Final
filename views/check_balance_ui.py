from tkinter import *
from constants import *

class CheckBalance():
    def __init__(self, master, account=None):
        self.master = master

        # Frames:
        self.info_screen = Frame(self.master, bg='blue')
        self.buttons_frame = Frame(self.master, bg='red')

        # Elements:
        self.label1 = Label(self.info_screen, text='Your account balance is:')
        self.label2 = Label(self.info_screen, text='$0')
        self.button1 = Button(self.buttons_frame, text='CANCEL')
        self.button2 = Button(self.buttons_frame, text='OK')

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

        self.info_screen.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.buttons_frame.grid(row=1, column=0, padx=20, pady=20, sticky=N+S+E+W)

        self.label1.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.label2.grid(row=1, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.button1.grid(row=0, column=0, padx=20, pady=20, sticky=N+S+E+W)
        self.button2.grid(row=0, column=1, padx=20, pady=20, sticky=N+S+E+W)

if __name__ == '__main__':
    root = Tk()
    CheckBalance(root)
    mainloop()