import sqlite3

class DBInterraction:

    def __init__(self):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  book_db (id INTEGER PRIMARY KEY, title TEXT,  author TEXT, year TEXT, isdn TEXT )')
        conn.commit()
        conn.close()

    def insert(self,title,author, year, isdn):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO book_db VALUES(NULL, ?, ?, ? , ?)", (title, author, year, isdn))
        conn.commit()
        conn.close()

    def search(self, title = '', author = '', year = '', isdn = ''):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book_db WHERE TITLE = ? OR AUTHOR = ? OR YEAR = ? OR ISDN = ?", (title, author, year, isdn))
        rows = cursor.fetchall()
        conn.close()
        return rows


    def  view(self):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book_db")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM book_db WHERE id = ?", (id, ))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isdn):
        conn = sqlite3.connect("../data/book_store_oop.dba")
        cursor = conn.cursor()
        cursor.execute("UPDATE book_db set title = ?, author = ?, year = ?, isdn = ? where id = ?", (title, author, year, isdn, id))
        conn.commit()
        conn.close()
