import pygame

from src.map import (
    TipoTile,
    MAPA,
    Map
)

from src.config import (
    LARGURA_DISPLAY,
    ALTURA_DISPLAY,
    FPS,
    TITULO_JOGO,
    PRETO,
    PATH,
    GRASS,
    BORDER,
    CINZA,
    BRANCO,
    TAMANHO_TILE,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    CAMINHO_RANKING
)

from src import entradas

from src.funcoes import (
    limitar_valor,
    verificar_colisao,
    vitimas_perdidas,
    tempo_jogo,
    quantidade_vitimas,
    punicao_tempo_jogo,
    abrir_desafio,
    validar_resposta,
)

from src.npc import NPC

from src.camera import (
    camera,
    criar_display
)    

from src.personagem import carregar_frames
from src.texto import Texto, texto_desafio

from src.jogador import Jogador

from src.desafios import Carta, caixaTexto

from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking
)

from src.executar_jogo import exitGame

from src.tela_final import tela_derrota, tela_vitoria

class Jogo:
    # Instancia variáveis do jogo
    def __init__(self, display):
        self.display = display
        self.relogio = pygame.time.Clock()

        tipos_tile = [
            TipoTile("border", "assets/imagens/Tiles/GK_JC_Free_043.png", True),
            TipoTile("dirt", "assets/imagens/Tiles/GK_JC_Free_037.png", False),
            TipoTile("grass", "assets/imagens/Tiles/GK_JC_Free_047.png", False),
            TipoTile("path", "assets/imagens/Tiles/GK_JC_Free_041.png", False)
        ]

        self.mapa = Map(MAPA, tipos_tile, TAMANHO_TILE)

        # carrega todas as animações do jogador
        # cada chave do dicionário é um estado, e o valor é a lista de frames daquele estado
        animacoes_jogador = {
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

        # carrega todas as animações do npc
        animacoes_npc = {
            "idle":    carregar_frames("assets/imagens/npc_1/Idle.png"),
            "walk":    carregar_frames("assets/imagens/npc_1/Walk.png"),
            "run":     carregar_frames("assets/imagens/npc_1/Run.png"),
            "attack":  carregar_frames("assets/imagens/npc_1/Attack.png"),
            "hurt":    carregar_frames("assets/imagens/npc_1/Hurt.png"),
            "dead":    carregar_frames("assets/imagens/npc_1/Dead.png"),
        }

        # velocidade de cada animação do jogador separadamente
        # quanto menor o número, mais rápido troca os frames
        velocidade_animacao_jogador = {
            "idle":    10,
            "idle2":   10,
            "walk":    5,
            "run":     5,
            "jump":    8,
            "attack1": 4,  # ataques são mais rápidos
            "attack2": 4,
            "attack3": 4,
            "hurt":    5,
            "dead":    8,
        }

        # velocidade de cada animação do npc separadamente
        velocidade_animacao_npc = {
            "idle":    10,
            "walk":    10,
            "run":     7,
            "attack":  4,  # ataques são mais rápidos
            "hurt":    5,
            "dead":    8,
        }

        self.jogador = Jogador(LARGURA_DISPLAY // 2, ALTURA_DISPLAY // 2,
                            largura = 32, 
                            altura = 64,
                            velocidade = 4,
                            velocidade_corrida = 10,
                            estado = "idle",
                            velocidade_animacao = velocidade_animacao_jogador,
                            animacoes = animacoes_jogador)

        self.npc = NPC("john", LARGURA_DISPLAY // 2, ALTURA_DISPLAY // 2 - 100,
                        largura = 50, 
                        altura = 100,
                        velocidade = 0,
                        velocidade_corrida = 0,
                        estado = "idle",
                        velocidade_animacao = velocidade_animacao_npc,
                        animacoes = animacoes_npc)

        self.delay = 0
        self.fonte_timer = pygame.font.Font(None, 36)

        self.carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")
        self.caixa_resposta = caixaTexto(LARGURA_DISPLAY // 2 ,ALTURA_DISPLAY - 50 , 300, 40)
        self.caixa_insert = caixaTexto(LARGURA_DISPLAY // 2 ,ALTURA_DISPLAY - 50 , 300, 40)
        self.caixa_insert.texto = "Nome"
        self.dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_DISPLAY-100, LARGURA_DISPLAY, 100)) 
        self.vitimas = ["vitima_1","vitima_1","vitima_1","vitima_1","vitima_1","vitima_1"]
        self.vitimas_vivas = len(self.vitimas)
        self.vitimas_perdidas_quantidade = 0
        self.desafio_aberto = False
        self.recorde = carregar_recorde(CAMINHO_RECORDE)
        self.desafio_finalizado = False
        self.jogo_iniciado = False
        self.desenhar_caixa_insert = False
        self.desenhar_carta = False
        self.tempo_limite_ms = 30 * 60 * 1000
        self.penalidade_tempo_ms = 0

        self.pontos = 0
        self.tempo_inicio = pygame.time.get_ticks()

    # Atualiza estado, colisões e pontuação do jogo
    def atualizar(self):
        self.relogio.tick(FPS)
        self.jogador.atualizar(self.mapa)
        self.npc.atualizar()

        if verificar_colisao(self.jogador.hitbox["rect"], self.npc.hitbox["rect"]):

            if self.npc.indice_dialogo == 1:
                self.caixa_insert.atualizar()

                if entradas.clicado(pygame.K_RETURN):
                    self.jogador.nome = self.caixa_insert.texto
                    if not validar_resposta(self.jogador.nome, "Nome"):
                        self.npc.indice_dialogo += 1

                if entradas.clicado(pygame.K_SPACE):
                    self.npc.indice_dialogo = 1

                if entradas.clicado(pygame.MOUSEBUTTONDOWN * 1):
                    ativo = self.caixa_resposta.caixa.collidepoint(entradas.teclas_clicadas[pygame.MOUSEBUTTONDOWN * 1]) 

                self.desenhar_caixa_insert = True

            else:
                self.desenhar_caixa_insert = False
                self.npc.atualizar_dialogos(self.dialogos)
            
        if self.npc.indice_dialogo == -2:
            self.desafio_aberto = True
            self.npc.indice_dialogo = -3

        #chamando desfaio
        if self.desafio_aberto:
            self.caixa_resposta.atualizar() 

            if entradas.clicado(pygame.K_RETURN):

                if validar_resposta(self.caixa_resposta.texto,"teste"):
                    self.desafio_finalizado = True
                    self.desafio_aberto = False
                    self.caixa_resposta.limpar()

                    tempo_finalizado_ms = pygame.time.get_ticks() - self.tempo_inicio + self.penalidade_tempo_ms
                    segundos = tempo_finalizado_ms // 1000
                    minutos = segundos // 60
                    segundos = segundos % 60
                    tempo_formatado = f"{minutos:02d}:{segundos:02d}"

                    self.pontos = tempo_formatado
                    tela_vitoria(self.display, LARGURA_DISPLAY, ALTURA_DISPLAY, self.pontos)

                    if self.pontos > self.recorde:
                        self.recorde = self.pontos
                        salvar_recorde(CAMINHO_RECORDE, self.recorde)
                        
                else:
                    self.penalidade_tempo_ms += 30 * 1000
                    self.caixa_resposta.limpar()
                
            if entradas.clicado(pygame.MOUSEBUTTONDOWN * 1):
                ativo = self.caixa_resposta.caixa.collidepoint(entradas.teclas_clicadas[pygame.MOUSEBUTTONDOWN * 1])  # ativa ao clicar na caixa
                if not ativo: self.carta.virar()

            # Desenha a Carta
            self.desenhar_carta = True

            if entradas.clicado(pygame.K_ESCAPE):
                self.desafio_aberto = False
        
        else:
            self.desenhar_carta = False


        #sistema de recompensa e punição por tempo com sistema de relogio do pygame
        ticks_atual = pygame.time.get_ticks()
        
        if quantidade_vitimas(ticks_atual, self.vitimas_perdidas_quantidade, minutos=5):
            self.vitimas_vivas -= 1
            self.vitimas_perdidas_quantidade += 1

        tempo_decorrido = ticks_atual - self.tempo_inicio + self.penalidade_tempo_ms
        tempo_restante_ms = max(0, self.tempo_limite_ms - tempo_decorrido)

        if tempo_jogo(ticks_atual, minutos=30):
            self.pontos = punicao_tempo_jogo(self.pontos, 30)
            tela_derrota(self.display, LARGURA_DISPLAY, ALTURA_DISPLAY, self.pontos)
            exitGame()
            return False
        
        if vitimas_perdidas(self.vitimas_vivas):
            tela_derrota(self.display, LARGURA_DISPLAY, ALTURA_DISPLAY, self.pontos)
            exitGame()
            return False

        if self.desafio_finalizado:
            salvar_ranking(CAMINHO_RANKING, self.jogador.nome, tempo_formatado)
            self.desafio_finalizado = False

        ticks_atual = pygame.time.get_ticks()
        tempo_decorrido = ticks_atual - self.tempo_inicio + self.penalidade_tempo_ms
        tempo_restante_ms = max(0, self.tempo_limite_ms - tempo_decorrido)

        segundos_restantes = tempo_restante_ms // 1000
        self.minutos_jogo = segundos_restantes // 60
        self.segundos_jogo = segundos_restantes % 60

        return True
    
    def desenhar(self):
        self.display.fill(PRETO)
        self.mapa.desenhar_mapa(self.display)

        self.jogador.desenhar(self.display)
        self.npc.desenhar(self.display)
        self.npc.desenhar_dialogos(self.display, self.dialogos)

        if self.desenhar_caixa_insert:
            self.delay += self.relogio.get_time()
            self.delay = self.caixa_insert.desenhar(self.display, self.delay)

        if self.desenhar_carta:
            self.carta.desenhar(self.display)
            self.delay += self.relogio.get_time()
            self.delay = self.caixa_resposta.desenhar(self.display, self.delay)


        texto_tempo_jogo = self.fonte_timer.render(
            f"Tempo total: {self.minutos_jogo:02d}:{self.segundos_jogo:02d}", True, BRANCO
        )
        texto_vitimas = self.fonte_timer.render(
            f"Vitimas Vivas: {self.vitimas_vivas}/{len(self.vitimas)}", True, BRANCO
        )

        self.display.blit(texto_tempo_jogo, (10, 10))
        self.display.blit(texto_vitimas, (10, 50))
        pygame.display.flip()