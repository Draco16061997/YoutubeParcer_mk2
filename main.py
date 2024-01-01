import Youtube_parcer
import BD
import config
import folderParcer


DO = Youtube_parcer.Youtube(config.API_KEY, config.DO).getlist()
NM = Youtube_parcer.Youtube(config.API_KEY, config.NM).getlist()
DP = Youtube_parcer.Youtube(config.API_KEY, config.DP).getlist()

writeYoutube = BD.AppEndYoutube("/Users/mikita/Main/PythonProjects/YoutubeParcer_mk2/testdb.db")
writeNAS = BD.AppEndNAS("/Users/mikita/Main/PythonProjects/YoutubeParcer_mk2/testdb.db")



writeYoutube.writheBdYoutube(DO)
writeYoutube.writheBdYoutube(NM)
writeYoutube.writheBdYoutube(DP)

getFiles = folderParcer.Folder(config.path).getListFiles()

writeNAS.writeBdNas(getFiles)



if __name__=="__main__":
    pass
