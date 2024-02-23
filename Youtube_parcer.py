from googleapiclient.discovery import build
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



class Youtube2(Youtube):
    def __init__(self, API_KEY, ID_CHANEL):
        self.API_KEY = API_KEY
        self.ID_CHANEL = ID_CHANEL

    def get_video_length(self,  video_id):


        # Создание объекта YouTube Data API
        youtube = service = build('youtube', 'v3', developerKey=self.API_KEY)

        # Запрос к API для получения информации о видео
        request = youtube.videos().list(
            part='contentDetails',
            id=video_id
        )

        response = request.execute()

        # Извлечение продолжительности видео из ответа


        duration = response['items'][0]['contentDetails']['duration'].replace("PT","")
        duration = duration.replace("M", " хв ")
        duration = duration.replace("S", " c")

        return duration

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
        num = 0

        for i in l:
            titleChanel = i['snippet']['channelTitle']
            title = i['snippet']['title'].replace("&quot;", "")

            dataPublish = i['snippet']['publishedAt'].split('T')[0]
            url = keyUrl + i['id']['videoId']

            key = i['id']['videoId']
            #
            dur = self.get_video_length(key)

            youYubeList.append((dataPublish, title, titleChanel, key, dur))
            num +=1
            print(num)

        return youYubeList





if __name__ == '__main__':
    do = Youtube2(config.API_KEY2, config.DO)
    for i in do.getlist():
        print(i)



