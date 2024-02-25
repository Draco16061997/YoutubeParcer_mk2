import sqlite3
import get
import Youtube_parcer
import config
import folderParcer


class DB():
    def __init__(self, path):
        self.path = path


    def createDb(self, path = None):


        db = sqlite3.connect(self.path)

        db.commit()


        print("DB OK!")

    def CreateTableYoutube(self):


        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(
            f'''
            CREATE TABLE IF NOT EXISTS Youtube
                (
                publishData DATA,
                FileName TEXT,
                chanel TEXT,
                key TEXT);''')
        db.commit()

        print("Youtube table is create!")

    def CreateTableNas(self):
        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(
            f'''
                    CREATE TABLE IF NOT EXISTS NAS
                        (
                        RenderData DATA,
                        FileName TEXT,
                        TypeClip TEXT,
                        Newsman TEXT,
                        Editor TEXT,
                        key TEXT);
        ''')
        db.commit()

        print("NAS table is create!")

    def CreateTableEmploues(self):
        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(
            f'''
                            CREATE TABLE IF NOT EXISTS Emoloues (
                            ID INT PRIMARY KEY NOT NULL,
                            Name TEXT,
                            PsevdoName TEXT
                            );
                ''')
        db.commit()

        print("Emplouse table is create!")

    def CreateTableProduct(self):
        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(
            f'''
                                    CREATE TABLE IF NOT EXISTS Products (
                                    ID INT PRIMARY KEY NOT NULL,
                                    Name TEXT,
                                    PsevdoName TEXT 
                                    );
                        ''')
        db.commit()

        print("Products table is create!")


class AppEndYoutube(DB):
    def writheBdYoutube(self, list):

        count = 0

        db = sqlite3.connect(self.path)
        c = db.cursor()

        for i in list:
            c.execute(f"SELECT FileName FROM Youtube WHERE FileName = '{i[1]}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO Youtube VALUES (?, ?, ?, ?)", (i[0], i[1], i[2],i[3]))
                count +=1
        db.commit()
        print(f'UPDATE TABLE FROM Youtube ADD {count} RECORDS')

class AppEndNAS(DB):

    def ReadEmplouse(self):
        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(f'''
        SELECT * FROM Emoloues ''')
        rows = c.fetchall()
        list = []

        for i in rows:
            l=(i[0],i[1], i[2].split(", "))
            list.append(l)
        db.close()
        return list


    def ReadProducts(self):
        db = sqlite3.connect(self.path)
        c = db.cursor()

        c.execute(f'''
                SELECT * FROM Products ''')
        rows = c.fetchall()
        list = []
        for i in rows:
            l = (i[0], i[1], i[2].split(", "))
            list.append(l)

        db.close()
        return list


    def writeBdNas(self,l):
        count = 0
        db = sqlite3.connect(self.path)
        c = db.cursor()

        for i in l:

            nameDir = i[4]
            nameJurn = i[3]
            typVideo = i[2]
            key = i[5]

            key = i[5].replace(" ", "")
            key = key.replace("@SynoEAStream", "")
            key = key.replace("@SynoResource", "")

            if nameJurn != None:
                nameJurn = get.getId(nameJurn,config.user)
            if nameDir != None:
                nameDir = get.getId(nameDir,config.user)
            if typVideo != None:
                typVideo = get.getId(typVideo, config.products)
            if key == "v" or key == 'V' or key == "v.ewc2" or key == 'V.ewc2':
                key = 0
            if key == "+v" or key == '+V'or key == "+v.ewc2" or key == '+V.ewc2':
                key = 1



            c.execute(f"SELECT key FROM NAS WHERE key = ? AND FileName = ?", (key, i[1]))
            if c.fetchone() is None:
                c.execute(f"INSERT INTO NAS VALUES (?, ?, ?, ?, ?, ?)",
                          (i[0], i[1], typVideo, nameJurn, nameDir, key))
                count += 1

            db.commit()
        print(f'UPDATE TABLE NAS ADD {count} RECORDS')


class AppEndYoutube2(AppEndYoutube):
    def writheBdYoutube(self, list):

        count = 0

        db = sqlite3.connect(self.path)
        c = db.cursor()

        for i in list:
            c.execute(f"SELECT FileName FROM Youtube WHERE FileName = '{i[1]}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO Youtube VALUES (?, ?, ?, ?)", (i[0], i[1], i[2], i[3]))
                c.execute(f"INSERT INTO DURATION VALUES (?, ?)", (i[4], i[3]))
                count += 1

        db.commit()
        print(f'UPDATE TABLE FROM Youtube ADD {count} RECORDS')


if __name__ == "__main__":
    pass


    add = AppEndYoutube2(config.db)

    add.writheBdYoutube(Youtube_parcer.Youtube2(config.API_KEY2,config.DO).getlist())







   

