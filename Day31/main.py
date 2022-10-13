from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_word = {}

# ------------------------  Reading Files ------------------------

# data_file = pd.read_csv("./data/french_words.csv")
# data = data_file.to_dict(orient="records")

# data_file = pd.read_csv("./data/words_to_learn.csv")
# data = data_file.to_dict(orient="records")
try:
    data_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pd.read_csv("./data/french_words.csv")
finally:
    data = data_file.to_dict(orient="records")
    print(f"length: {len(data)}")


# -------------- Button functions
def show_english_word():
    global current_word
    canvas.itemconfig(image_backgroung, image=back_card_photo)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


def next_card():
    # get random French word
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(data)
    canvas.itemconfig(image_backgroung, image=front_card_photo)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")

    timer = window.after(3000, show_english_word)


def correct():
    # remove correct entry from the list
    data.remove(current_word)

    # convert the new list to a dataframe
    new_data = pd.DataFrame.from_records(data)

    # convert new data into a csv file
    new_file = new_data.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


# ------------------------ USER INTERFACE ------------------------

window = Tk()
window.title("Flash-Card Project")
window.config(pady=35, padx=35, bg=BACKGROUND_COLOR)
timer = window.after(3000, show_english_word)

# images

front_card_photo = PhotoImage(file="./images/card_front.png")
back_card_photo = PhotoImage(file="./images/card_back.png")
right_photo = PhotoImage(file="./images/right.png")
wrong_photo = PhotoImage(file="./images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_backgroung = canvas.create_image(400, 263, image=front_card_photo)
canvas.grid(column=0, row=0, columnspan=3)

language_text = canvas.create_text(400, 188, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 338, text="Je", fill="black", font=(FONT_NAME, 40, "bold"))

# buttons
right_button = Button(image=right_photo, highlightthickness=0, command=correct)
right_button.grid(column=2, row=1)

wrong_button = Button(image=wrong_photo, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

# mainloop
window.mainloop()
