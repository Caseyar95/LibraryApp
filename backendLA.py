import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, Read INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, Read=""):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, Read))
        self.conn.commit()

    def viewAll(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", Read=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR Read = ?", (title, author, year, Read))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, Read):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, Read = ? WHERE id = ?", (title, author, year, Read, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
