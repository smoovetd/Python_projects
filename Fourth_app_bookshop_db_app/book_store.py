from tkinter import *
import tkinter
import tkinter.messagebox
import tkinter.ttk
from tkinter.ttk import Treeview
import sqlite3

db_file_name = 'data/book_store.dba'
books_db_name = 'book_db'
select_all_records = '*'

#global variables:
crnt_text_vals = []
# set is_verbose to True for debug
is_verbose = False

def validate_input() -> bool:
    res = True
    if title_val.get() == '':
        tkinter.messagebox.showerror(title = 'Input error', message = 'Title should not be empty')
        res = False
    elif author_val.get() == '':
        tkinter.messagebox.showerror(title = 'Input error', message = 'author should not be empty')
        res = False
    elif year_val.get() == '':
        tkinter.messagebox.showerror(title = 'Input error', message = 'Year should not be empty')
        res = False
    elif isdn_val.get() == '':
        tkinter.messagebox.showerror(title = 'Input error', message = 'ISDN should not be empty')
        res = False
    else:
        res = True
    return res

def validate_search():
    res = True
    if title_val.get() == '' and author_val.get() == '' and year_val.get() == '' and isdn_val.get() == '':
        tkinter.messagebox.showerror(title = 'Input error', message = 'At least one field should not be empty')
        res = False
    else:
        res = True
    return res

def get_next_id() -> int:
    '''Returns the current value of global variable g_next_Id and increment it by 1'''
    global g_next_Id
    global is_verbose
    crnt_id = g_next_Id
    g_next_Id = g_next_Id + 1
    if is_verbose: print ('Current id: ' + str(crnt_id) + ', Next id: ' + str(g_next_Id))
    return crnt_id

def create_db() -> None:
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ' + books_db_name + ' (id INTEGER, title TEXT,  author TEXT, year TEXT, isdn TEXT )')
    conn.commit()
    conn.close()


def insert(id:int, title:str, author:str, year:str,  isdn:str) -> bool:
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ' + books_db_name + '(id, title ,author, year, isdn) VALUES (?,?,?,?,?)', (id, title, author, year, isdn))
    conn.commit()
    conn.close()

def select (query:str, where_clause:str = None) -> list:
    global is_verbose
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    full_query = "SELECT " + query + " FROM " + books_db_name
    if where_clause != None:
        full_query = full_query + " WHERE " + where_clause
        if is_verbose: print(where_clause)
    if is_verbose: print(full_query)
    cursor.execute(full_query)
    result = cursor.fetchall()
    conn.close()
    return result

def init_db() -> None:
    global g_next_Id
    global is_verbose
    create_db()
    ids = select('id')
    if len(ids) == 0:
        g_next_Id = 1
    else:
        if is_verbose: print(ids)
        ids_int = [int(str_val[0]) for str_val in ids]
        ids_int.sort()
        g_next_Id = ids_int[-1] + 1
    #print(next_id)

def get_selected_item(event) -> None:
    global crnt_text_vals
    global is_verbose
    current_item = tree.focus()
    if (current_item != ''):
        curnt_record = tree.item(current_item)['values']
        #print(curnt_record)
        title_val.set(curnt_record[1])
        author_val.set(curnt_record[2])
        year_val.set(curnt_record[3])
        isdn_val.set(curnt_record[4])
        crnt_text_vals = curnt_record

    if is_verbose: print(crnt_text_vals)

def populate(records:list) -> None:
    '''Deletes content of the treeview and populate with records list'''
    #out_text.delete('2.0', END)
    for item in tree.get_children():
#        print(item)
        tree.delete(item)

    for record in records:
        # row = ''
        # for item in record:
        #     row = row + str(item) + ' | '
        #  out_text.insert(index = END, chars= row + '\n')
        # out_lb.insert(END, row)
        tree.insert('', 'end', values=record)

def select_all() -> None:
    '''Select all records from the database and add them to the text box'''
    res = select(select_all_records)
    populate(res)

def search() -> None:
    '''Searches DB based on non-empty Entries'''
    global is_verbose
    if validate_search():
        query_parts = []
        if title_val.get() != '':
            query_parts.append("title like '%" + title_val.get()+ "%'")

        if author_val.get() != '':
            query_parts.append("author like '%" + author_val.get() + "%'")

        if year_val.get() != '':
            query_parts.append("year like '%" + year_val.get()+ "%'")

        if isdn_val.get() != '':
            query_parts.append("isdn like '%" + isdn_val.get() + "%'")

        is_first = True
        where_query = ''
        if is_verbose: print(query_parts)
        for part in query_parts:
            if is_verbose: print('Part: ' + part)
            if not is_first:
                where_query = where_query + ' AND '
            where_query = where_query + part
            is_first = False

        result = select (query = select_all_records, where_clause =  where_query)
        populate(result)


def add() -> None:
    '''Adds Entry in DB based on non-empty Entries'''
    # print('Title: ' + title_val.get())
    # print('Author: ' + author_val.get())
    # print('Year: ' + year_val.get())
    # print('ISDN: ' + isdn_val.get())
    if validate_input():
        insert(id = get_next_id(), title = title_val.get(), author = author_val.get(), year = year_val.get(), isdn = isdn_val.get())

def update() -> None:
    '''Updates Selected record in DB based on non-empty Entries'''
    global crnt_text_vals
    # print(crnt_text_vals)
    # print(crnt_text_vals[0])
    if validate_input():
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute(" UPDATE " + books_db_name +
                       " SET title = '" + title_val.get() + "'," +
                       " author = '" + author_val.get() + "'," +
                       " year = '" + year_val.get() + "'," +
                       " isdn = '" + isdn_val.get() +
                       "' WHERE id = '" + str(crnt_text_vals[0]) + "';")
        conn.commit()
        conn.close()


def delete() -> None:
    '''Deletes Selected record in DB based on non-empty Entries'''
    global crnt_text_vals
    if validate_input():
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute(" DELETE FROM " + books_db_name +
                       " WHERE id=" + str(crnt_text_vals[0]) + ";")
        conn.commit()
        conn.close()

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

#author:
l_author = Label(main_win, text = 'Author', height=1 , width = 15)
l_author.grid(row = 0, column = 2)
author_val = StringVar()
e_author = Entry(main_win, textvariable = author_val)
e_author.grid(row = 0, column = 3, padx = 2)

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

# out_text = Text(main_win, bg = '#00F0A0', height = 15, width = 60)
# out_text.grid(row = 2, column = 0, columnspan = 3, rowspan = 6, pady = 10, padx = 2)
# heading = ' Id  |      Title     |     Author     |    Year    |      ISDN        '
# out_text.insert(END, heading)
# out_text.tag_add('heading', '1.0', '1.end')
# out_text.tag_config('heading', font='arial 14 bold')
#
# out_lb = Listbox(main_win,height = 15, width = 60)
# out_lb.grid(row = 9, column = 0, columnspan = 3, rowspan = 6, pady = 10, padx = 2)

headings = ['Id', 'Title', 'Author', 'Year', 'isdn']
tree =  Treeview(main_win, columns = headings, show='headings')
tree.grid(row = 2, column = 0, columnspan = 3, rowspan = 6)
for item in headings:
    tree.heading(item, text = item)
for col in headings:
    desired_width = 0
    if col == 'Id':
        desired_width = 30
    elif col == 'Title':
        desired_width = 200
    elif col == 'Author':
        desired_width = 170
    else:
        desired_width = 80
    tree.column(col, width = desired_width)

vertscrollbar = tkinter.ttk.Scrollbar(main_win, orient = 'vertical', command = tree.yview)
vertscrollbar.place(x = 560, y = 58, height = 205)
tree.bind('<ButtonRelease-1>', get_selected_item)
#main_win.update()
main_win.mainloop()
