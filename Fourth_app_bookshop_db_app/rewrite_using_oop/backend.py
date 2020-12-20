import sqlite3

class DBInterraction:

    def __init__(self, dblocation):
        self.conn = sqlite3.connect(dblocation)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS  book_db (id INTEGER PRIMARY KEY, title TEXT,  author TEXT, year TEXT, isdn TEXT )')
        self.conn.commit()

    def insert(self,title,author, year, isdn):
        self.cursor.execute("INSERT INTO book_db VALUES(NULL, ?, ?, ? , ?)", (title, author, year, isdn))
        self.conn.commit()

    def search(self, title = '', author = '', year = '', isdn = ''):
        self.cursor.execute("SELECT * FROM book_db WHERE TITLE = ? OR AUTHOR = ? OR YEAR = ? OR ISDN = ?", (title, author, year, isdn))
        rows = self.cursor.fetchall()
        return rows

    def  view(self):
        self.cursor.execute("SELECT * FROM book_db")
        rows = self.cursor.fetchall()
        return rows

    def delete(self,id):
        self.cursor.execute("DELETE FROM book_db WHERE id = ?", (id, ))
        self.conn.commit()

    def update(self, id, title, author, year, isdn):
        self.cursor.execute("UPDATE book_db set title = ?, author = ?, year = ?, isdn = ? where id = ?", (title, author, year, isdn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
