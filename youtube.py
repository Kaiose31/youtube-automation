import selenium
import urllib.request,urllib.parse,json
import time
from selenium import webdriver



def look_for_new_video():
    api_key = "AIzaSyAw-_otx2SVq66S68TBWcEOdhD2XxWeVQQ"
    channel_id = "AIzaSyAG4S9ymL9jxZt_tThc5FCB7rV3E_ebAEE"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'


    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key,channel_id)
    inp = urllib.request.urlopen(url)
    resp = json.load(inp)

    vidId = resp['items'][0]['id']['videoId']

    with open('videoid.json','r') as json_file:
        data = json.load(json_file)
        if data['videoId']!= vidId:
            driver = webdriver.Firefox()
            driver.get(base_video_url+ vidId)
            video_exists = True

    if video_exists:
        with open('videoid.json','w') as json_file:
            data = {'videoId':vidId}
            json.dump(data,json_file)



try:
    while True:
        look_for_new_video()
        time.sleep(10)
    
except KeyboardInterrupt:
    print('stopping')











