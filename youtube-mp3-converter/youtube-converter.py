import sys
import ssl
import os
import yt_dlp 
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
      ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        } ]
      }

      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(link)
      
    except Exception as e:
      print(f"Error {e}")

if __name__ == '__main__':
  YoutubeConverter()