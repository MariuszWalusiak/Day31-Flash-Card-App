from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Aerial"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
photo_image_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=photo_image_front)

canvas.create_text(400, 150, text="french", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="french", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image,highlightthickness=0)
wrong_button.grid(column=0,row=1)

check_image = PhotoImage(file="images/right.png",)
right_button = Button(image=check_image,highlightthickness=0)
right_button.grid(column=1,row=1)

window.mainloop()