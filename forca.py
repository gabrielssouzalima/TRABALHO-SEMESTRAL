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
altura_janela = 615

# Calcula as coordenadas x e y para centralizar a janela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Define a geometria da janela
root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()
canvas.create_line(5, 400, 5, 50)
canvas.create_line(5, 50, 170, 50)
canvas.create_line(170, 50, 170, 100)

palavra_label = tk.Label(root, text=" ".join(
    letras_corretas), font=("Helvetica", 18))
palavra_label.pack(pady=20)

letra_entry = tk.Entry(root, font=("Helvetica", 16))
letra_entry.pack()

# Vincula a tecla Enter para acionar o botão "Verificar"
letra_entry.bind("<Return>", lambda event: verificar_letra())

verificar_button = tk.Button(root, text="Verificar", command=verificar_letra)
verificar_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
resultado_label.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()