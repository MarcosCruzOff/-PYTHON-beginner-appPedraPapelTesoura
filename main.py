from tkinter import *
import random
import os
import re

app = Tk()
app.title("Jogo da velha")
icon = PhotoImage(file="icon.png")
app.iconphoto(True, icon)
app.geometry("380x720")

title = Label(app, text="Escolha sua opção!", font=("jetBrains Mono", 16, "bold"), fg="#121212").pack(pady=10)

def handle_click(event):
  x,y = event.x, event.y
  
  if(x>=100 and y<=80):
    print("Pedra")

frame_background_rock = Canvas(app, bg="red", width=360, height=100)
frame_background_rock.pack(pady=10)
# frame_background_paper.bind("<Button-1>", handle_click)
rock = PhotoImage(file="PEDRA.png", width=100, height=85)
img_rock = Label(frame_background_rock, width=360, image=rock, bg="white", highlightthickness=0, justify="center")
img_rock.place(x=0, y=7)
img_rock.bind("<Button-1>", handle_click)

frame_background_paper = Canvas(app, bg="red", width=360, height=100)
frame_background_paper.pack(pady=10)
# frame_background_paper.bind("<Button-1>", handle_click)
paper = PhotoImage(file="PAPELs.png", width=100, height=85)
img_paper = Label(frame_background_paper, width=360, image=paper, bg="white", highlightthickness=0, justify="center")
img_paper.place(x=0, y=7)
img_paper.bind("<Button-1>", handle_click)

frame_background_scissor = Canvas(app, bg="red", width=360, height=100)
frame_background_scissor.pack()
# frame_background_scissor.bind("<Button-1>", handle_click)
scissor = PhotoImage(file="TESOURA.png", width=100, height=85)
img_scissor = Label(frame_background_scissor, width=360, image=scissor, bg="white", highlightthickness=0, justify="right",)
img_scissor.place(x=0, y=7)
img_scissor.bind("<Button-1>", handle_click) 



mainloop()