import pygame
from src.personagem import Personagem, carregar_frames
from src.entradas import clicado
from src.texto import Texto
from src.camera import camera

class NPC(Personagem):
    def __init__(self, nome, x, y, largura, altura, velocidade, velocidade_corrida, estado, animacoes, velocidade_animacao):
        self.nome = nome # nome do npc

        # índice do diálogo do npc
        # -1 = não falou ainda
        # -2 = falou todos os diálogos
        self.indice_dialogo = -1

        # armazena a posição inicial da câmera
        self.last_camerax = camera.x
        self.last_cameray = camera.y

        super().__init__(x, y, largura, altura, velocidade, velocidade_corrida, estado, animacoes, velocidade_animacao)

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
        if clicado(pygame.K_SPACE) and (not self.indice_dialogo == -2):
            self.indice_dialogo+=1
            if self.indice_dialogo >= len(dialogos._textos[self.nome + "_pista"]): self.indice_dialogo = -2 # se os diálogos chegaram ao final, atualiza com -2

    def desenhar_dialogos(self, tela, dialogos: Texto): 
        dialogos.desenhar(tela, self.nome + "_pista", self.indice_dialogo)  # desenha os dialogos
