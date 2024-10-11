# Desktop  Application with a GUI where you can upload an image and use python to add a watermark logo/text.

# https://pypi.org/project/Pillow/
#https://docs.python.org/3/library/tkinter.html

from PIL import Image,ImageDraw, ImageFont
from tkinter import *


class WatermarkApp:
  def __init__(self):
    self.root = Tk()
    self.root.title("Window Marker App")
    self.root.geometry('300x300')
    # Main frame
    self.mainframe = Frame(self.root,bg="white")
    self.mainframe.grid(column=0,row=0,stick="nsew",padx=10,pady=10)
    self.label = Label(self.mainframe, text="Upload your image file", font=("Arial", 14))
    self.label.grid(row=1,column=0)
    self.root.mainloop()
    



if __name__ == '__main__':
  watermark_gui = WatermarkApp()
  
  
  # im = Image.open('./matrix.jpg')
  # watermark_im = im.copy()
  # fnt = ImageFont.truetype("./Arial.ttf", 40)

  # draw = ImageDraw.Draw(watermark_im)
  # draw.text((0,0),"Diogo Guedes",fill=(0, 0, 0, 0),font=fnt)
  # watermark_im.show()

