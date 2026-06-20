import pygame
from src.camera import camera

# recebe o caminho da imagem e a largura de cada frame
# divide a imagem em pedaços iguais e guarda cada um numa lista
def carregar_frames(caminho, largura_frame=128):
    spritesheet = pygame.image.load(caminho).convert_alpha()
    spritesheet.set_colorkey((0, 0, 0))  # remove o fundo preto da imagem

    # descobre quantos frames tem na imagem dividindo a largura total pela largura de cada frame
    num_frames = spritesheet.get_width() // largura_frame
    altura_frame = spritesheet.get_height()

    frames = []
    for i in range(num_frames):
        # recorta cada frame da imagem usando a posição x de cada um
        frame = spritesheet.subsurface((i * largura_frame, 0, largura_frame, altura_frame))
        frames.append(frame)

    return frames  # retorna a lista com todos os frames recortados

class Personagem:
    def __init__(self, x, y, largura, altura, velocidade, velocidade_corrida, estado, animacoes, velocidade_animacao):
        # posição inicial do personagem na tela
        self.x = x
        self.y = y
        self.hitbox = {"rect": pygame.Rect(x, y, largura, altura)} 

        # velocidade normal e velocidade ao segurar shift
        self.velocidade = velocidade
        self.velocidade_corrida = velocidade_corrida

        # estado atual do personagem: começa parado
        self.estado = estado
        self.estado_anterior = estado  # guarda o estado do frame anterior pra saber se mudou

        # controle da animação
        self.frame_atual = 0   # qual frame da lista está sendo mostrado agora
        self.contador = 0      # conta quantas iterações do loop já passaram

        self.olhando_direita = True  # controla se o sprite precisa ser espelhado ou não

        # quando bloqueado, o personagem não pode fazer outra ação
        # isso acontece durante ataques, hurt e dead
        self.bloqueado = False

        # carrega todas as animações do personagem
        # cada chave do dicionário é um estado, e o valor é a lista de frames daquele estado
        self.animacoes = animacoes

        # velocidade de cada animação separadamente
        # quanto menor o número, mais rápido troca os frames
        self.velocidade_animacao = velocidade_animacao

    def atualizar(self):
        # se o estado mudou, reseta a animação do zero
        # sem isso, o personagem começaria do meio da animação nova
        if self.estado != self.estado_anterior:
            self.frame_atual = 0
            self.contador = 0
        
        self.hitbox["rect"].x = self.x
        self.hitbox["rect"].y = self.y

        self.avancar_animacao()

    def avancar_animacao(self):
        # incrementa o contador a cada iteração do loop
        self.contador += 1

        # só troca o frame quando o contador atingir o limite daquele estado
        if self.contador >= self.velocidade_animacao[self.estado]:
            self.contador = 0
            # o % faz o frame voltar pra 0 depois do último, criando o loop da animação
            self.frame_atual = (self.frame_atual + 1) % len(self.animacoes[self.estado])

    def desenhar(self, tela):
        # pega o frame atual da animação do estado correto
        frame = self.animacoes[self.estado][self.frame_atual]

        # se estiver olhando para a esquerda, espelha a imagem horizontalmente
        # o True no primeiro parâmetro espelha no eixo X, o False no Y não mexe
        if not self.olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        # teste de hitbox
        # a = pygame.Surface(self.hitbox["rect"].size, pygame.SRCALPHA)
        # a.fill((255,255,255,127))
        # tela.blit(a, (self.hitbox["rect"].x +37.5, self.hitbox["rect"].y +30))

        # desenha o frame na posição do personagem
        tela.blit(
        frame,
        (
            self.x - camera.x,
            self.y - camera.y
        )
        )