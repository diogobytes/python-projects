import sys
from pytube import YouTube
import ffmpeg
import ssl
"""
Usage: python3 youtube-converter.py {--playlist} {--link}"
"""


class YoutubeConverter:
  
  def __init__(self):
    print("[*] Welcome to Youtube Converter to MP3")
    ssl._create_default_https_context = ssl._create_stdlib_context
    if len(sys.argv) == 1:
      print("[*] Usage: python3 youtube-converter.py {--playlist} {--link}")
    else:
      if sys.argv[1] == '--playlist':
        print("Playlist")
      if sys.argv[1] == '--link':
        self.convert_link(sys.argv[2])
      else: 
        print("Error: provide a valid argument")
  def convert_link(self,link):
    try:
      yt_download = YouTube(link)
      audio_streams = yt_download.streams.filter(only_audio=True)
      if not audio_streams:
        print("Error: no audio from youtube video.")
        return
    except Exception as e:
      print(f"Error {e}")
      
   

  def convert_playlist(self):
    print



if __name__ == '__main__':
  YoutubeConverter()