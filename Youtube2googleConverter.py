from pytube import YouTube
import pandas as pd
from tqdm import tqdm

data = pd.DataFrame(pd.read_csv("Robin2bin.csv"))
opener = 'https://www.youtube.com/watch?v='
count = 0
thumbnails = []
for i in tqdm(data['Links']):
    download = YouTube(opener + i)
    try:
        new_link = download.streams.filter(progressive=True,resolution='720p')[0].url
        thumbnail = download.thumbnail_url
        thumbnails.append(thumbnail)
        data._set_value(count,'Links',new_link)
    except Exception:
        new_link = download.streams.filter(progressive=True,resolution='360p')[0].url
        thumbnail = download.thumbnail_url
        thumbnails.append(thumbnail)
        data._set_value(count, 'Links', new_link)
    count += 1
data['Thumbnails'] = thumbnails
data.to_csv('Robin2bin_edited.csv')
print(data)