
from googleapiclient.discovery import build
import google.oauth2

import config

class Youtube():
    def __init__(self, API_KEY, ID_CHANEL):
        self.API_KEY = API_KEY
        self.ID_CHANEL = ID_CHANEL

    def getlist(self):
        keyUrl = "https://www.youtube.com/watch?v="

        service = build('youtube', 'v3', developerKey=self.API_KEY)

        r = service.search().list(
            channelId=self.ID_CHANEL,
            part="snippet",
            type="video",
            order="date",
            maxResults='50'
        ).execute()

        dat = r['items'][0]['snippet']['publishedAt']
        title = r['items'][0]['snippet']['title']
        l = r['items']
        youYubeList = []

        for i in l:
            titleChanel = i['snippet']['channelTitle']
            title = i['snippet']['title'].replace("&quot;", "")

            dataPublish = i['snippet']['publishedAt'].split('T')[0]
            url = keyUrl + i['id']['videoId']

            key = i['id']['videoId']
            #
            youYubeList.append((dataPublish, title, titleChanel, key))

        return youYubeList






if __name__ == '__main__':
    # pass
    do = Youtube(config.API_KEY2, config.NM)

    for i in do.getlist():
        print(i)