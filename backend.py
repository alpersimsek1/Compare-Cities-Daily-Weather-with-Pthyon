import sqlite3
class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS city (id INTEGER PRIMARY KEY, city_name TEXT, datenow TEXT, temperature INTEGER, temp_min INTEGER, temp_max INTEGER)")
        self.conn.commit()

    def insert(self,city_name,datenow,temperature,temp_min,temp_max):
        self.cur.execute("INSERT INTO city VALUES (NULL,?,?,?,?,?)",(city_name,datenow,temperature,temp_min,temp_max))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM city")
        rows=self.cur.fetchall()
        return rows

    def search(self,city_name="",datenow=""):
        self.cur.execute("SELECT * FROM city WHERE city_name=? OR datenow=? ",(city_name,datenow))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM city WHERE id=?",(id,))
        self.conn.commit()

    def accessing_items_in_db(self,a):
        self.conn = sqlite3.connect('cities.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM city")
        rows = self.cur.fetchall()
        li = []
        if a == "temperature":
            for item in rows:
                li.append(item[3])
        elif a == "city_name":
            for item in rows:
                li.append(item[1])
        elif a == "datenow":
            for item in rows:
                li.append(item[2])
        else:
            print("Please try again with: 'city_name' or 'datenow' ")
        return li

    def __del__(self):
        self.conn.close()

