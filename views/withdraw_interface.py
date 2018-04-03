from tkinter import *


class WithdrawInterface():

    def __init__(self, master: Frame):
        self.master = master

        # frames

        self.top_frame = Frame(self.master)
        self.left_frame = Frame(self.master)
        self.right_frame = Frame(self.master)
        # self.top_frame.config(bg='blue')
        # self.right_frame.config(bg='red')
        # self.left_frame.config(bg='green')


        self.top_frame.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        # self.top_frame.grid_rowconfigure(5, minsize=100)
        # self.top_frame.grid_columnconfigure(2, minsize=100)

        self.left_frame.grid(row=1, column=0, sticky=NSEW)
        # self.middle_frame.grid_rowconfigure(8, minsize=100)

        self.right_frame.grid(row=1, column=1, sticky=NSEW)


        # widgets

        self.top_label = Label(self.top_frame, text="Please select withdraw amount", font=("Courier", 20))

        self.right_amount_20_button = Button(self.right_frame, text="20", font=("Courier", 20))
        self.right_amount_40_button = Button(self.right_frame, text="40", font=("Courier", 20))
        self.right_amount_80_button = Button(self.right_frame, text="80", font=("Courier", 20))
        self.right_amount_other_button = Button(self.right_frame, text="Other", font=("Courier", 20))

        self.left_amount_100_button = Button(self.left_frame, text="100", font=("Courier", 20))
        self.left_amount_200_button = Button(self.left_frame, text="200", font=("Courier", 20))
        self.left_amount_400_button = Button(self.left_frame, text="400", font=("Courier", 20))
        self.left_cancel_button = Button(self.left_frame, text="Cancel", font=("Courier", 20))


        # grid the buttons
        self.master.rowconfigure(0, weight=1)
        # self.master.rowconfigure(1, weight=1)
        # self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)

        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)

        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure(0, weight=1)


        self.top_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        self.right_amount_20_button.grid(row=0, column=0, sticky=NSEW, padx=(100,1), pady=10)
        self.right_amount_40_button.grid(row=1, column=0, sticky=NSEW, padx=(100,1), pady=10)
        self.right_amount_80_button.grid(row=2, column=0, sticky=NSEW, padx=(100,1), pady=10)
        self.right_amount_other_button.grid(row=3, column=0, sticky=NSEW, padx=(100,1), pady=10)

        self.left_amount_100_button.grid(row=0, column=0, sticky=NSEW,  padx=(1,100), pady=10)
        self.left_amount_200_button.grid(row=1, column=0, sticky=NSEW,  padx=(1,100), pady=10)
        self.left_amount_400_button.grid(row=2, column=0, sticky=NSEW,  padx=(1,100), pady=10)
        self.left_cancel_button.grid(row=3, column=0, sticky=NSEW, padx=(1,100), pady=10)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    WithdrawInterface(root)
    mainloop()





