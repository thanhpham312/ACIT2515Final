import os
from tkinter import *
from tkinter import filedialog, messagebox
from namer import Namer


class NameWindow:

    def __init__(self, master):

        # create any instances of other support classes that are needed and save them
        # as attributes of this window
        self.namer = Namer()
        self.master = master

        # set main window attributes such as title, geometry etc
        self.master.title('Name')
        # self.master.geometry('400x200')
        # self.master.config(background = 'LightBlue')

        # set up menus if there are any
        self.main_menu = Menu(self.master)
        self.master.config(menu = self.main_menu)
        self.file_menu = Menu(self.main_menu)

        self.main_menu.add_cascade(label = 'File', menu = self.file_menu)

        self.file_menu.add_command(label = 'Open', command = self._open)

        self.file_menu.add_command(label = 'Clear', command = self._clear)
        self.file_menu.add_command(label = 'Quit', command = self.master.quit)

        # define frames if needed
        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)

        self.right_frame = Frame(self.master)
        self.right_top_frame = Frame(self.right_frame)
        self.right_bot_frame = Frame(self.right_frame)

        self.top_frame.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.mid_frame.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.bot_frame.grid(row = 2, column = 0, padx = 20, pady = 10)

        self.right_frame.grid(row = 0, column = 1, rowspan = 3, pady = 20)
        self.right_top_frame.grid(row = 0, padx = 5, pady = 5)
        self.right_bot_frame.grid(row = 1, padx = 5, pady = 5)

        # define/create widgets and bind to events
        self.file_label = Label(self.top_frame, text = 'File:')
        self.file_value = Label(self.top_frame, text = self.namer.filename)

        self.name_label = Label(self.mid_frame, text = 'Random name:')
        self.name_value = Label(self.mid_frame, text = self.namer.random())
        self.new_label = Label(self.mid_frame, text='Name to add:')
        self.new_entry = Entry(self.mid_frame, width = 20)
        self.new_entry.bind('<Return>', self._add)

        self.rand_button = Button(self.bot_frame, text = 'Random', width = 10, command = self._random)
        self.add_button = Button(self.bot_frame, text = 'Add', width = 10, command = self._add)

        self.name_listbox = Listbox(self.right_top_frame, width = 20, height = 10, selectmode = SINGLE)
        self.name_scrollbar = Scrollbar(self.right_top_frame, orient = 'vertical')

        self.name_delete_button = Button(self.right_bot_frame, text = 'Delete', width = 10, command = self._delete)

        # place widgets in window (ie use pack or grid or whatever layout manager to place widgets)
        self.file_label.grid(row = 0, column = 0, sticky = E, padx = 5, pady = 5)
        self.file_value.grid(row = 0, column = 1, sticky = E, padx = 5, pady = 5)

        self.name_label.grid(row = 0, column = 0, sticky = E, padx = 5, pady = 5)
        self.name_value.grid(row = 0, column = 1, sticky = W, padx = 5, pady = 5)
        self.new_label.grid(row = 1, column = 0, sticky = E, padx = 5, pady = 5)
        self.new_entry.grid(row = 1, column = 1, sticky = W, padx = 5, pady = 5)
        self.new_entry.focus()

        self.rand_button.grid(row = 2, column = 0, sticky = E, padx = 20, pady = 5)
        self.add_button.grid(row = 2, column = 1, sticky = W, padx = 20, pady = 5)

        self.name_listbox.grid(row = 0, column = 0, sticky = E, padx = (20, 0), pady = 5)
        self.name_listbox.config(yscrollcommand = self.name_scrollbar.set)
        self.name_scrollbar.config(command = self.name_listbox.yview)
        self.name_scrollbar.grid(row=0, column=1, sticky = NS, padx = (0, 20))

        self.name_delete_button.grid(row = 1, padx = 5, pady = 5)

        self._populate_name_listbox()


    ##################
    # now we define command and/or callback functions as needed
    def _populate_name_listbox(self):
        self.name_listbox.delete(0, END)
        for name in self.namer._namelist:
            self.name_listbox.insert(END, name)

    def _open(self):
        new_file_name = os.path.basename(filedialog.askopenfilename(initialdir = '.'))
        if new_file_name != '':
            del self.namer
            self.namer = Namer(new_file_name)
            self.file_value.config(text = self.namer.filename)
        self._populate_name_listbox()

    def _clear(self):
        self.namer.clear()
        self.name_value['text'] = ''

    def _add(self):
        new_name = self.new_entry.get()
        if new_name != '':
            self.namer.add(new_name)
            self.new_entry.delete(0, END)
            messagebox.showinfo(title = 'Add Name', message = 'Name"{}" added to {}'.format(new_name, self.namer.filename))
            self._populate_name_listbox()

    def _random(self):
        self.name_value['text'] = self.namer.random()

    def _delete(self):
        self.namer.delete(self.name_listbox.curselection()[0])
        self._populate_name_listbox()

if __name__ == "__main__":
    root = Tk()
    NameWindow(root)
    mainloop()
