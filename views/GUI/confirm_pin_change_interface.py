from tkinter import *


class ConfirmPinChangeInterface():

    def __init__(self, master: Frame):
        self.master = master

        # frames

        self.top_frame = Frame(self.master)
        self.middle_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)


        self.top_frame.grid(row=0, column=0, sticky=NSEW)
        self.middle_frame.grid(row=1, column=0, sticky=NSEW)
        self.bottom_frame.grid(row=2, column=0, sticky=NSEW)


        # widgets

        self.top_label = Label(self.top_frame, text="Please enter your old pin\n to confirm change", font=("Courier", 20))
        self.pin_entry = Entry(self.middle_frame, font=("Courier", 35), justify=CENTER, show="*")
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
        self.middle_frame.rowconfigure(1, weight=1)

        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)


        self.top_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)
        self.pin_entry.grid(row=1, column=0, sticky=NSEW, padx=30, pady=20)
        self.bottom_cancel_button.grid(row=0, column=0, sticky=NSEW, padx=(10,50), pady=50)
        self.bottom_continue_button.grid(row=0, column=1, sticky=NSEW, padx=(50,10), pady=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    ConfirmPinChangeInterface(root)
    mainloop()





