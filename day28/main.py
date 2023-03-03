from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
stopwatch = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(stopwatch)
    canvas.itemconfig(timer, text="00:00")
    work_break.config(text="Timer", fg=GREEN)
    check_marker.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        work_break.config(text= "Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break)
        work_break.config(text="Break", fg=PINK)

    else:
        countdown(work)
        work_break.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(seconds):
    global checks, stopwatch
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    count = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer, text= count)
    if seconds > 0:
        stopwatch = window.after(1000, countdown, seconds -1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✔"
        check_marker.config(text= checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png",)
canvas.create_image(100,112, image=tomato_image)
canvas.grid(row=1, column=1)

timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))

work_break = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg= YELLOW, fg=GREEN)
work_break.grid(row=0,column=1)

start_button= Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button= Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command = reset_timer)
reset_button.grid(row=2, column=2)

check_marker = Label(text="︎", font=(FONT_NAME, 50, "bold"), bg= YELLOW, fg=GREEN)
check_marker.grid(row=3, column=1)

window.mainloop()


