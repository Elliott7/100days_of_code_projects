""""
Project Twenty-Eight - Pomodoro Project
"""

from tkinter import *
import time


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = '✔'
reps = 0
timerr = None


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
y = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    try:
        window.after_cancel(timerr)
    except:
        pass
    if reps % 2 == 1:
        timer.config(text="Timer", fg=GREEN)
        count_down(work_sec)
        add_check()

    elif reps == 8:
        timer.config(text="Break", fg=RED)
        count_down(long_break)

    else:
        timer.config(text="Break", fg=PINK)
        count_down(short_break)


def count_down(count):
    global timerr
    mins, secs = divmod(count, 60)
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(y, text=f'{mins}:{secs}')
    if count > 0:
        timerr = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def reset():
    global reps
    reps = 0
    window.after_cancel(timerr)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(y, text='00:00')


def add_check():
    count = TICK*int((reps/2))
    checks.config(text=count)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer.grid(column=1, row=0)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset)
checks = Label(text=TICK, bg=YELLOW, fg=GREEN)
start_button.grid(column=0, row=4)
reset_button.grid(column=2, row=4)
checks.grid(column=1, row=5)


window.mainloop()