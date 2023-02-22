from tkinter import *
import random

#Inicialização gerais do app: dimensão de tela, título icone
app = Tk()
app.title("Jogo da velha")
icon = PhotoImage(file="imagens/icon.png")
app.iconphoto(True, icon)
app.geometry("380x720")
app.resizable(False, False)

title = Label(app, text="1° Escolha sua opção!", font=("jetBrains Mono", 16, "bold"), fg="#121212").pack(pady=10)

imagens = {
    'pedra': PhotoImage(file='imagens/pedra.png', width=100, height=85),
    'papel': PhotoImage(file='imagens/papel.png', width=100, height=85),
    'tesoura': PhotoImage(file='imagens/tesoura.png', width=100, height=85)
}

#Images Pedra, Papel, Tesoura
pedra = PhotoImage(file="imagens/pedra.png", width=100, height=85)
pedra_label = Label(app, image=pedra)
pedra_label.place(x=10,y=80)
pedra_label.bind("<Button-1>", lambda e: handle_click(pedra))

papel = PhotoImage(file="imagens/papel.png", width=100, height=85)
papel_label = Label(app, image=papel)
papel_label.place(x=137,y=80)
papel_label.bind("<Button-1>", lambda e: handle_click(papel))

tesoura = PhotoImage(file="imagens/tesoura.png", width=100, height=85)
tesoura_label = Label(app, image=tesoura)
tesoura_label.place(x=264,y=80)
tesoura_label.bind("<Button-1>", lambda e: handle_click(tesoura))

#Cria um novo componente Label para mostrar a imagem selecionada do usuário
usuario_label = Label(app, image=None)
usuario_label.place(x=9, y=260)

#Cria um novo componente Label para mostrar a imagem selecionada da máquina
maquina_label = Label(app, image=None)
maquina_label.place(x=260, y=260)

vs_img = PhotoImage(file="imagens/vs.png")
vs_label = Label(app, image=vs_img)
vs_label.place(x=140, y=170)

#Cria o componente placar
resultado_label = Label(app, width=50, height=5)
resultado_label.place(x=140, y=370)
# resultados_label = Label(app,width=50, height=5)
# resultado_label.place(x=140, y=470)




# função para tratar o evento de clique nas imagens
def handle_click(event):
    usuario_label.config(image=event)
    usuario_label.image = event
    # habilita o botão "Jogar" que estará desabilitado
    jogar_button.config(state="normal")
    print(event)

def jogar():
    # obter a opção do usuário e validar se foi selecionada
    opcao_usuario = usuario_label.cget("image")
    if not opcao_usuario:
        return

    # opções do jogo
    opcoes = ["pedra", "papel", "tesoura"]

    # escolher uma opção aleatória para a máquina
    opcao_maquina = random.choice(opcoes)

    # criar um caminho para o arquivo da imagem da opção da máquina
    opcao_maquina_path = f"imagens/{opcao_maquina}.png"

    # exibir a imagem da opção da máquina
    opcao_maquina_image = PhotoImage(file=opcao_maquina_path)
    maquina_label.config(image=opcao_maquina_image)
    maquina_label.image = opcao_maquina_image

    # determinar o resultado do jogo
    if opcao_usuario == pedra and opcao_maquina == "tesoura":
        resultado = "Você ganhou!"
    elif opcao_usuario == papel and opcao_maquina == "pedra":
        resultado = "Você ganhou!"
    elif opcao_usuario == tesoura and opcao_maquina == "papel":
        resultado = "Você ganhou!"
    elif opcao_usuario == pedra and opcao_maquina == "papel":
        resultado = "Você perdeu!"
    elif opcao_usuario == papel and opcao_maquina == "tesoura":
        resultado = "Você perdeu!"
    elif opcao_usuario == tesoura and opcao_maquina == "pedra":
        resultado = "Você perdeu!"
    else:
        resultado = "Empate!"

    
    
    # # atualizar o contador de resultados
    # if resultado == "Você ganhou!":
    #     vitorias.set(vitorias.get() + 1)
    # elif resultado == "Você perdeu!":
    #     derrotas.set(derrotas.get() + 1)
    # else:
    #     empates.set(empates.get() + 1)

    # # exibir o resultado do jogo
    
    resultado_label.config(text=resultado)



#Criar botão jogar
jogar_button = Button(app, text="Jogar", width=50, height=2)
jogar_button.place(x=9, y=360)
jogar_button.bind("<Button-1>", lambda e: jogar())
jogar_button.config(state="disabled")






mainloop()