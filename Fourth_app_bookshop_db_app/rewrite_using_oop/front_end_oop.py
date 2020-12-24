from tkinter import *
from backend import DBInterraction

class BookStoreWindow():
    """Creates front end of the book store application. As input DBInterraction object is needed"""

    def __init__(self, dbclass):
        self.window = Tk()
        self.dbclass = dbclass
        self.title_text = StringVar()
        self.author_text = StringVar()
        self.year_text = StringVar()
        self.isdn_text = StringVar()
        self.selected_tuple = ()
        self.list1 = Listbox(self.window, height = 6, width = 35)
        self.e1 = Entry(self.window, textvariable = self.title_text)
        self.e2 = Entry(self.window, textvariable = self.author_text)
        self.e3 = Entry(self.window, textvariable = self.year_text)
        self.e4 = Entry(self.window, textvariable = self.isdn_text)


    def __get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])

    def __init_labels(self):
        l1 = Label(self.window, text='Title')
        l1.grid(row = 0, column = 0)

        l2 = Label(self.window, text='Author')
        l2.grid(row = 0, column = 2)

        l3 = Label(self.window, text='Year')
        l3.grid(row = 1, column = 0)

        l4 = Label(self.window, text='ISDN')
        l4.grid(row = 1, column = 2)

    def __init_entries(self):
        self.e1.grid(row = 0, column = 1)
        self.e2.grid(row = 0, column = 3)
        self.e3.grid(row = 1, column = 1)
        self.e4.grid(row = 1, column = 3)

    def __init_box(self):
        self.list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        sb1 = Scrollbar(self.window)
        sb1.grid(row = 2, column = 2, rowspan = 6)

        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

        self.list1.bind('<ButtonRelease-1>', self.__get_selected_row)

    def __init_buttons(self):
        b1 = Button(self.window, text = 'View all',width = 12,  command = self.__view_command)
        b1.grid(row = 2, column = 3)

        b2 = Button(self.window, text = 'Search entry',width = 12,  command = self.__search_command)
        b2.grid(row = 3, column = 3)

        b3 = Button(self.window, text = 'Add entry',width = 12,  command = self.__add_command)
        b3.grid(row = 4, column = 3)

        b4 = Button(self.window, text = 'Update',width = 12,  command = self.__update_command)
        b4.grid(row = 5, column = 3)

        b5 = Button(self.window, text = 'Delete',width = 12,  command = self.__delete_command)
        b5.grid(row = 6, column = 3)

        b6 = Button(self.window, text = 'Close',width = 12, command = self.__close_command)
        b6.grid(row = 7, column = 3)

    def __view_command(self):
        self.list1.delete(0, END)
        for row in self.dbclass.view():
            self.list1.insert(END, row)

    def __search_command(self):
        self.list1.delete(0, END)
        for row in self.dbclass.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),      self.isdn_text.get()):
            self.list1.insert(END, row)


    def __add_command(self):
        self.dbclass.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(),      self.isdn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(),      self.isdn_text.get()))

    def __delete_command(self):
        self.dbclass.delete(self.selected_tuple[0])

    def __update_command(self):
        self.dbclass.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isdn_text.get())

    def __close_command(self):
        self.window.destroy()

    def run_window(self):
        self.__init_labels()
        self.__init_entries()
        self.__init_box()
        self.__init_buttons()

        self.window.mainloop()


db = DBInterraction("../data/book_store_oop.dba")
crntApp = BookStoreWindow(db)
crntApp.run_window()
