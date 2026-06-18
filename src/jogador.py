import pygame
from src.personagem import Personagem, carregar_frames
from src.camera import camera
from src.entradas import pressionado

class Jogador(Personagem):
    def __init__(self, x, y, largura, altura, velocidade, velocidade_corrida, estado, animacoes, velocidade_animacao):
        self.nome = ""
        super().__init__(x, y, largura, altura, velocidade, velocidade_corrida, estado, animacoes, velocidade_animacao)

    def atualizar(self):
        # guarda o estado atual antes de qualquer coisa
        # assim dá pra saber se ele mudou no final
        self.estado_anterior = self.estado

        # se estiver no meio de um ataque ou levando dano, espera terminar
        # só desbloqueia quando chegar no último frame da animação
        if self.bloqueado:
            self.avancar_animacao()
            if self.frame_atual == len(self.animacoes[self.estado]) - 1:
                self.bloqueado = False
                if self.estado != "dead":  # se morreu, fica no chão
                    self.estado = "idle"
            return  # sai do método sem processar movimento

        movendo = False
        correndo = pressionado(pygame.K_LSHIFT)  # verifica se shift está pressionado

        # move o personagem e atualiza a direção que ele está olhando
        if pressionado(pygame.K_LEFT) or pressionado(pygame.K_a):
            vel = self.velocidade_corrida if correndo else self.velocidade
            self.x -= vel
            movendo = True
            self.olhando_direita = False  # virou para a esquerda

        if pressionado(pygame.K_RIGHT) or pressionado(pygame.K_d):
            vel = self.velocidade_corrida if correndo else self.velocidade
            self.x += vel
            movendo = True
            self.olhando_direita = True  # virou para a direita

        if pressionado(pygame.K_UP) or pressionado(pygame.K_w):
            vel = self.velocidade_corrida if correndo else self.velocidade
            self.y -= vel
            movendo = True

        if pressionado(pygame.K_DOWN) or pressionado(pygame.K_s):
            vel = self.velocidade_corrida if correndo else self.velocidade
            self.y += vel
            movendo = True

        # define o estado de movimento baseado no que está acontecendo
        if movendo:
            self.estado = "run" if correndo else "walk"
        else:
            self.estado = "idle"

        # ataques têm prioridade, substituem o estado de movimento
        # ao atacar, bloqueia pra animação terminar antes de fazer outra coisa
        if pressionado(pygame.K_z):
            self.estado = "attack1"
            self.bloqueado = True
        elif pressionado(pygame.K_x):
            self.estado = "attack2"
            self.bloqueado = True
        elif pressionado(pygame.K_c):
            self.estado = "attack3"
            self.bloqueado = True

        # se o estado mudou, reseta a animação do zero
        # sem isso, o personagem começaria do meio da animação nova
        if self.estado != self.estado_anterior:
            self.frame_atual = 0
            self.contador = 0

        # atualiza a câmera para seguir o personagem
        camera.x = self.x - camera.width // 2 + 64
        camera.y = self.y - camera.height // 2 + 64

        super().atualizar()