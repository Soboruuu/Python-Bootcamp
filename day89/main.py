from tkinter import *

BACKGROUND_COLOR = "#F5EDDC"
FONT_COLOR = "#434242"
WRONG_COLOR = "#EB1D36"
second=5

def sec():
    global second, current_text
    if len(text.get()) > 0 and text.get() == current_text:
        timer.config(text=f"Deleting in: {second}")
        if second == 0:
            text.delete(0, END)
            timer.config(text=f"Start again...")
            screen.after(1000, sec)
        else:
            screen.after(1000, sec)
            second -= 1
    else:
        current_text = text.get()
        second = 5
        timer.config(text=f"Deleting in: {second}")
        screen.after(1000, sec)


#-----UI-----#
screen = Tk()
screen.geometry("400x200")
screen.title("Text disappearing writing")
screen.config(bg=BACKGROUND_COLOR, padx=20, pady=20, highlightthickness=0)

title = Label(text="Text Disappearing Writing", bg=BACKGROUND_COLOR, fg=FONT_COLOR, font=('Arial', 20))
title.grid(row=0, pady=10)

current_text=""
text = Entry(width=38, bg="white", fg=FONT_COLOR)
text.grid(row=1, pady=10)
text.focus()

timer = Label(text=f"", bg=BACKGROUND_COLOR, fg=FONT_COLOR)
timer.grid(row=2, pady=10)


if True:
    sec()
    screen.mainloop()
