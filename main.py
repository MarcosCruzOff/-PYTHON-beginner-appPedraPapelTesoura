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
  # Obtenha as coordenadas x e y do mouse a partir do evento
  x, y = event.x, event.y

  # Verifique qual objeto canvas foi clicado
  for imagem, obj in imagens:
      # Obtenha as coordenadas do objeto canvas
      obj_coords = frame_background.coords(obj)

      # Obtenha a largura e altura da imagem
      img_width = imagem.width()
      img_height = imagem.height()

      # Calcule as coordenadas dos dois cantos da imagem
      obj_x1, obj_y1 = obj_coords
      obj_x2 = obj_x1 + img_width
      obj_y2 = obj_y1 + img_height

      # Verifique se as coordenadas do mouse estão dentro das coordenadas do objeto canvas
      if obj_x1 <= x <= obj_x2 and obj_y1 <= y <= obj_y2:
          # Atualize a imagem do componente Label para a imagem atualmente selecionada
          imagem_label.configure(image=imagem)


frame_background = Canvas(app, bg="white", width=360, height=300)
frame_background.pack()
frame_background.bind("<Button-1>", handle_click)

#Images Pedra, Papel, Tesoura
rock = PhotoImage(file="PEDRA.png", width=100, height=85)
obj_rock = frame_background.create_image(190,50, image=rock, tags="imagem")

paper = PhotoImage(file="PAPEL.png", width=100, height=85)
obj_paper = frame_background.create_image(190,150, image=paper, tags="imagem")

scissor = PhotoImage(file="TESOURA.png", width=100, height=85)
obj_scissor = frame_background.create_image(190,250, image=scissor, tags="imagem")

imagens = [(rock, obj_rock), (paper, obj_paper), (scissor, obj_scissor)]

#Cria um novo componente Label para mostrar a imagem selecionada
imagem_label = Label(app, image='')
imagem_label.place(x=9, y=360)



mainloop()