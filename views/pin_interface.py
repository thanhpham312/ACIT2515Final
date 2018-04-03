from tkinter import *

class PinInterface():
    def __init__(self, master, photo_p):
        self.master = master



        self.top_frame = Frame(self.master)
        self.left_frame = Frame(self.master)
        self.center_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0, column=1, sticky=NSEW)
        self.left_frame.grid(row=1, column=0, sticky=NSEW)
        self.center_frame.grid(row=2, column=1, sticky=NSEW)
        self.bottom_frame.grid(row=3, column=1, sticky=NSEW)


        self.enter_pin_text = Label(self.top_frame, text="Please enter your PIN\nthen press OK", font=("Courier", 15))
        self.enter_pin_field = Entry(self.top_frame, font=("Courier", 20), justify=CENTER)

        self.prot_pin_labed = Label(self.left_frame, image=photo_p)

        self.pin_pad_1 = Button(self.center_frame, text="1", anchor=W)
        self.pin_pad_2 = Button(self.center_frame, text="2", anchor=W)
        self.pin_pad_3 = Button(self.center_frame, text="3", anchor=W)
        self.pin_pad_cancel = Button(self.center_frame, text="Cancel", anchor=W)

        self.pin_pad_4 = Button(self.center_frame, text="4", anchor=W)
        self.pin_pad_5 = Button(self.center_frame, text="5", anchor=W)
        self.pin_pad_6 = Button(self.center_frame, text="6", anchor=W)
        self.pin_pad_correct = Button(self.center_frame, text="Correction", anchor=W)

        self.pin_pad_7 = Button(self.center_frame, text="7", anchor=W)
        self.pin_pad_8 = Button(self.center_frame, text="8", anchor=W)
        self.pin_pad_9 = Button(self.center_frame, text="9", anchor=W)
        self.pin_pad_OK = Button(self.center_frame, text="OK", anchor=W)

        self.pin_pad_blank = Button(self.center_frame, text="", anchor=W)
        self.pin_pad_0 = Button(self.center_frame, text="0", anchor=W)
        self.pin_pad_random = Button(self.center_frame, text="blah", anchor=W)
        self.pin_pad_another_blank = Button(self.center_frame, text="blah", anchor=W)

        self.bottom_text = Label(self.bottom_frame, text="Press CORRECTION to correct an error\nPress CANCEL to return your card", font=("Courier", 15), anchor=CENTER)


        #row config master
        # self.master.rowconfigure(0, weight=1)
        # self.master.rowconfigure(1, weight=1)
        # self.master.rowconfigure(2, weight=1)
        # self.master.rowconfigure(3, weight=1)
        # self.master.columnconfigure(0, weight=1)


        # GRID THE TOP
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.rowconfigure(1, weight=1)

        self.enter_pin_text.grid(row=0, column=0)
        self.enter_pin_field.grid(row=1, column=0)


        #GRID THE LEFT
        self.left_frame.rowconfigure(0, weight=1)

        self.prot_pin_labed.grid(row=0, column=0)

        #grid the pin pad
        self.center_frame.rowconfigure(0, weight=1)
        self.center_frame.rowconfigure(1, weight=1)
        self.center_frame.rowconfigure(2, weight=1)
        self.center_frame.rowconfigure(3, weight=1)

        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.columnconfigure(2, weight=1)
        self.center_frame.columnconfigure(3, weight=1)


        self.pin_pad_1.grid(row=0, column=0, sticky=NSEW)
        self.pin_pad_2.grid(row=0, column=1, sticky=NSEW)
        self.pin_pad_3.grid(row=0, column=2, sticky=NSEW)
        self.pin_pad_cancel.grid(row=0, column=3, sticky=NSEW)

        self.pin_pad_4.grid(row=1, column=0, sticky=NSEW)
        self.pin_pad_5.grid(row=1, column=1, sticky=NSEW)
        self.pin_pad_6.grid(row=1, column=2, sticky=NSEW)
        self.pin_pad_correct.grid(row=1, column=3, sticky=NSEW)

        self.pin_pad_7.grid(row=2, column=0, sticky=NSEW)
        self.pin_pad_8.grid(row=2, column=1, sticky=NSEW)
        self.pin_pad_9.grid(row=2, column=2, sticky=NSEW)
        self.pin_pad_OK.grid(row=2, column=3, sticky=NSEW)

        self.pin_pad_blank.grid(row=3, column=0, sticky=NSEW)
        self.pin_pad_0.grid(row=3, column=1, sticky=NSEW)
        self.pin_pad_random.grid(row=3, column=2, sticky=NSEW)
        self.pin_pad_another_blank.grid(row=3, column=3, sticky=NSEW)


        #draw the bottom grid
        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(0, weight=1)

        self.bottom_text.grid(row=0, column=0, sticky=NSEW)






if __name__ == '__main__':
    root = Tk()
    root.geometry('600x450')
    photo = PhotoImage(file="assets/images/protect_pin.gif")
    PinInterface(root, photo)
    mainloop()

