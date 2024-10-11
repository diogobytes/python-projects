# Desktop  Application with a GUI where you can upload an image and use python to add a watermark logo/text.

# https://pypi.org/project/Pillow/
#https://docs.python.org/3/library/tkinter.html

from PIL import Image,ImageDraw, ImageFont




if __name__ == '__main__':
  im = Image.open('./matrix.jpg')
  watermark_im = im.copy()
  fnt = ImageFont.truetype("./Arial.ttf", 40)

  draw = ImageDraw.Draw(watermark_im)
  draw.text((0,0),"Diogo Guedes",fill=(0, 0, 0, 0),font=fnt)
  watermark_im.show()

