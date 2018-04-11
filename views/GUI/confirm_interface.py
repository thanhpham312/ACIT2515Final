from tkinter import *


class ConfirmInterface():

    def __init__(self, master: Frame):
        self.master = master

        # frames

        self.top_frame = Frame(self.master)
        self.middle_frame =Frame(self.master)
        self.bottom_frame = Frame(self.master)


        self.top_frame.grid(row=0, column=0, sticky=NSEW)
        self.middle_frame.grid(row=1, column=0, sticky=NSEW)
        self.bottom_frame.grid(row=2, column=0, sticky=NSEW)


        # widgets

        self.top_label = Label(self.top_frame, text="Thank you\n\n This Transaction\nis complete", font=("Courier", 20))
        self.middle_label = Label(self.middle_frame, text="Would you like to do another transaction?", font=("Courier", 15))
        self.bottom_yes_button = Button(self.bottom_frame, text="Yes", font=("Courier", 20), width=30, height=1)
        self.bottom_no_button = Button(self.bottom_frame, text="No", font=("Courier", 20), width=30, height=1)



        # grid the buttons
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)

        self.middle_frame.rowconfigure(0, weight=1)
        self.middle_frame.columnconfigure(0, weight=1)


        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)


        self.top_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)
        self.middle_label.grid(row=0, column=0, sticky=NSEW, padx=20, pady=(0, 20))
        self.bottom_yes_button.grid(row=0, column=0, sticky=NSEW, padx=(10,50), pady=20)
        self.bottom_no_button.grid(row=0, column=1, sticky=NSEW, padx=(50,10), pady=20)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    ConfirmInterface(root)
    mainloop()





