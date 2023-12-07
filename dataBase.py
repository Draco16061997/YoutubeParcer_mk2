import sqlite3
import Youtube_parcer
import folderParcer
import get
import config

class dataBase():
    def __init__(self, pathDb):
        self.pathDb = pathDb

    def createDb(self, path = None):
        if path == None:
            path = self.pathDb

        db = sqlite3.connect(path)

        db.commit()
        print("DB OK!")


    def createTables(self, path = None):

        if path == None:
            path = self.pathDb

        db = sqlite3.connect(path)
        c = db.cursor()

        c.execute('''
        
                CREATE TABLE IF NOT EXISTS Youtube
                (
                publishData DATA,
                FileName TEXT,
                chanel TEXT,
                key TEXT

        );''')

        c.execute('''

                CREATE TABLE IF NOT EXISTS FilesOnNas
                (
                renderData DATA,
                fileName TEXT,
                ClipType INT,
                Newsman INT,
                Editor INT,
                key TEXT
                );''')

        c.execute('''
                CREATE TABLE IF NOT EXISTS emploues 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT
                );''')

        c.execute('''
                CREATE TABLE IF NOT EXISTS VideoType
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT
                );''')




        db.commit()
        print("TABLES CREATE COMPLITE!")

    def writheBdYoutube(self, list, path = None):
        if path == None:
            path = self.pathDb

        db = sqlite3.connect(path)
        c = db.cursor()

        for i in list:
            c.execute(f"SELECT FileName FROM Youtube WHERE FileName = '{i[1]}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO Youtube VALUES (?, ?, ?, ?)", (i[0], i[1], i[2],i[3]))
            db.commit()




if __name__ == '__main__':
    db = dataBase(config.db)
    do = Youtube_parcer.Youtube(config.API_KEY2, config.DO)
    # for i in do.getlist():
    #     print(i)
    # db.writheBdYoutube(do.getlist())

    # db.writheBdYoutube()




