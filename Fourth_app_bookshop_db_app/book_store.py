from tkinter import *

def select_all() -> None:
    '''Select all records from the database and add them to the text box'''

def search() -> None:
    '''Searches DB based on non-empty Entries'''

def add() -> None:
    '''Adds Entry in DB based on non-empty Entries'''

def update() -> None:
    '''Updates Selected record in DB based on non-empty Entries'''

def delete() -> None:
    '''Deletes Selected record in DB based on non-empty Entries'''

def close() -> None:
    '''Closes the program'''

main_win = Tk(className = 'Book Store')

#Title:
l_title = Label(main_win, text = 'Title', height=1 , width = 15)
l_title.grid(row = 0, column = 0)
title_val = StringVar()
e_title = Entry(main_win, textvariable = title_val)
e_title.grid(row = 0, column = 1)

#Year:
l_year = Label(main_win, text = 'Year', height=1 , width = 15)
l_year.grid(row = 1, column = 0)
year_val = StringVar()
e_year = Entry(main_win, textvariable = year_val)
e_year.grid(row = 1, column = 1)

#Autor:
l_autor = Label(main_win, text = 'Autor', height=1 , width = 15)
l_autor.grid(row = 0, column = 2)
autor_val = StringVar()
e_autor = Entry(main_win, textvariable = autor_val)
e_autor.grid(row = 0, column = 3)

#ISDN:
l_isdn = Label(main_win, text = 'ISDN', height=1 , width = 15)
l_isdn.grid(row = 1, column = 2)
isdn_val = StringVar()
e_isdn = Entry(main_win, textvariable = isdn_val)
e_isdn.grid(row = 1, column = 3)

#Buttons
b_viewall = Button(main_win, text = 'View All', width = 12, command = select_all)
b_viewall.grid(row = 2, column = 3)
b_search = Button(main_win, text = 'Search Entry', width = 12, command = search)
b_search.grid(row = 3, column = 3)
b_add = Button(main_win, text = 'Add entry', width = 12, command = add)
b_add.grid(row = 4, column = 3)
b_update = Button(main_win, text = 'Update Selected', width = 12, command = update)
b_update.grid(row = 5, column = 3)
b_delete = Button(main_win, text = 'Delete Selected', width = 12, command = delete)
b_delete.grid(row = 6, column = 3)
b_close = Button(main_win, text = 'Close', width = 12, command = close)
b_close.grid(row = 7, column = 3)

main_win.mainloop()
