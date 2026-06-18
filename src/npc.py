import pygame
from src.movel import Movel, carregar_frames
from src.teclas import pressionado
from src.texto import Texto
from src.camera import camera

class NPC(Movel):
    def __init__(self, x, y, nome):
        self.nome = nome # nome do npc

        # índice do diálogo do npc
        # -1 = não falou ainda
        # -2 = falou todos os diálogos
        self.indice_dialogo = -1

        self.travar_dialogo = False

        # velocidade de cada animação separadamente
        # quanto menor o número, mais rápido troca os frames
        velocidade_animacao = {
            "idle":    10,
            "walk":    10,
            "run":     7,
            "attack":  4,  # ataques são mais rápidos
            "hurt":    5,
            "dead":    8,
        }

        # carrega todas as animações do personagem
        # cada chave do dicionário é um estado, e o valor é a lista de frames daquele estado
        animacoes = {
            "idle":    carregar_frames("assets/imagens/npc_1/Idle.png"),
            "walk":    carregar_frames("assets/imagens/npc_1/Walk.png"),
            "run":     carregar_frames("assets/imagens/npc_1/Run.png"),
            "attack":  carregar_frames("assets/imagens/npc_1/Attack.png"),
            "hurt":    carregar_frames("assets/imagens/npc_1/Hurt.png"),
            "dead":    carregar_frames("assets/imagens/npc_1/Dead.png"),
        }

        # armazena a posição inicial da câmera
        self.last_camerax = camera.x
        self.last_cameray = camera.y

        super().__init__(x, y,
                        hitbox = {"rect": pygame.Rect(x, y, 50, 100)},
                        velocidade = 1,
                        velocidade_corrida = 3,
                        estado = "idle",
                        velocidade_animacao = velocidade_animacao,
                        animacoes = animacoes)

    def atualizar(self):
        #atualiza a posição do personagem em relação à câmera
        if self.last_camerax != camera.x: self.x -= (camera.x - self.last_camerax)
        if self.last_cameray != camera.y: self.y -= (camera.y - self.last_cameray)

        # armazena a última posição da câmera
        self.last_camerax = camera.x
        self.last_cameray = camera.y

        super().atualizar()

    def atualizar_dialogos(self, dialogos: Texto):
        #atualiza o índice do diálogo
        if pressionado(pygame.K_SPACE) and (not self.travar_dialogo) and (not self.indice_dialogo == -2):
            self.travar_dialogo = True
            self.indice_dialogo+=1
            if self.indice_dialogo >= len(dialogos._textos[self.nome + "_pista"]): self.indice_dialogo = -2 # se os diálogos chegaram ao final, atualiza com -2
        elif not pressionado(pygame.K_SPACE) and self.travar_dialogo:
            self.travar_dialogo = False

    def desenhar_dialogos(self, tela, dialogos: Texto): 
        dialogos.desenhar(tela, self.nome + "_pista", self.indice_dialogo)  # desenha os dialogos
