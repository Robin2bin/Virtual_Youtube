from flask import Flask, render_template
from pytube import YouTube
import pandas as pd

app = Flask(__name__)
opener = 'https://www.youtube.com/watch?v='

# Read the CSV file and store the video links and names in a list of tuples
df = pd.read_csv('Robin2bin_official_mail.csv')
video_links = []
for index, row in df.iterrows():
    link = opener + row['Links']
    name = row['Video_title']
    video_id = link.split('v=')[1]
    thumbnail_url = YouTube(link).thumbnail_url
    video_links.append((video_id, link, name, thumbnail_url))

# Define a route to display the videos
@app.route('/')
def show_videos():
    return render_template('videos.html', video_links=video_links)

# Define a new route to display an individual video page
@app.route('/video/<video_id>')
def show_video(video_id):
    for vid, link, name, thumbnail in video_links:
        if vid == video_id:
            try:
                new_link = YouTube(link)
                new_link = new_link.streams.filter(resolution="720p",progressive=True)[0].url
                print(YouTube(link).metadata)
                return render_template('video.html', link=new_link, name=name, width="1000",height="720")
            except Exception:
                new_link = YouTube(link)
                new_link = new_link.streams.filter(resolution="360p", progressive=True)[0].url
                return render_template('video.html', link=new_link, name=name, width="640",height="480")

if __name__ == '__main__':
    app.run(debug=True)
