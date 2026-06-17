import pygame
from src.movel import Movel, carregar_frames
from src.camera import camera
from src.teclas import pressionado

class Personagem(Movel):
    def __init__(self, x, y):
        # carrega todas as animações do personagem
        # cada chave do dicionário é um estado, e o valor é a lista de frames daquele estado
        animacoes = {
            "idle":    carregar_frames("assets/imagens/personagem_principal/Idle.png"),
            "idle2":   carregar_frames("assets/imagens/personagem_principal/Idle_2.png"),
            "walk":    carregar_frames("assets/imagens/personagem_principal/Walk.png"),
            "run":     carregar_frames("assets/imagens/personagem_principal/Run.png"),
            "jump":    carregar_frames("assets/imagens/personagem_principal/Jump.png"),
            "attack1": carregar_frames("assets/imagens/personagem_principal/Attack_1.png"),
            "attack2": carregar_frames("assets/imagens/personagem_principal/Attack_2.png"),
            "attack3": carregar_frames("assets/imagens/personagem_principal/Attack_3.png"),
            "hurt":    carregar_frames("assets/imagens/personagem_principal/Hurt.png"),
            "dead":    carregar_frames("assets/imagens/personagem_principal/Dead.png"),
        }

        # velocidade de cada animação separadamente
        # quanto menor o número, mais rápido troca os frames
        velocidade_animacao = {
            "idle":    10,
            "idle2":   10,
            "walk":    10,
            "run":     7,
            "jump":    8,
            "attack1": 4,  # ataques são mais rápidos
            "attack2": 4,
            "attack3": 4,
            "hurt":    5,
            "dead":    8,
        }

        super().__init__(x, y,
                        hitbox = {"rect": pygame.Rect(x, y, 50, 100)},
                        velocidade = 1,
                        velocidade_corrida = 3,
                        estado = "idle",
                        velocidade_animacao = velocidade_animacao,
                        animacoes = animacoes)

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