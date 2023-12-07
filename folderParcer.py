import os
import config

from os.path import getctime
import datetime


class Folder():

    def __init__(self, path):
        self.path = path
        self.l = []
        self.g =[]

    def WalkFiles(self,current_path=None):
        if current_path is None:
            current_path = self.path

        for i in os.listdir(current_path):

            if os.path.isdir(current_path + '/' + i):
                self.WalkFiles(current_path + '/' + i)
            else:

                self.l.append(datetime.datetime.fromtimestamp(getctime(current_path + '/' + i)).strftime('%Y-%m-%d')+'_'+i)
        return self.l

    def getListFiles(self):

        for i in self.WalkFiles(self.path):
            s = i.replace(".mp4", "")
            s = s.split('_', 5)
            t = len(s)
            if t == 6:

                self.g.append(s)

        return self.g


if __name__ =='__main__':
    # pass
    folder = Folder(config.path)
    # print(folder.getListFiles(config.path))

    # for i in folder.WalkFiles():
    #     print(i)

    for i in folder.getListFiles():
        print(i)
