from tkinter import *
import pandas as pd
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
window = Tk()
window.minsize(width=1000, height=600)
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
file_path = "data/word_to_learn.csv"
try:
    word_list = pd.read_csv("../flash-card-project-start/data/french_words.csv")
    word_list_to_learn = pd.read_csv("../flash-card-project-start/data/word_to_learn.csv")
except FileNotFoundError:
    word_list_to_learn = word_list.to_csv(file_path,index=False)
else:
    Tran_word_list = word_list.to_dict(orient="records")
    word_dict_to_learn = word_list_to_learn.to_dict(orient="records")
    current_card = {}



# TODO 2 : create function That changes the words
def next_word():
    global card_flip_timer, current_card, word_list_to_learn
    window.after_cancel(card_flip_timer)
    print(word_dict_to_learn)
    current_card = random.choice(word_dict_to_learn)
    # index =len(current_card)
    # print(index)
    card.itemconfig(card_title, text=f"French",fill="black" )
    card.itemconfig(card_word, text=current_card['French'], fill="black")
    card.itemconfig(card_background, image=image_card_front)
    card_flip_timer = window.after(3000, func=flip_card)
    word_dict_to_learn.remove(current_card)
    print(word_dict_to_learn)
    # new_data = {'French':word_dict_to_learn[0:]["French"]}
    # word_list_to_learn.drop()
    # word_list_to_learn = word_dict_to_learn.(file_path,index=False)


#TODO 3 : create the fliping function
def flip_card():
    card.itemconfig(card_background, image=image_card_back)
    card.itemconfig(card_title, fill="white", text="English")
    card.itemconfig(card_word, fill="white", text=current_card['English'])

# TODO 1 : create the UI for the game
#--------------------UI------------------------------------------------------------------------------------------------
image_card_front = PhotoImage(file="../flash-card-project-start/images/card_front.png")
image_card_back = PhotoImage(file="../flash-card-project-start/images/card_back.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(400, 263, image=image_card_front)
card_title = card.create_text(400, 150, text="", font=(FONT, 40, "italic"))
card_word = card.create_text(400, 263, text="", font=(FONT, 60, "bold"))

card.grid(column=1, row=1, columnspan=2)

image_right_but = PhotoImage(file="../flash-card-project-start/images/right.png")
right_but = Button(width=100,height=100,image=image_right_but, bd=0,bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word )
right_but.grid(column=2,row=2)

image_wrong = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_but = Button(width=100, height=100,image=image_wrong, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_but.grid(column=1,row=2)

card_flip_timer = window.after(3000, func=flip_card)
next_word()

window.mainloop()
