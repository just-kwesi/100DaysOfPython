import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

sessions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_label,text="Timer")
    checkLabel.config(text="")
    global sessions
    sessions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global sessions,checks_count
    sessions += 1


    if sessions % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        canvas.itemconfig(timer_label, text="Break", fill=RED)

    elif sessions % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        canvas.itemconfig(timer_label, text="Break", fill=PINK)
    else:
        count_down(WORK_MIN * 60)
        canvas.itemconfig(timer_label, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    mins_left = math.floor(count / 60)
    secs_left = count % 60
    if secs_left < 10:
        secs_left = f"0{secs_left}"

    canvas.itemconfig(timer_text, text=f"{mins_left}:{secs_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(sessions / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkLabel.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)

canvas = Canvas(width=250, height=300, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")

canvas.create_image(125, 150, image=photo)
timer_label = canvas.create_text(125, 20, text="Timer", fill=GREEN, font=(FONT_NAME, 40, "bold"))
timer_text = canvas.create_text(125, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=1)
reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=1)

checkLabel = Label(fg=GREEN, bg=YELLOW)
checkLabel.grid(column=1, row=2)

window.mainloop()
