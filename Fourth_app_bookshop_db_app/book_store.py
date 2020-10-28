from tkinter import *
import sqlite3

db_file_name = 'data/book_store.dba'
books_db_name = 'book_db'
select_all_records = '*'


def get_next_id() -> int:
    '''Returns the current value of global variable g_next_Id and increment it by 1'''
    global g_next_Id
    crnt_id = g_next_Id
    g_next_Id = g_next_Id + 1
    return crnt_id

def create_db() -> None:
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ' + books_db_name + ' (id INTEGER, title TEXT,  author TEXT, year TEXT, isdn TEXT )')
    conn.commit()
    conn.close()


def insert(id:int, title:str, year:str, autor:str, isdn:str) -> bool:
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ' + books_db_name + '(id, title ,author, year, isdn) VALUES (?,?,?,?,?)', (id, title, year, autor, isdn))
    conn.commit()
    conn.close()

def select (query:str) -> list:
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute('SELECT ' + query + ' FROM ' + books_db_name)
    result = cursor.fetchall()
    conn.close()
    return result

def init_db() -> None:
    global g_next_Id
    create_db()
    ids = select('id')
    if len(ids) == 0:
        g_next_Id = 1
    else:
        print(ids)
        ids_int = [int(str_val[0]) for str_val in ids]
        ids_int.sort()
        g_next_Id = ids_int[-1] + 1
    #print(next_id)

def select_all() -> None:
    '''Select all records from the database and add them to the text box'''
    res = select(select_all_records)
    print(res)

def search() -> None:
    '''Searches DB based on non-empty Entries'''


def add() -> None:
    '''Adds Entry in DB based on non-empty Entries'''
    # print('Title: ' + title_val.get())
    # print('Autor: ' + autor_val.get())
    # print('Year: ' + year_val.get())
    # print('ISDN: ' + isdn_val.get())
    insert(id = get_next_id(), title = title_val.get(), autor = autor_val.get(), year = year_val.get(), isdn = isdn_val.get())

def update() -> None:
    '''Updates Selected record in DB based on non-empty Entries'''

def delete() -> None:
    '''Deletes Selected record in DB based on non-empty Entries'''

def close() -> None:
    '''Closes the program'''
    main_win.destroy()

init_db()

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
e_autor.grid(row = 0, column = 3, padx = 2)

#ISDN:
l_isdn = Label(main_win, text = 'ISDN', height=1 , width = 15)
l_isdn.grid(row = 1, column = 2)
isdn_val = StringVar()
e_isdn = Entry(main_win, textvariable = isdn_val)
e_isdn.grid(row = 1, column = 3, padx = 2)

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

out_text = Text(main_win, bg = '#00F0A0', height = 15, width = 60)
out_text.grid(row = 2, column = 0, columnspan = 3, rowspan = 6, pady = 10, padx = 2)

main_win.mainloop()
