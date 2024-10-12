from PIL import Image, ImageDraw, ImageFont
from tkinter import *

class WatermarkApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Window Marker App")
     
        # Set initial window size
        window_width = 300
        window_height = 150

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center position
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        # Set the window size and position it at the center
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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

      self.input_field = Entry(self.watermark_page_mainframe, font=('Arial', 14),background="white",foreground="black")
      self.input_field.grid(row=2, column=0, sticky='n', padx=10, pady=10)  # Ensure padding and stickiness

      # Add a button to continue after entering text
      self.continue_button = Button(self.watermark_page_mainframe, text="Continue")
      self.continue_button.grid(row=3, column=0, pady=10, sticky='n')  # Add continue button with padding


if __name__ == '__main__':
    watermark_gui = WatermarkApp()