import sqlite3

import folderParcer
import get
import config

class dataBase():
    def __init__(self, pathDb):
        self.pathDb = pathDb


    def createTableYoutube(self):
        db = sqlite3.connect(self.pathDb)
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS YoutubeVideo 
           (data DATA, 
           name NVARCHAR(256), 
           url TEXT, 
           chanel TEXT,
           key TEXT)''')

        db.commit()

    def createTableNAS(self):

        db = sqlite3.connect(self.pathDb)
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS VideoStorage
        (
        NameFile TEXT,
        TypeClip TEXT,
        NameJurn TEXT,
        NameDirector TEXT,
        key TEXT,
        FOREIGN KEY (key) REFERENCES YoutubeVideo(key)

        )''')

        db.commit()

    def writheBdYoutube(self, list):
        db = sqlite3.connect(self.pathDb)
        c = db.cursor()
        for i in list:
            c.execute(f"SELECT name FROM YoutubeVideo WHERE name = '{i[1]}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO YoutubeVideo VALUES (?, ?, ?, ?, ?)", (i[0], i[1], i[2], i[3], i[4]))
        db.commit()

    def writheBdListVideostorage(self, list):
        db = sqlite3.connect(self.pathDb)
        c = db.cursor()
        for i in list:

            nameDir = i[3]
            nameJurn = i[2]

            typVideo = i[1]

            key = i[4].replace(" ", "")
            key = key.replace("@SynoEAStream", "")
            key = key.replace("@SynoResource", "")

            if get.getId(nameJurn, config.list) != None:
                nameJurn = get.getId(nameJurn, config.list)
            if get.getId(nameDir, config.list) != None:
                nameDir = get.getId(nameDir, config.list)
            if get.getId(typVideo) != None:
                typVideo = get.getId(typVideo)

            if typVideo == "НМ" or typVideo == "ДО" or typVideo == "ДП":
                typVideo = "СЮЖ"

            c.execute(f"SELECT key FROM VideoStorage WHERE key = '{key}'")
            if c.fetchone() is None:
                c.execute(f"INSERT INTO VideoStorage VALUES (?, ?, ?, ?, ?)", (i[0], typVideo, nameJurn, nameDir, key))
        db.commit()



if __name__ == '__main__':

    pass

