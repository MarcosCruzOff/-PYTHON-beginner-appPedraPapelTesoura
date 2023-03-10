from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

#Inicialização gerais do app: dimensão de tela, título icone
app = Tk()
app.title("Jogo Pedra Papel Tesoura")
icon = PhotoImage(file="imagens/icon.png")
app.iconphoto(True, icon)
app.geometry("380x720")
app.resizable(False, False)
app.config(bg="#FFFFFF")

#variável de estilização
bg_app = "#FFFFFF"
color_fonts_bords = "#0D1C47"

#variavel global
opcao_usuario = None

title = Label(app, text="1° Escolha sua opção!", font=("jetBrains Mono", 16, "bold"), fg=color_fonts_bords, bg=bg_app).pack(pady=10)

# carregar imagens
pedra_img = ImageTk.PhotoImage(Image.open("imagens/pedra.png"))
papel_img = ImageTk.PhotoImage(Image.open("imagens/papel.png"))
tesoura_img = ImageTk.PhotoImage(Image.open("imagens/tesoura.png"))

# armazenar as imagens em um dicionário
opcoes_imagens = {
    "pedra": pedra_img,
    "papel": papel_img,
    "tesoura": tesoura_img
}

# função para tratar o evento de clique nas imagens
def escolher_opcao(opcao):
    global opcao_usuario
    usuario_label.config(image=opcoes_imagens[opcao])
    usuario_label.image = opcoes_imagens[opcao]
    opcao_usuario = opcao
    print(opcao)  

# criar labels para as imagens
pedra_label = Label(app, image=pedra_img, bg=color_fonts_bords)
pedra_label.place(x=10,y=80)
pedra_label.bind("<Button-1>", lambda e: escolher_opcao("pedra"))
papel_label = Label(app, image=papel_img, bg=color_fonts_bords)
papel_label.place(x=137,y=80)
papel_label.bind("<Button-1>", lambda e: escolher_opcao("papel"))
tesoura_label = Label(app, image=tesoura_img, bg=color_fonts_bords)
tesoura_label.place(x=264,y=80)
tesoura_label.bind("<Button-1>", lambda e: escolher_opcao("tesoura"))

#Cria um novo componente Label para mostrar a imagem selecionada do usuário
usuario_label = Label(app, image=None, bg=bg_app, highlightthickness=0)
usuario_label.place(x=9, y=300)

#Cria um novo componente Label para mostrar a imagem selecionada da máquina
maquina_label = Label(app, image=None, bg=bg_app)
maquina_label.place(x=260, y=300)

#Cria um novo componente Label para mostrar as escolhas do usuário e da máquina
escolhas_label = Label(app, image= None, bg=bg_app)
escolhas_label.place(x=80, y=210)

vs_img = PhotoImage(file="imagens/vs.png")
vs_label = Label(app, image=vs_img, highlightthickness=0, bg=bg_app)
vs_label.place(x=140, y=300)
    
#adicionar contador de vitórias, empate e derrotas
empates = StringVar(value="0")
vitorias = StringVar(value="0")
derrotas = StringVar(value="0")

Label(app, text="Vitórias: ", font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=10, y=600)
Label(app, textvariable=vitorias, font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=80, y=600)

Label(app, text="Empates", font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=10, y=620)    
Label(app, textvariable=empates, font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=80, y=620)

Label(app, text="Derrotas", font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=10, y=640)    
Label(app, textvariable=derrotas, font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app).place(x=80, y=640)

def determinar_resultado(escolha_usuario, escolha_bot):
    if escolha_usuario == escolha_bot:
        return "Empate!"
    elif escolha_usuario == "pedra":
        if escolha_bot == "papel":
            return "Você perdeu!"
        else:
            return "Você ganhou!"
    elif escolha_usuario == "papel":
        if escolha_bot == "tesoura":
            return "Você perdeu!"
        else:
            return "Você ganhou!"
    elif escolha_usuario == "tesoura":
        if escolha_bot == "pedra":
            return "Você perdeu!"
        else:
            return "Você ganhou!"

def jogar(vitorias, derrotas, empates):
    # obter opção do usuário
    global opcao_usuario
    
    if opcao_usuario :
        # escolher opção da máquina
        opcoes_maquina = ["pedra", "papel", "tesoura"]
        opcao_maquina = random.choice(opcoes_maquina)
    
        # exibir a imagem da opção da máquina
        opcao_maquina_path = f"imagens/{opcao_maquina}.png"
        opcao_maquina_image = PhotoImage(file=opcao_maquina_path)
        maquina_label.config(image=opcao_maquina_image)
        maquina_label.image = opcao_maquina_image

        # atualizar as labels de escolhas
        escolhas_label.config(text=f"Você escolheu {opcao_usuario}. \nO computador escolheu {opcao_maquina}.",font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, justify="center",  bg=bg_app)
        
        # determinar o resultado da partida
        resultado = determinar_resultado(opcao_usuario, opcao_maquina)
        
        # atualizar o contador de resultados
        if resultado == "Você ganhou!":
            vitorias.set(str(int(vitorias.get()) + 1))
        elif resultado == "Você perdeu!":
            derrotas.set(str(int(derrotas.get()) + 1))
        else:
            empates.set(str(int(empates.get()) + 1))

        resultado_label.config(text=resultado)
    else:
        # usuário não selecionou nenhuma opção
        messagebox.showwarning("Aviso","Faça sua escolha primeiro antes de jogar")
        # return   

      

# criar botão jogar
botao_jogar = Button(app, text="JOGAR", font=("jetBrains Mono", 10, "bold"),bg="#FED934", width=45, height=2, command= lambda: jogar(vitorias, derrotas, empates))
botao_jogar.place(x=5, y=410)
# botao_jogar.bind("<Button-1>", lambda e: jogar(vitorias, derrotas, empates))

#Cria o componente placar
resultado_label = Label(app, width=50, height=5,  font=("jetBrains Mono", 10, "bold"), fg=color_fonts_bords, bg=bg_app)
resultado_label.place(x=100, y=600)

mainloop()