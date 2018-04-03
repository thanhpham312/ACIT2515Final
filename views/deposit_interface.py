from tkinter import *
from .constants import *

class depositInterface():

    def __init__(self, master: Frame):
        self.master = master

        # frames

        self.top_frame = Frame(self.master)
        self.middle_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)
        # self.top_frame.config(bg='blue')
        # self.middle_frame.config(bg='red')
        # self.bottom_frame.config(bg='green')


        self.top_frame.grid(row=0, column=0, sticky=NSEW)
        # self.top_frame.grid_rowconfigure(5, minsize=100)
        # self.top_frame.grid_columnconfigure(2, minsize=100)

        self.middle_frame.grid(row=1, column=0, sticky=NSEW)
        # self.middle_frame.grid_rowconfigure(8, minsize=100)

        self.bottom_frame.grid(row=2, column=0, sticky=NSEW)


        # widgets

        self.top_label = Label(self.top_frame, text="Please enter deposit amount", font=("Courier", 20))
        self.middle_amount_box = Entry(self.middle_frame, font=("Courier", 20), justify=CENTER)
        self.bottom_cancel_button = Button(self.bottom_frame, text="Cancel", font=("Courier", 20), width=30, height=1)
        self.bottom_continue_button = Button(self.bottom_frame, text="Continue", font=("Courier", 20), width=30, height=1)



        # grid the buttons
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)

        self.middle_frame.columnconfigure(0, weight=1)
        self.middle_frame.rowconfigure(0, weight=1)

        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)


        self.top_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)
        self.middle_amount_box.grid(row=0, column=0, sticky=NSEW, padx=200, pady=80)
        self.bottom_cancel_button.grid(row=0, column=0, sticky=NSEW, padx=(10,50), pady=50)
        self.bottom_continue_button.grid(row=0, column=1, sticky=NSEW, padx=(50,10), pady=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    depositInterface(root)
    mainloop()





