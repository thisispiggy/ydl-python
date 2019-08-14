import os
import youtube_dl


if not os.path.exists('images'):
    os.makedirs('images')
os.chdir('images')

options = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'bestaudio/best',  # choice of quality
    'extractaudio': False,        # only keep the audio
    'audioformat': "mp3",        # convert to mp3       # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': False,         # print a list of the formats to stdout and exit
}


def download_video(url):

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.extract_info(f'{url}', download=True)

def main():
    url = input("Enter url:\n")
    download_video(url)

if __name__ == '__main__':
    main()