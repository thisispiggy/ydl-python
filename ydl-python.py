import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})

def download_video(url):

    with ydl:
        ydl.extract_info(f'{url}', download=True)

def main():
    url = input("Enter url:\n")
    download_video(url)

if __name__ == '__main__':
    main()