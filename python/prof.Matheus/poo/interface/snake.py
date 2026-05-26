import tkinter as tk
import random

# ================== CONFIGURAÇÕES DO JOGO ==================
# Aqui a gente define o tamanho da tela e da cobrinha

LARGURA = 600   # largura da tela
ALTURA = 400    # altura da tela
TAMANHO = 20    # tamanho de cada "quadradinho" da cobrinha e comida
VELOCIDADE = 120  # velocidade do jogo (quanto menor, mais rápido)


# ================== CLASSE DO JOGO ==================
# Essa classe é tipo o "cérebro" do jogo, ela controla tudo
class SnakeGame:
    def __init__(self, root):
        # root é a janela principal
        self.root = root
        self.root.title("Jogo da Cobrinha")

        # Aqui criamos a área onde tudo vai ser desenhado
        self.canvas = tk.Canvas(root, width=LARGURA, height=ALTURA, bg="black")
        self.canvas.pack()

        # Mostra o menu inicial
        self.menu_inicial()

        # ================= CONTROLES DO TECLADO =================
        # Aqui falamos: quando apertar uma tecla, faz alguma coisa
        self.root.bind("<Up>", self.subir)       # seta ↑
        self.root.bind("<Down>", self.descer)    # seta ↓
        self.root.bind("<Left>", self.esquerda)  # seta ←
        self.root.bind("<Right>", self.direita)  # seta →

        # Começa indo para a direita
        self.direcao = "Right"

    # ================== MENU ==================
    def menu_inicial(self):
        # Limpa a tela
        self.canvas.delete("all")

        # Escreve o nome do jogo
        self.canvas.create_text(LARGURA/2, ALTURA/2 - 20,
                                text="COBRINHA",
                                fill="white",
                                font=("Arial", 30))

        # Escreve instrução
        self.canvas.create_text(LARGURA/2, ALTURA/2 + 20,
                                text="Pressione ENTER para jogar",
                                fill="white",
                                font=("Arial", 15))

        # Quando apertar ENTER, começa o jogo
        self.root.bind("<Return>", lambda e: self.iniciar_jogo())

    # ================== INICIAR JOGO ==================
    def iniciar_jogo(self):
        # Limpa tela
        self.canvas.delete("all")

        # Aqui criamos a cobrinha (3 pedacinhos)
        self.cobrinha = [(100, 100), (80, 100), (60, 100)]

        # Começa indo para direita
        self.direcao = "Right"

        # Começa com 0 pontos
        self.score = 0

        # Cria comida
        self.criar_comida()

        # Começa o jogo (loop)
        self.atualizar()

    # ================== CRIAR COMIDA ==================
    def criar_comida(self):
        # Escolhe uma posição aleatória dentro da tela
        x = random.randint(0, (LARGURA - TAMANHO) // TAMANHO) * TAMANHO
        y = random.randint(0, (ALTURA - TAMANHO) // TAMANHO) * TAMANHO

        # Guarda onde a comida está
        self.comida = (x, y)

    # ================== ATUALIZAR JOGO ==================
    def atualizar(self):
        # Pega a posição da cabeça da cobrinha
        x, y = self.cobrinha[0]

        # Aqui vemos para onde ela vai
        if self.direcao == "Up":
            y -= TAMANHO  # sobe
        elif self.direcao == "Down":
            y += TAMANHO  # desce
        elif self.direcao == "Left":
            x -= TAMANHO  # esquerda
        elif self.direcao == "Right":
            x += TAMANHO  # direita

        # Nova posição da cabeça
        nova_cabeca = (x, y)

        # ================= COLISÃO =================
        # Se bater na parede ou no próprio corpo -> morreu
        if (
            x < 0 or x >= LARGURA or
            y < 0 or y >= ALTURA or
            nova_cabeca in self.cobrinha
        ):
            self.game_over()
            return

        # A cobrinha anda adicionando uma nova cabeça
        self.cobrinha.insert(0, nova_cabeca)

        # ================= COMER COMIDA =================
        if nova_cabeca == self.comida:
            self.score += 1      # ganha ponto
            self.criar_comida() # cria nova comida
        else:
            self.cobrinha.pop() # remove o último pedaço (andar normal)

        # Desenha tudo na tela
        self.desenhar()

        # Faz o jogo repetir depois de um tempo (delay)
        self.root.after(VELOCIDADE, self.atualizar)

    # ================== DESENHAR ==================
    def desenhar(self):
        # Limpa tela
        self.canvas.delete("all")

        # Desenha a cobrinha
        for x, y in self.cobrinha:
            self.canvas.create_rectangle(x, y, x+TAMANHO, y+TAMANHO, fill="green")

        # Desenha a comida
        x, y = self.comida
        self.canvas.create_rectangle(x, y, x+TAMANHO, y+TAMANHO, fill="red")

        # Mostra o score
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")

    # ================== GAME OVER ==================
    def game_over(self):
        # Limpa tela
        self.canvas.delete("all")

        # Mensagem de derrota
        self.canvas.create_text(LARGURA/2, ALTURA/2 - 20,
                                text="GAME OVER",
                                fill="red",
                                font=("Arial", 30))

        # Mostra pontuação final
        self.canvas.create_text(LARGURA/2, ALTURA/2 + 10,
                                text=f"Score: {self.score}",
                                fill="white",
                                font=("Arial", 15))

        # Instrução para reiniciar
        self.canvas.create_text(LARGURA/2, ALTURA/2 + 40,
                                text="Pressione ENTER para reiniciar",
                                fill="white",
                                font=("Arial", 12))

        # Se apertar ENTER, começa de novo
        self.root.bind("<Return>", lambda e: self.iniciar_jogo())

    # ================== CONTROLES ==================
    # Essas funções mudam a direção da cobrinha

    def subir(self, event):
        if self.direcao != "Down":
            self.direcao = "Up"

    def descer(self, event):
        if self.direcao != "Up":
            self.direcao = "Down"

    def esquerda(self, event):
        if self.direcao != "Right":
            self.direcao = "Left"

    def direita(self, event):
        if self.direcao != "Left":
            self.direcao = "Right"


# ================== EXECUÇÃO ==================
# Aqui o jogo começa de verdade

root = tk.Tk()           # cria a janela
game = SnakeGame(root)   # cria o jogo

root.mainloop()          # mantém o jogo rodando