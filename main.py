from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
window = Tk()
window.minsize(width=1000, height=600)
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

image_card_front = PhotoImage(file="../flash-card-project-start/images/card_front.png")
card_front = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front.create_image(400,260, image=image_card_front )
card_front.create_text(400,150, text="French",font=(FONT,40,"italic"))
card_front.create_text(400,263, text="Trouve",font=(FONT,60,"bold"))
card_front.grid(column=1,row=1,columnspan=2)

image_right_but = PhotoImage(file="../flash-card-project-start/images/right.png")
right_but = Canvas(width=100,height=100,highlightthickness=0)
right_but.create_image(50,50, image=image_right_but)
right_but.grid(column=2,row=2)

image_wrong_but = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_but = Canvas(width=100, height=100,highlightthickness=0)
wrong_but.create_image(50,50, image=image_wrong_but)
wrong_but.grid(column=1,row=2)

window.mainloop()
