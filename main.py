from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
window = Tk()
window.minsize(width=1000, height=600)
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


# TODO 2 : create function That changes the words
# Problem in changinig the words can't print them one after ther other by cliking the button
def word_change():
    word_list = pd.read_csv("../flash-card-project-start/data/french_words.csv")
    Tran_word_list = word_list.to_dict(orient="list")
    French_word = []
    for word in Tran_word_list["French"]:
        French_word.append(word)
    for word1 in French_word :
        card_front.create_text(400, 263, text=f"{word1}", font=(FONT, 60, "bold"))
        print(word1)
# word_change()

# TODO 1 : create the UI for the game
#--------------------UI------------------------------------------------------------------------------------------------
image_card_front = PhotoImage(file="../flash-card-project-start/images/card_front.png")
card_front = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front.create_image(400,263, image=image_card_front )
card_front.create_text(400,150, text="Title",font=(FONT,40,"italic"))
card_front.grid(column=1,row=1,columnspan=2)

image_right_but = PhotoImage(file="../flash-card-project-start/images/right.png")
right_but = Button(width=100,height=100,image=image_right_but, bd=0,bg=BACKGROUND_COLOR, highlightthickness=0, command=word_change  )
right_but.grid(column=2,row=2)

image_wrong = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_but = Button(width=100, height=100,image=image_wrong, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR)
wrong_but.grid(column=1,row=2)



window.mainloop()
