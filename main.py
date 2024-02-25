import Youtube_parcer
import BD
import config
import folderParcer


DO = Youtube_parcer.Youtube2(config.API_KEY, config.DO).getlist()
NM = Youtube_parcer.Youtube2(config.API_KEY, config.NM).getlist()
DP = Youtube_parcer.Youtube2(config.API_KEY, config.DP).getlist()

writeYoutube = BD.AppEndYoutube2(config.db)
writeNAS = BD.AppEndNAS(config.db)


print("DO")
writeYoutube.writheBdYoutube(DO)

print("=====================================")

print("NM")
writeYoutube.writheBdYoutube(NM)

print("=====================================")

print("DP")
writeYoutube.writheBdYoutube(DP)

getFilesNikita = folderParcer.Folder(config.Nikita).getListFiles()
getFilesIgor = folderParcer.Folder(config.Igor).getListFiles()
getFilesJenya = folderParcer.Folder(config.Jenya).getListFiles()
getFilesKostya = folderParcer.Folder(config.Kostya).getListFiles()
getFilesTaylor = folderParcer.Folder(config.Taylor).getListFiles()


print("=====================================")

print("Nikita")
writeNAS.writeBdNas(getFilesNikita)

print("=====================================")

print("Igor")
writeNAS.writeBdNas(getFilesIgor)

print("=====================================")

print("Jenya")
writeNAS.writeBdNas(getFilesJenya)

print("=====================================")

print("Kostya")
writeNAS.writeBdNas(getFilesKostya)

print("=====================================")

print("Max")
writeNAS.writeBdNas(getFilesTaylor)

print("=====================================")


if __name__=="__main__":
    pass
