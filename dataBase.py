import sqlite3
import Youtube_parcer
import folderParcer
import get
import config

class dataBase():
    def __init__(self, pathDb, YoutubeTable, NasTable):
        self.pathDb = pathDb
        self.table1 = YoutubeTable
        self.table2 = NasTable

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
                typVideo = get.getId(typVideo, config.products)
            if key == "v" or key == '+v':
                key = get.getId(key, config.typeRels)



            c.execute(f"SELECT key FROM {self.table2} WHERE key = '{key}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO {self.table2} VALUES (?, ?, ?, ?, ?, ?)", (i[0], i[1], typVideo, nameJurn, nameDir, key))
                count += 1

            db.commit()
        print(f'UPDATE TABLE {self.table2} ADD {count} RECORDS')

    def ReadBd(self,NameUser = None, FromTable = None, JoinTable = None, dataIn = None, dataOut = None, path = None):
        if path == None:
            path = self.pathDb

        if FromTable == None:
            FromTable = self.table1

        if JoinTable == None:
            JoinTable = self.table2


        # реализация ограничение поиска по периоду дат
        if dataIn != None and dataOut != None:
            where = f'WHERE data BETWEEN {dataIn} AND {dataOut}'
        elif dataIn != None and dataOut != None and NameUser != None:
            where = f'WHERE NameJurn = {NameUser} OR NameDirector = {NameUser} AND data BETWEEN {dataIn} AND {dataOut}'
        else:
            where = ''



        db = sqlite3.connect(path)
        c = db.cursor()

        c.execute(f'''SELECT *
                    FROM {FromTable}
                    LEFT JOIN {JoinTable} ON {FromTable}.key = {JoinTable}.key
                    {where} 
                    LEFT JOIN typeVideo ON VideoStorage.TypeClip =typeVideo.id
                    LEFT JOIN emploues AS j ON j.id = VideoStorage.NameJurn
                    LEFT JOIN emploues AS d ON d.id = VideoStorage.NameDirector

                    ORDER BY data DESC''')

        rows = c.fetchall()
        db.close()
        return rows



if __name__ == '__main__':
    # pass
    db = dataBase(config.db, "YoutubeVideo","VideoStorage")
    # do = Youtube_parcer.Youtube(config.API_KEY2, config.DO)
    # nm = Youtube_parcer.Youtube(config.API_KEY2, config.NM)
    #
    # db.writheBdYoutube(do.getlist())
    # db.writheBdYoutube(nm.getlist())
    # folder = folderParcer.Folder(config.path)
    #
    # db.writheBdList(folder.getListFiles())
    for i in db.ReadBd():
        print(i)



