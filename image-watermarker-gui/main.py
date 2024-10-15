import PIL.Image,PIL.ImageFont,PIL.ImageDraw
from tkinter import *
from tkinter import filedialog, messagebox

class WatermarkApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Window Marker App")
     
        window_width = 300
        window_height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.home_page()
        self.root.grid_rowconfigure(0, weight=1) 
        self.root.grid_columnconfigure(0, weight=1)
        self.root.mainloop()

    def home_page(self):
        self.mainframe = Frame(self.root)
        self.mainframe.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        self.mainframe.grid_rowconfigure(1, weight=0)
        self.mainframe.grid_columnconfigure(0, weight=1)

        self.label_homepage = Label(self.mainframe, text="Add Watermark", font=("Arial", 14))
        self.label_homepage.grid(row=1, column=0, sticky="n")
        
        self.button = Button(self.mainframe, text="Upload your image file", command=self.upload_image)
        self.button.grid(row=3, column=0)

    def upload_image(self):
        self.filepath = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("ICON","*.ico")]
        )
        if not self.filepath:
            messagebox.showwarning("File not selected", "Please upload an image file!")
        else:
            self.watermark_page()
    
    def watermark_page(self):
        self.clear_frame()
        
        # Create new Label and Entry widgets for text input
        self.label_watermark = Label(self.mainframe, text="Insert the text you want to watermark", font=("Arial", 14))
        self.label_watermark.grid(row=1, column=0, sticky='n', pady=(0, 10))
    
        self.text_field = Entry(self.mainframe, font=('Arial', 14))
        self.text_field.grid(row=2, column=0, sticky='n', padx=10, pady=10)
        
        # Button to continue to the next step
        self.continue_button = Button(self.mainframe, text="Continue", command=self.save_text_and_continue)
        self.continue_button.grid(row=3, column=0, pady=10, sticky='n')

        self.watermark_text = self.text_field.get()

    def save_text_and_continue(self):
        self.watermark_text = self.text_field.get()
        self.location_page()

    def location_page(self):
        self.clear_frame()
        self.label_coordinate_x = Label(self.mainframe, text="Coordinate X:")
        self.label_coordinate_x.grid(row=1, column=0, sticky='n', pady=(0, 10))

        self.coordinate_x_field = Entry(self.mainframe, font=('Arial', 14))
        self.coordinate_x_field.grid(row=1, column=1, sticky='n', pady=(0, 10))
        self.x_coordinate = self.coordinate_x_field.get()
        
        self.label_coordinate_y = Label(self.mainframe, text="Coordinate Y:")
        self.label_coordinate_y.grid(row=2, column=0, sticky='n', pady=(0, 10))

        self.coordinate_y_field = Entry(self.mainframe, font=('Arial', 14))
        self.coordinate_y_field.grid(row=2, column=1, sticky='n', pady=(0, 10))
        self.y_coordinate = self.coordinate_x_field.get()

        self.apply_button = Button(self.mainframe, text="Apply Watermark",command=self.apply_watermark)
        self.apply_button.grid(row=3, column=0, columnspan=2, pady=10)

    def apply_watermark(self):
        try:
            # Check if the input fields are valid and contain values
            x = int(self.coordinate_x_field.get())
            y = int(self.coordinate_y_field.get())
            text = self.watermark_text
          
            if not text:
                messagebox.showwarning("Input Error", "Please enter the text for the watermark.")
                return

            # Open the image
            im = PIL.Image.open(self.filepath)
            watermark_im = im.copy()
            
            # Font for the watermark (adjust the path if necessary)
            fnt = PIL.ImageFont.truetype("./Arial.ttf", 40)
            draw = PIL.ImageDraw.Draw(watermark_im)
            
            # Add the text as watermark
            draw.text((x, y), text, fill=(0, 0, 0), font=fnt)
            
            # Show the watermarked image
            watermark_im.show()

        except ValueError:
            messagebox.showerror("Invalid Input", "Coordinates must be integers.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def location_page(self):
        self.clear_frame()
        
        # Coordinate X input
        self.label_coordinate_x = Label(self.mainframe, text="Coordinate X:")
        self.label_coordinate_x.grid(row=1, column=0, sticky='n', pady=(0, 10))

        self.coordinate_x_field = Entry(self.mainframe, font=('Arial', 14))  # Reassign widget
        self.coordinate_x_field.grid(row=1, column=1, sticky='n', pady=(0, 10))

        # Coordinate Y input
        self.label_coordinate_y = Label(self.mainframe, text="Coordinate Y:")
        self.label_coordinate_y.grid(row=2, column=0, sticky='n', pady=(0, 10))

        self.coordinate_y_field = Entry(self.mainframe, font=('Arial', 14))  # Reassign widget
        self.coordinate_y_field.grid(row=2, column=1, sticky='n', pady=(0, 10))

        # Apply watermark button
        self.apply_button = Button(self.mainframe, text="Apply Watermark", command=self.apply_watermark)
        self.apply_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def clear_frame(self): 
      # Iterate through every widget inside the frame
      for widget in self.mainframe.winfo_children():
          widget.destroy()  # deleting widget


if __name__ == '__main__':
    WatermarkApp()