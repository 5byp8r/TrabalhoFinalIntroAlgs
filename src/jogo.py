import pygame

from src.map import (
    TipoTile,
    MAPA,
    Map
)

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    PATH,
    GRASS,
    BORDER,
    CINZA,
    BRANCO,
    tamanho_tile,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    CAMINHO_RANKING
)

from src import entradas

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    recompensa_pista,
    recompensa_objetivo,
    punicao_erro,
    punicao_tempo,
    abrir_desafio,
    validar_resposta,
)

from src.npc import NPC

from src.camera import (
    camera,
    criar_tela
)    

from src.personagem import carregar_frames
from src.texto import Texto, texto_desafio

from src.jogador import Jogador

from src.desafios import Carta, caixaResposta

from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking
)

tipos_tile = [
    TipoTile("dirt", "assets/imagens/Tiles/GK_JC_Free_037.png", False),
    TipoTile("border", "assets/imagens/Tiles/GK_JC_Free_043.png", True),
    TipoTile("grass", "assets/imagens/Tiles/GK_JC_Free_047.png", False),
    TipoTile("path", "assets/imagens/Tiles/GK_JC_Free_041.png", False)
]

mapa = Map(MAPA, tipos_tile, tamanho_tile)

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    
    tela = criar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_JOGO)

    relogio = pygame.time.Clock()
    delay = 0
    rodando = True

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

    jogador = Jogador(  LARGURA_TELA // 2, ALTURA_TELA // 2,
                        largura = 50, 
                        altura = 100,
                        velocidade = 2,
                        velocidade_corrida = 4,
                        estado = "idle",
                        velocidade_animacao = velocidade_animacao_jogador,
                        animacoes = animacoes_jogador)

    npc = NPC(          "john", LARGURA_TELA // 2, ALTURA_TELA // 2 - 100,
                        largura = 50, 
                        altura = 100,
                        velocidade = 0,
                        velocidade_corrida = 0,
                        estado = "idle",
                        velocidade_animacao = velocidade_animacao_npc,
                        animacoes = animacoes_npc)

    pontos = 0

    carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")
    caixa_resposta = caixaResposta(LARGURA_TELA // 2 ,ALTURA_TELA - 50 , 300, 40)
    caixa_insert = caixaResposta(LARGURA_TELA // 2 ,ALTURA_TELA - 50 , 300, 40)
    caixa_insert.texto = "Nome"

    dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_TELA-100, LARGURA_TELA, 100)) 
    
    pista_encontrada = False
    objetivo_encontrado = False
    acao_errada = False
    tempo_esgotado = False
    tempo_limite = FPS * 30
    frame_atual = 0

    desafio_aberto = False

    recorde = carregar_recorde(CAMINHO_RECORDE)

    desafio_finalizado = False

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        entradas.teclas_clicadas.clear()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                entradas.adicionar_tecla(evento.key, evento.unicode)
            if evento.type == pygame.KEYUP:
                entradas.deletar_tecla(evento.key)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                entradas.adicionar_tecla(evento.type * evento.button, evento.pos)
            if evento.type == pygame.MOUSEBUTTONUP:
                entradas.deletar_tecla((evento.type - 1) * evento.button)

        # Desenhando o mapa na tela quando a camera é 0
        tela.fill(PRETO)
        mapa.desenhar_mapa(tela)
        jogador.atualizar()
        npc.atualizar()

        jogador.desenhar(tela)
        npc.desenhar(tela)
        npc.desenhar_dialogos(tela, dialogos)

        if verificar_colisao(jogador.hitbox["rect"], npc.hitbox["rect"]):

            if npc.indice_dialogo == 1:
                caixa_insert.atualizar()

                if entradas.clicado(pygame.K_RETURN):
                    jogador.nome = caixa_insert.texto
                    if not validar_resposta(jogador.nome, "Nome"):
                        npc.indice_dialogo += 1

                if entradas.clicado(pygame.K_SPACE):
                    npc.indice_dialogo = 1

                if entradas.clicado(pygame.MOUSEBUTTONDOWN * 1):
                    ativo = caixa_resposta.caixa.collidepoint(entradas.teclas_clicadas[pygame.MOUSEBUTTONDOWN * 1]) 

                delay += relogio.get_time()
                caixa_insert.desenhar(tela)
                delay = caixa_insert.desenhar(tela, delay)

            else:
                npc.atualizar_dialogos(dialogos)
            
        if npc.indice_dialogo == -2:
            desafio_aberto = True
            npc.indice_dialogo = -3


        #chamando desfaio
        if desafio_aberto:
            caixa_resposta.atualizar() 

            if entradas.clicado(pygame.K_RETURN):
                if validar_resposta(caixa_resposta.texto,"teste"):
                    desafio_finalizado = True
                    objetivo_encontrado = True
                    desafio_aberto = False
                else:
                    acao_errada = True
                caixa_resposta.limpar()

            if entradas.clicado(pygame.MOUSEBUTTONDOWN * 1):
                ativo = caixa_resposta.caixa.collidepoint(entradas.teclas_clicadas[pygame.MOUSEBUTTONDOWN * 1])  # ativa ao clicar na caixa

                if not ativo: carta.virar()

            delay += relogio.get_time()
            # Desenha a Carta
            carta.desenhar(tela)
            delay = caixa_resposta.desenhar(tela, delay)

            if entradas.clicado(pygame.K_ESCAPE):
                desafio_aberto = False

        #recompensa por pista coletada (gema) e objetivos
        if  pista_encontrada:
            pontos = recompensa_pista(pontos, 10)

        if objetivo_encontrado:
            pontos = recompensa_objetivo(pontos, 50)

        #sistema de punição
        if acao_errada:
            pontos = punicao_erro(pontos, 20)

        if tempo_esgotado:
            pontos = punicao_tempo(pontos, 30)

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        if desafio_finalizado:
            salvar_ranking(CAMINHO_RANKING, jogador.nome, pontos)
            carregar_ranking(CAMINHO_RANKING)
            desafio_finalizado = False

        frame_atual += 1 
        if frame_atual >= tempo_limite:
            tempo_esgotado = True
        pygame.display.flip()

    pygame.quit()