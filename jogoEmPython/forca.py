import tkinter as tk
import random

def escolher_palavra():
    palavras = ["MITS", "altair", "programacao", "etec", "tecnologia",
                "computador", "Ridley", "Microsoft", "Apple", "informatica"]
    return random.choice(palavras).upper()

def atualizar_palavra():
    palavra_label.config(text=" ".join(letras_corretas))

def desenhar_boneco():
    # Desenhar partes do boneco com base no número de tentativas restantes
    if tentativas == 5:
        canvas.create_oval(140, 100, 200, 160)  # Cabeça
    elif tentativas == 4:
        canvas.create_line(170, 160, 170, 290)  # Corpo
    elif tentativas == 3:
        canvas.create_line(170, 190, 140, 240)  # Braço esquerdo
    elif tentativas == 2:
        canvas.create_line(170, 190, 200, 240)  # Braço direito
    elif tentativas == 1:
        canvas.create_line(170, 290, 140, 345)  # Perna esquerda
    elif tentativas == 0:
        canvas.create_line(170, 290, 200, 345)  # Perna direita
        # Criando a primeira linha do X da forca
        canvas.create_line(117, 140, 222, 180)
        # Criando o segundo linha do X da forca
        canvas.create_line(117, 180, 222, 140)

def verificar_letra():
    global tentativas
    chute = letra_entry.get().upper()
    letra_entry.delete(0, tk.END)

    if len(chute) != 1 or not chute.isalpha():
        resultado_label.config(text="Digite uma única letra válida.")
        return

    if chute in letras_corretas or chute in letras_erradas:
        resultado_label.config(text="Você já tentou essa letra. Tente outra.")
        return

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_corretas[i] = letra
        resultado_label.config(text="Boa! A letra está na palavra.")
    else:
        tentativas -= 1
        letras_erradas.append(chute)
        desenhar_boneco()
        resultado_label.config(text="A letra não está na palavra.")

    atualizar_palavra()

    if "_" not in letras_corretas:
        resultado_label.config(text="Parabéns! Você adivinhou a palavra!")
        letra_entry.config(state=tk.DISABLED)
    elif tentativas == 0:
        resultado_label.config(
            text=f"Você perdeu! A palavra era: {palavra_secreta}")
        letra_entry.config(state=tk.DISABLED)

# Esta linha define uma nova função chamada reiniciaJogo.
# Esta função será chamada quando o botão "Jogar Novamente" for clicado.
def reiniciaJogo():
    # Essa linha indica que as variáveis palavra_secreta, letras_corretas,
    # tentativas e letras_erradas serão usadas dentro da função reiniciaJogo,
    # e estas variáveis são globais, o que significa que são definidas fora
    # da função.
    global palavra_secreta, letras_corretas, tentativas, letras_erradas
    # Esta linha redefine palavra_secreta escolhendo uma nova palavra secreta
    # para o jogo.
    palavra_secreta = escolher_palavra()
    # Esta linha redefine letras_corretas para uma lista de sublinhados,
    # representando a nova palavra secreta, onde cada caractere é representado
    # por um sublinhado.
    letras_corretas = ["_" for _ in palavra_secreta]
    # Esta linha redefine o número de tentativas restantes para 6,
    # reiniciando o contador de tentativas.
    tentativas = 6
    # Esta linha redefine a lista letras_erradas para uma lista vazia,
    # removendo quaisquer tentativas erradas anteriores.
    letras_erradas = []
    # Esta linha chama a função atualizar_palavra para atualizar a exibição
    # da palavra na interface com os sublinhados da nova palavra.
    atualizar_palavra()
    # Esta linha limpa o canvas, removendo todos os desenhos anteriores
    # (como partes do boneco).
    canvas.delete("all")
    # Essas linhas redesenham a estrutura da forca no canvas.
    canvas.create_line(5, 400, 5, 50)
    canvas.create_line(5, 50, 170, 50)
    canvas.create_line(170, 50, 170, 100)
    # Esta linha redefine o texto do resultado_label para uma string vazia,
    # removendo qualquer mensagem anterior.
    resultado_label.config(text="")
    # Esta linha reativa a entrada de texto letra_entry, permitindo que o
    # jogador insira novas letras.
    letra_entry.config(state=tk.NORMAL)

# Inicializa o jogo
palavra_secreta = escolher_palavra()
letras_corretas = ["_" for _ in palavra_secreta]
tentativas = 6
letras_erradas = []

# Configura a interface gráfica
root = tk.Tk()
root.title("Jogo da Forca")

# Configura a posição da janela no centro da tela
# Obtém a largura e altura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Define as dimensões da janela
largura_janela = 500
altura_janela = 621

# Calcula as coordenadas x e y para centralizar a janela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Define a geometria da janela
root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

# Essas linhas desenham a estrutura da forca no canvas.
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()
canvas.create_line(5, 400, 5, 50)
canvas.create_line(5, 50, 170, 50)
canvas.create_line(170, 50, 170, 100)

# Esta linha cria um widget Label na interface gráfica. Um
# Label é usado para exibir texto ou imagens na interface.
palavra_label = tk.Label(root, text=" ".join(
    letras_corretas), font=("Helvetica", 18))
# Esta linha adiciona o Label à janela principal utilizando o
# método pack, que é um dos métodos de gerenciamento de layout em Tkinter.
palavra_label.pack(pady=20)

# Esta linha cria um widget Entry na interface gráfica. Um Entry é um
# campo de entrada de texto que permite ao usuário digitar uma linha de texto.
letra_entry = tk.Entry(root, font=("Helvetica", 16))
# Esta linha adiciona o Entry à janela principal utilizando o método pack,
# que é um dos métodos de gerenciamento de layout em Tkinter.
letra_entry.pack()

# Vincula a tecla Enter para acionar o botão "Verificar"
letra_entry.bind("<Return>", lambda event: verificar_letra())
# Frame para os botões
# Essa linha cria um novo contêiner Frame dentro da janela
# principal root. Um Frame é um widget que pode conter outros widgets,
# permitindo organizar o layout da janela.
button_frame = tk.Frame(root)
# Essa linha adiciona o Frame à janela principal e aplica um
# preenchimento vertical (pady) de 15 pixels ao redor do Frame,
# criando algum espaço vertical extra.
button_frame.pack(pady=15)
# Esta linha cria um botão chamado "Verificar" dentro do button_frame.
# O texto do botão é "Verificar" e, quando clicado, ele executará a
# função verificar_letra.
verificar_button = tk.Button(
    button_frame, text="Verificar", command=verificar_letra)
# Essa linha empacota (adiciona) o botão "Verificar" ao button_frame
# e o centraliza horizontalmente (side=tk.RIGHT).
verificar_button.pack(side=tk.LEFT)
# Esta linha cria um segundo botão chamado "Jogar Novamente" dentro
# do button_frame. O texto do botão é "Jogar Novamente" e, quando clicado,
# ele executará a função reiniciaJogo.
jogarDeNovo = tk.Button(
    button_frame, text="Jogar Novamente", command=reiniciaJogo)
# Essa linha empacota (adiciona) o botão "Jogar Novamente" ao button_frame
# e o centraliza horizontalmente (side=tk.CENTER).
jogarDeNovo.pack(side=tk.RIGHT)

# Esta linha cria um widget Label na interface gráfica. Um Label é usado
# para exibir texto ou imagens na interface.
resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
# Esta linha adiciona o Label à janela principal utilizando o método pack,
# que é um dos métodos de gerenciamento de layout em Tkinter.
resultado_label.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()