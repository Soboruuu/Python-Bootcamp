from words import word_list
from tkinter import *
from tkinter import messagebox
import random
import time

BACKGROUND_COLOR = "#F5EDDC"
FONT_COLOR = "#434242"
CORRECT_COLOR = "#3E8E7E"
WRONG_COLOR = "#EB1D36"

WORDCOUNT = 0
START_TIME = 0
timer = None

with open("words.txt") as f:
    word_list = []
    for line in f:
        word_list.append(line.strip())

#-----DEF-----#

def start_test():
    global START_TIME, WORDCOUNT, timer
    WORDCOUNT = 0
    START_TIME = time.time()
    next_word()
    typing_entry.delete(0, END)
    typing_entry.config(state="normal")
    typing_entry.focus()
    words_label.config(fg=FONT_COLOR)
    start_button.config(state="disabled")
    timer = screen.after(60000, func=timeout)

def timeout():
    global WORDCOUNT, START_TIME, timer
    time_taken = time.time() - START_TIME
    typing_speed = int((WORDCOUNT / time_taken) * 60)
    messagebox.showinfo("Time Out!", f"Your Typing speed is {typing_speed} wpm")
    words_label.config(text="")
    typing_entry.delete(0, END)
    screen.after_cancel(timer)
    typing_entry.config(state="disabled")
    start_button.config(state="normal")


def check(event):
    global WORDCOUNT
    typed_word = typing_entry.get()
    if typed_word == words_label.cget("text"):
        words_label.config(fg=CORRECT_COLOR)
        WORDCOUNT += 1
    else:
        words_label.config(fg=WRONG_COLOR)
    typing_entry.delete(0, END)
    words_label.update()
    time.sleep(0.1)
    next_word()

def next_word():
    word = random.choice(word_list)
    words_label.config(text=word, fg=FONT_COLOR)

def reset_ui():
    words_label.config(text="", fg=FONT_COLOR)
    typing_entry.delete(0, END)
    typing_entry.config(state="disabled")
    start_button.config(state="normal")

#-----UI-----#

screen = Tk()
screen.title("Typing Test")
screen.config(bg=BACKGROUND_COLOR, width=1000, height=600, padx=50, highlightthickness=0)

words_label = Label(text="",
                    font=("NotoSansKR-Light.otf", 50, "italic"),
                    bg=BACKGROUND_COLOR,
                    fg=FONT_COLOR,
                    highlightthickness=0,
                    pady=20)
words_label.grid(row=0, column=0)

typing_entry = Entry(width=30, bg=BACKGROUND_COLOR, fg=FONT_COLOR, state="disabled")
typing_entry.grid(row=1, column=0, pady=30)
typing_entry.bind('<Return>', check)

start_button = Button(text="Start",
                      font=("NotoSansKR-Light.otf", 20),
                      bg=BACKGROUND_COLOR,
                      fg=FONT_COLOR,
                      highlightcolor=BACKGROUND_COLOR,
                      highlightthickness= 0,
                      command= start_test)
start_button.grid(row=2, column=0, pady=20)

screen.mainloop()
