import urllib.request as urllib
import json
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
yt = config_object["YOUTUBE"]

key = yt["youtube_api_key"]

def getVid(channel):
    try:
        apikey = key

        video_url = 'https://www.youtube.com/watch?v='
        search_url = 'https://www.googleapis.com/youtube/v3/search?'

        url = search_url+f'key={apikey}&channelId={channel}&part=snippet,id&order=date&maxResults=1'
        visit = urllib.urlopen(url)
        resp = json.load(visit)
        video_link = ""

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_link = video_url + i['id']['videoId']

        return video_link
    except Exception as e:
        print(e)
