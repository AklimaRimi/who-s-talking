from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube
import time
import os
import subprocess
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}


lists = [
    ['Oprah Winfrey' , 'https://www.youtube.com/watch?v=8q-rOGqVVG4&list=PLlYQEunSGNIpDvgBtnsAa0_b_0nX7ihC_'],
    ['Eric Thomas' , 'https://www.youtube.com/watch?v=W7WwURsaU-s&list=PLVbZK3ubBgIYaDu-CtvvvvHfi7TzITJrD'],
    ['Les Brown' , 'https://www.youtube.com/watch?v=ulCsBqBHq1c&list=PL5r0bR7hFYGJxnPjqiwf8mh3Iumbjo1oV'],
    ['Simon Sinek','https://www.youtube.com/watch?v=ReRcHdeUG9Y&list=PL9NJg2uW-tXsgicsHh8d9wfAlrqvwE7ri'],
    ['Brene Brown','https://www.youtube.com/watch?v=psN1DORYYV0&list=PL_8y1sfjDBgFgTROXTsIIielUMh79bK2S'],
    ['Gary Vee','https://www.youtube.com/watch?v=gKTYWngIGAI&list=PLfA33-E9P7FD_gqmhbHOmTZeFyjBt6n7-'],
    ['Mel Robbins','https://www.youtube.com/watch?v=1dAN6SQ5J-A&list=PLhW2xUEb-B-ZEzpe_YKNv8f3Uw_xkZO1P'],
    ['Eckhart Tolle','https://www.youtube.com/watch?v=PIyzvKq19gg&list=PLBfwuuKtlF5p6xyIupIENXTiFDTsoRZsg'],
    ['Nick Vujicic','https://www.youtube.com/watch?v=6P2nPI6CTlc&list=PLJLmvG8JoVmkzHwJzXu3f7cLXbx8JHcMJ'],
    ['Rabin Sharma','https://www.youtube.com/watch?v=UkhE_afMsDc&list=PLmqIZxMeCGZovrksUaGYyjntM_svtLXnx'],
    ['Jay Shetty','https://www.youtube.com/watch?v=gxURcDSeRns&list=PLb0C_I-k2Ph9bsj_cGBGmidR8749g4XKU'],
]

driver = webdriver.Chrome()
for l in lists[10:]:
    driver.get(l[1]) 
    os.mkdir(f'{l[0]}')
    time.sleep(5)
    vid_links_container = driver.find_element(By.XPATH,'//div[contains(@class,"playlist-items style-scope ytd-playlist-panel-renderer") and contains(@id, "items")]')
    links = vid_links_container.find_elements(By.XPATH,'//a[@id="wc-endpoint"]')
    cnt = 0
    for link in links:
        print(link.get_attribute('href'))
        yt = link.get_attribute('href')
        print(yt)
        vid = YouTube(yt)
        try:
            path = vid.streams.filter(only_audio=True).first().download(output_path=f'{l[0]}')
            
            os.rename(path,f'{path[:-3]}wav')
        except:
            print('Error')
            continue
        
        # subprocess.call(['ffmpeg','-i',out_file,f'{out_file[:-3]}wav'])
        




              
