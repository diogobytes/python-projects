# This project is to create a bot to play the Google Dino Game!
# Play here: https://elgoog.im/dinosaur-game/

# Documentation
#https://pypi.org/project/Pillow/
#https://pyautogui.readthedocs.io/en/latest/

import pyautogui
import webbrowser
import time
from PIL import Image, ImageChops

URL = "https://elgoog.im/dinosaur-game/"

def is_obstacle_present():
  game_region = pyautogui.screenshot(region=(600,150,300,200))
  obstacle_image = Image.open('./image.png')
  diff = ImageChops.difference(game_region,obstacle_image)
  if diff.getbbox() is None:
    return False
  else: 
    return True

def main():

  webbrowser.open(URL)  
  time.sleep(3)
  pyautogui.press('space')  # Jump if the obstacle is detected
  while True:
    if is_obstacle_present():
      pyautogui.press('space')  # Jump if the obstacle is detected
    time.sleep(0.1)
  
if __name__ == "__main__":
  main()