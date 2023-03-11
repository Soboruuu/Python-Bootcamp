from PyPDF2 import PdfReader
from gtts import gTTS
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time


file_path = ""

#---Function---#


def browse():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/",
                                           title="Select PDF Files",
                                           filetypes=(('pdf file', '*.pdf'),
                                                       ("all files", "*.*")))


def create(audio, txt):
    # Open pdf file and pass it to PDFReader.
    file = open(file_path, 'rb')
    pdf_read = PdfReader(file)
    # Set empty output.
    output = ""
    # add each page to output.
    for page in pdf_read.pages:
        output += page.extract_text()
        output += "\n"
        window.update()
    # create txt file and write output.
    with open(f'{txt}', 'w') as text:
        text.write(output)
    # Initialize gTTS with output.
    time.sleep(3)
    tts = gTTS(text=output, lang='en')
    # Save mp3 Audio file.
    tts.save(f'{audio}')
    messagebox.showinfo(title="Success", message="PDF was successfully converted into mp3 & txt files.")


#---UI---#
window = Tk()
window.title("PDF Reader & Audio Book converter")
window.config(padx=20, pady=10)

canvas = Canvas(height=100, width=100)
canvas.grid(row=0, column=0)

#1 PDF file Search button. Open file browser window.
filebrowser_btn = Button(text="Search PDF File", command=browse)
filebrowser_btn.grid(row=0, column=0, padx=10)

#2 PDF Audio file name Entry Field. Default pdf-audio.mp3.
audiofile_name = Entry()
audiofile_name.insert(0,'pdf-audio.mp3')
audiofile_name.grid(row=1, column=0, padx=10)

#3 PDF Text file name Entry Field. Defauld pdf-text.txt.
txtfile_name = Entry()
txtfile_name.insert(0, "pdf-text.txt")
txtfile_name.grid(row=2, column=0, padx=10)

#4 Create PDF audio file & PDF txt file Button.
audiofile = audiofile_name.get()
txtfile = txtfile_name.get()
create_btn = Button(text="Create mp3 & txt files from PDF", command= lambda: create(audiofile,txtfile))
create_btn.grid(row=3, column=0, padx=10, pady=20)

window.mainloop()
