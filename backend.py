import sqlite3

class database():
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS newdatabase (id INTEGER primary key , name text , lastname text , passin integer , dorename text)')
        self.con.commit()

    def insert(self,name,lastname,passin,dorename):
        self.cur.execute('INSERT INTO newdatabase VALUES(Null,?,?,?,?)',(name,lastname,passin,dorename))
        self.con.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM newdatabase")
        rows = self.cur.fetchall()
        return rows
        
    def remove(self,id):
        self.cur.execute('DELETE FROM newdatabase WHERE id = ?',(id,))
        self.con.commit()