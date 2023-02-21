from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

image_paths=""


### ---------------------------- DEF ------------------------------- ###

def browseFiles():
    global image_paths
    image_paths = filedialog.askopenfilenames(initialdir= "/", title= "Select Image Files", filetypes= ((('png file', '*.png'),('jpg file', '*.jpg'),('jpeg file', '*jpeg'),('all file','*.*'))))

    # Display Selected image on the UI. If multiple images are selected, display the first one.
    image= Image.open(image_paths[0])
    image.thumbnail((150,150))
    photo= ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image=photo


def addWatermark():
    global image_paths

    # Display Error message if image is not selected.
    if not image_paths:
        messagebox.showwarning("Error", "Please select at least one image.")
        return

    # Open multiple images to insert watermarks. Convert images to RGBA Format.
    for image_path in image_paths:
        image=Image.open(image_path).convert("RGBA")

    # Create transparent empty image canvases for watermark texts. The canvases are same in their size with original images.
        watermark_canvas=Image.new("RGBA", image.size, (255,255,255,0))
        draw=ImageDraw.Draw(watermark_canvas)

    # Set watermark font color
    if font_color.get() == 1:
        watermark_fontcolor = 'black'
    else:
        watermark_fontcolor='white'

    # Calculate & Set watermark font sizes based on the sizes of the images
    w, h= image.size
    x, y= int(w/2), int(h/2)
    if x>y:
        font_size=y
    elif y>x:
        font_size=x
    else:
        font_size=x

    # Set font style and size. Default arial.ttf in the root folder.
    font= ImageFont.truetype("arial.ttf", int(font_size / 6))
 
    # Set watermark sizes & contents
        text_width, text_height = draw.textsize(watermrktxt_entry.get(), font=font)

    # Set watermark position based on the size of each images
        if position == 'nw':
            watermark_position = (0, 0)
        elif position == 'ne':
            watermark_position = (w - text_width, 0)
        elif position == 'sw':
            watermark_position = (0, h - text_height)
        else:
            watermark_position = (w - text_width, h - text_height)

        # Insert watermark in set position.
        draw.text(watermark_position, watermark_entry.get(), fill=watermark_fontcolor, font=font)
        watermarked_image=Image.alpha_composite(image,watermark_canvas)

        # Save watermarked images in original image path as 'original file name' + 'watermarked'
        directory = os.path.dirname(image_path)
        file_name, file_ext = os.path.splitext(os.path.basename(image_path))
        save_path = os.path.join(directory, file_name + '_watermarked' + file_ext)

        # display message window if work completed.
        if save_path:
            watermarked_image.save(save_path)
        messagebox.showinfo("Success", "Watermark added and image saved successfully.")


### ---------------------------- UI SETUP ------------------------------- ###

window = Tk()
window.title("Watermark creator")
window.config(padx=50, pady=50)

canvas = Canvas(height=400, width=400)
canvas.grid(row=0, column=0)

#1 Image label. Display text "Images:". If image is selected in browseFiles(), replace it with the image.
image_label=Label(window, text="Images:")
image_label.grid(row=0, column=0, rowspan=10, columnspan=2, padx=10, pady=10)

#2-1 Image file label. Display text "Image files".
imagefile_label=Label(window, text="Image Files")
imagefile_label.grid(row=0, column=2, columnspan=2)

#2-2 Image Search button. Open file browser window.
imgsearch_btn = Button(text="Search Image Files", command=browseFiles)
imgsearch_btn.grid(row=1, column=2, columnspan=2)

#3-1 Watermark text label. Display text "Watermark Text".
watermrktxt_label = Label(window, text="Watermark Text")
watermrktxt_label.grid(row=2, column=2, columnspan=2)

#3-2 Watermark Entry field. Type in text as watermark.
watermrktxt_entry = Entry()
watermrktxt_entry.insert(0, "Type Your Watermark Text")
watermkrktxt_entry.grid(row=3, column=2, columnspan=2)

#4-1 Watermark font color label. Display text "Watermark Font Color" 
watermrkcolor_lable = Label(window, text="Watermark Font Color")
watermrkcolor_label.grid(row=4, column=2, columnspan=2)

#4-2 Watermark font color Radio button. Choose between black or whote.
font_color = IntVar()
font_color.set(1)
black_rb = Radiobutton(window, text="Black", variable=font_color, value=1)
black_rb.grid(row=5, column=2)
white_rb = Radiobutton(window, text="White", variable=font_color, value=2)
white_rb.grid(row=5, column=3)

#5-1 Watermark position label. Display text "Watermark Position"
watermrkpos_label = Label(window, text="Watermark Position")
watermrkpos_label.grid(row=6, column=2, columnspan=2)

#5-2 Watermark position radio buttons(total 4). 
position = IntVar()
position.set(4)
postionrb_nw = Radiobutton(window, text="Top-Left", variable=position, value=1)
postionrb_nw.grid(row=7, column=2)
positionrb_ne = Radiobutton(window, text="Top-Right", variable=position, value=2)
positionrb_ne.grid(row=7, column=3)
positionrb_sw = Radiobutton(window, text="Bottom-Left", variable=position, value=3)
positionrb_sw.grid(row=8, column=2)
positionrb_se = Radiobutton(window, text="Bottom-right", variable=position, value=4)
positionrb_se.grid(row=8, column=3)

# 6 Create Watermarked image Button.
watermrk_btn = Button(text="Create Watermarked image", command=addWatermark)
watermrk_btn.grid(row=9, column=2, columnspan=2)

window.mainloop()
