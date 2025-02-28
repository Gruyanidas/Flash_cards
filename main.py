#dependencies:
import random
import pandas as pd
from tkinter import *

#CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"

#DATA - reading from csv using pandas, trying to continue learning at first,
#if nothing is learnt yet, opens main file
try:
	words = pd.read_csv("data/Left_for_learning.csv")
except FileNotFoundError:
	words = pd.read_csv("data/french_words.csv")
	data_dict = words.to_dict(orient="records")
else:
	data_dict = words.to_dict(orient="records")

#FUNCTIONALITY
current_card = {}
counter = 0

def flip_card():
	foto_canvas.itemconfig(language_label, text="English", fill="white")
	foto_canvas.itemconfig(word_label, text=current_card["English"], fill="white")
	foto_canvas.itemconfig(card_background, image=card_back)

def next_card():
	global current_card
	global flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(data_dict)
	foto_canvas.itemconfig(language_label, text="French", fill="black")
	foto_canvas.itemconfig(word_label, text=current_card["French"], fill="black")
	foto_canvas.itemconfig(card_background, image=card_front)
	flip_timer = window.after(3000, func=flip_card)

def remove_card():
	data_dict.remove(current_card)
	global counter
	counter += 1
	score_label.config(text=f"Score\n{counter} / {len(data_dict)}")
	to_learn = pd.DataFrame(data_dict)
	to_learn.to_csv("data/Left_for_learning", index=False)
	next_card()

#UI GENERAL CANVASES AND BUTTONS
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
foto_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = foto_canvas.create_image(400, 263, image=card_back)
language_label = foto_canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = foto_canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
foto_canvas.grid(column=1, row=1, columnspan=3)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)

score = f"Score\n{counter} / {len(data_dict)}"
score_label = Label(text=score, font=("Ariel", 30, "bold"), bg=BACKGROUND_COLOR)
score_label.grid(column=2, row=2)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image,
						background=BACKGROUND_COLOR,
						highlightthickness=0,
						command=remove_card)
correct_button.grid(column=3, row=2)

#PROGRAM EXECUTION
next_card()























window.mainloop()