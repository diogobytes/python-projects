import pyautogui
import webbrowser
import time
from PIL import Image

URL = "https://elgoog.im/dinosaur-game/"

def is_obstacle_present():
    # Capture a screenshot of the game region
    game_region = pyautogui.screenshot(region=(800, 350, 450, 300))
    # Convert the screenshot to a format we can manipulate (Pillow Image)
    game_region = game_region.convert('RGB')
    game_region.show()

    # Check multiple pixels within the screenshot for color changes
    for x in range(420, 430, 1):  # Check pixels towards the right edge
        for y in range(270, 300, 1):  # Check pixels towards the bottom edge
            pixel_color = game_region.getpixel((x, y))  # Get the color of the pixel

            # Detect if the pixel is dark (which could indicate an obstacle)
            if pixel_color[0] < 100 and pixel_color[1] < 100 and pixel_color[2] < 100:  # RGB check for dark color
                return True  # Return True if any dark pixel is found

    return False  # Return False if no dark pixels are found

def main():
    webbrowser.open(URL)  
    time.sleep(3)
    pyautogui.press('space')  # Jump to start the game
    n = 0
    while n < 16:  # Keep running indefinitely
        if is_obstacle_present():
            pyautogui.press('space')  # Jump if an obstacle is detected
        time.sleep(0.1)  # Adjust the sleep time as necessary
        n +=1

if __name__ == "__main__":
    main()