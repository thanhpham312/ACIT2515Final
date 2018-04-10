from tkinter import *


class AccountTypeCheckInterface():

    def __init__(self, master: Frame):
        self.master = master

        # frames

        self.top_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)


        self.top_frame.grid(row=0, column=0, sticky=NSEW)
        self.bottom_frame.grid(row=1, column=0, sticky=NSEW)


        # widgets

        self.top_label = Label(self.top_frame, text="Welcome\n\n\nPlease Select Account Type", font=("Courier", 20))
        self.bottom_savings_button = Button(self.bottom_frame, text="Savings", font=("Courier", 20), width=30, height=1)
        self.bottom_chequing_button = Button(self.bottom_frame, text="Chequing", font=("Courier", 20), width=30, height=1)



        # grid the buttons
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)




        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)


        self.top_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)
        self.bottom_savings_button.grid(row=0, column=0, sticky=NSEW, padx=(10,50), pady=(100, 10))
        self.bottom_chequing_button.grid(row=0, column=1, sticky=NSEW, padx=(50,10), pady=(100, 10))


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    AccountTypeCheckInterface(root)
    mainloop()





