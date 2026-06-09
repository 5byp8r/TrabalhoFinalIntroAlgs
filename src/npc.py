import pygame
from src.teclas import pressionado
from src.sprites import Sprite
from src.texto import Texto
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


class NPC:
    def __init__(self, x, y, name):
        self.i = -1
        self.name = name

        # posição inicial do personagem na tela
        self.x = x
        self.y = y
        self.hitbox = {"rect": pygame.Rect(x, y, 128, 128)} 

        # velocidade normal e velocidade ao segurar shift
        self.velocidade = 1
        self.velocidade_corrida = 3

        # estado atual do personagem: começa parado
        self.estado = "idle"
        self.estado_anterior = "idle"  # guarda o estado do frame anterior pra saber se mudou

        # controle da animação
        self.frame_atual = 0   # qual frame da lista está sendo mostrado agora
        self.contador = 0      # conta quantas iterações do loop já passaram

        # velocidade de cada animação separadamente
        # quanto menor o número, mais rápido troca os frames
        self.velocidade_animacao = {
            "idle":    10,
            "walk":    10,
            "run":     7,
            "attack1": 4,  # ataques são mais rápidos
            "hurt":    5,
            "dead":    8,
        }

        self.olhando_direita = True  # controla se o sprite precisa ser espelhado ou não

        # quando bloqueado, o personagem não pode fazer outra ação
        # isso acontece durante ataques, hurt e dead
        self.bloqueado = False


        # carrega todas as animações do personagem
        # cada chave do dicionário é um estado, e o valor é a lista de frames daquele estado
        self.animacoes = {
            "idle":    carregar_frames("assets/imagens/npc_1/Idle.png"),
            "walk":    carregar_frames("assets/imagens/npc_1/Walk.png"),
            "run":     carregar_frames("assets/imagens/npc_1/Run.png"),
            "attack1": carregar_frames("assets/imagens/npc_1/Attack.png"),
            "hurt":    carregar_frames("assets/imagens/npc_1/Hurt.png"),
            "dead":    carregar_frames("assets/imagens/npc_1/Dead.png"),
        }



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

        # captura todas as teclas que estão pressionadas agora
        # teclas = pygame.key.get_pressed()
        # movendo = False
        # correndo = teclas[pygame.K_LSHIFT]  # verifica se shift está pressionado

        # # move o personagem e atualiza a direção que ele está olhando
        # if teclas[pygame.K_LEFT]:
        #     vel = self.velocidade_corrida if correndo else self.velocidade
        #     self.x -= vel
        #     movendo = True
        #     self.olhando_direita = False  # virou para a esquerda

        # if teclas[pygame.K_RIGHT]:
        #     vel = self.velocidade_corrida if correndo else self.velocidade
        #     self.x += vel
        #     movendo = True
        #     self.olhando_direita = True  # virou para a direita

        # if teclas[pygame.K_UP]:
        #     vel = self.velocidade_corrida if correndo else self.velocidade
        #     self.y -= vel
        #     movendo = True

        # if teclas[pygame.K_DOWN]:
        #     vel = self.velocidade_corrida if correndo else self.velocidade
        #     self.y += vel
        #     movendo = True

        # # define o estado de movimento baseado no que está acontecendo
        # if movendo:
        #     self.estado = "run" if correndo else "walk"
        # else:
        #     self.estado = "idle"

        # ataques têm prioridade, substituem o estado de movimento
        # ao atacar, bloqueia pra animação terminar antes de fazer outra coisa
        # if teclas[pygame.K_z]:
        #     self.estado = "attack1"
        #     self.bloqueado = True
        # elif teclas[pygame.K_x]:
        #     self.estado = "attack2"
        #     self.bloqueado = True
        # elif teclas[pygame.K_c]:
        #     self.estado = "attack3"
        #     self.bloqueado = True

        # se o estado mudou, reseta a animação do zero
        # sem isso, o personagem começaria do meio da animação nova
        if self.estado != self.estado_anterior:
            self.frame_atual = 0
            self.contador = 0
        
        self.hitbox["rect"].x = self.x
        self.hitbox["rect"].y = self.y

        self.avancar_animacao()

    def atualizar_dialogos(self, delay, dialogos: Texto):
        if pressionado(pygame.K_SPACE) and delay > 1000 and not self.i == -2:
            self.i+=1
            if self.i >= len(dialogos.textos[self.name]): self.i = -2
            return 0
        return delay

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

        # desenha o frame na posição do personagem
        tela.blit(frame, (self.x - camera.x , self.y - camera.y))

    def desenhar_dialogos(self, tela, dialogos: Texto): 
        dialogos.desenhar(tela, self.name, self.i)  # desenha os dialogos
