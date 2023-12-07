import sqlite3
import Youtube_parcer
import folderParcer
import get
import config

class dataBase():
    def __init__(self, pathDb):
        self.pathDb = pathDb
        self.table1 = "Youtube"
        self.table2 = "NAS"

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

        c.execute(f'''
        
                CREATE TABLE IF NOT EXISTS {self.table1}
                (
                publishData DATA,
                FileName TEXT,
                chanel TEXT,
                key TEXT

        );''')

        # c.execute(f'''
        #
        #         CREATE TABLE IF NOT EXISTS {self.table2}
        #         (
        #         renderData DATA,
        #         fileName TEXT,
        #         ClipType INT,
        #         Newsman INT,
        #         Editor INT,
        #         key TEXT
        #         );''')
        #
        # c.execute('''
        #         CREATE TABLE IF NOT EXISTS emploues
        #         (id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         Name TEXT
        #         );''')
        #
        # c.execute('''
        #         CREATE TABLE IF NOT EXISTS VideoType
        #         (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         Name TEXT
        #         );''')

        c.execute('''
                       CREATE TABLE IF NOT EXISTS typeRelss
                       (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Name TEXT
                       );''')



        db.commit()
        print("TABLES CREATE COMPLITE!")

    def writheBdYoutube(self, list, path = None):
        if path == None:
            path = self.pathDb
        count = 0

        db = sqlite3.connect(path)
        c = db.cursor()

        for i in list:
            c.execute(f"SELECT FileName FROM {self.table1} WHERE FileName = '{i[1]}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO {self.table1} VALUES (?, ?, ?, ?)", (i[0], i[1], i[2],i[3]))
                count +=1
        db.commit()
        print(f'UPDATE TABLE {self.table1} ADD {count} RECORDS')

    def writheBdList(self, list, path = None):
        if path == None:
            path = self.pathDb
        count = 0



        db = sqlite3.connect(path)
        c = db.cursor()

        for i in list:
            nameDir = i[4]
            nameJurn = i[3]
            typVideo = i[2]

            key = i[5].replace(" ", "")
            key = key.replace("@SynoEAStream", "")
            key = key.replace("@SynoResource", "")

            if nameJurn != None:
                nameJurn = get.getId(nameJurn,config.user)
            if nameDir != None:
                nameDir = get.getId(nameDir,config.user)
            if typVideo != None:
                typVideo = get.getId(typVideo,config.types)
            if key == "v" or key == '+v':
                key = get.getId(key, config.typeRels)



            c.execute(f"SELECT key FROM {self.table2} WHERE key = '{key}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO {self.table2} VALUES (?, ?, ?, ?, ?, ?)", (i[0], i[1], typVideo, nameJurn, nameDir, key))
                count += 1

            db.commit()
        print(f'UPDATE TABLE {self.table2} ADD {count} RECORDS')



if __name__ == '__main__':
    db = dataBase(config.db)
    do = Youtube_parcer.Youtube(config.API_KEY2, config.DO)
    nm = Youtube_parcer.Youtube(config.API_KEY2, config.NM)
    # for i in do.getlist():
    #     print(i)
    db.writheBdYoutube(do.getlist())
    db.writheBdYoutube(nm.getlist())
    folder = folderParcer.Folder(config.path)

    # print(folder.getListFiles())
    db.writheBdList(folder.getListFiles())
    # db.createTables()


