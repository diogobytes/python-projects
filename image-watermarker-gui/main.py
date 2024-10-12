from PIL import Image, ImageDraw, ImageFont
from tkinter import *

class WatermarkApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Window Marker App")
        self.root.geometry('300x150')

        self.home_page()
        # Configure the grid to keep the label at the top
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.mainloop()

    def home_page(self):
        # Main frame
        self.mainframe = Frame(self.root)
        self.mainframe.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        self.mainframe.grid_rowconfigure(1, weight=0)  # Set weight to 0 to avoid stretching downwards
        self.mainframe.grid_columnconfigure(0, weight=1)
        # Label positioned at the top
        self.label = Label(self.mainframe, text="Add Watermark", font=("Arial", 14))
        self.label.grid(row=1, column=0, sticky="n")  # Align label to the top with padding

        self.button = Button(self.mainframe, text="Upload your image file", command=self.watermark_page)
        self.button.grid(row=3, column=0)
        # TODO: we need Continue button after the file has been uploaded.

    def watermark_page(self):
      self.watermark_page_mainframe = Frame(self.root)
      self.watermark_page_mainframe.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
      self.watermark_page_mainframe.grid_rowconfigure(1, weight=0)  # Set weight to 0 to avoid stretching downwards
      self.watermark_page_mainframe.grid_columnconfigure(0, weight=1)

      self.label_watermark = Label(self.watermark_page_mainframe, text="Insert the text you want to watermark", font=("Arial", 14))
      self.label_watermark.grid(row=1, column=0, sticky='n', pady=(0, 10))  # Add padding to separate label from the input field

      self.input_field = Entry(self.watermark_page_mainframe, font=('Arial', 14))
      self.input_field.grid(row=2, column=0, sticky='n', padx=10, pady=10)  # Ensure padding and stickiness

      # Add a button to continue after entering text
      self.continue_button = Button(self.watermark_page_mainframe, text="Continue")
      self.continue_button.grid(row=3, column=0, pady=10, sticky='n')  # Add continue button with padding


if __name__ == '__main__':
    watermark_gui = WatermarkApp()