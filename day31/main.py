from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#-------FUNCTIONS-------#

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/japanese_words.csv")
finally:
    dt_dict = data.to_dict(orient="records")
    current_card = random.choice(dt_dict)

def next_card():
    global current_card, flip_timer
    current_card=random.choice(dt_dict)
    screen.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language, text="Japanese", fill="black")
    canvas.itemconfig(word, text=current_card["Japanese"], fill="black")
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def known_word():
    dt_dict.remove(current_card)
    words_to_learn = pd.DataFrame(dt_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#-------UI-------#

screen = Tk()
screen.title("Flash Card Game")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = screen.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)

card_image = canvas.create_image(400,263, image=card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400,150, text= "Language", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"),fill="black")
canvas.grid(row=0, column=0, columnspan=2)



right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=known_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

screen.mainloop()



