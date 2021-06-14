# Import needed modules
import urllib.request as urllib
import json
from configparser import ConfigParser

# Define important things
config_object = ConfigParser()
config_object.read("config.ini")
yt = config_object["YOUTUBE"]

key = yt["api_key"]

# The function to grab the latest video from a specific channel
def getVid(channel):
    try:
        # Our api key
        apikey = key
        
        # Yt vid and search path
        video_url = 'https://www.youtube.com/watch?v='
        search_url = 'https://www.googleapis.com/youtube/v3/search?'
        
        # Load json of the channel page and get the latest video
        url = search_url+f'key={apikey}&channelId={channel}&part=snippet,id&order=date&maxResults=1'
        visit = urllib.urlopen(url)
        resp = json.load(visit)
        video_link = ""
        
        # Get the video url and return
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_link = video_url + i['id']['videoId']
                
        return video_link
    except Exception as e:
        print(e)
