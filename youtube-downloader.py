from pytube import YouTube
from pytube import Playlist


url = 'https://www.youtube.com/playlist?list=PLZcHRARJMstUv736u_2__KDXUUVHneBFb'

yt_obj = Playlist(url=url)

for url in yt_obj.video_urls:
    print('{}'.format(url.title()))
    video = YouTube(url)
    
    best_video = video.streams.get_highest_resolution()
    
    best_video.download()
    
    print('Baixado')
    
    
   
