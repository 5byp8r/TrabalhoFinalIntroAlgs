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
)

from src import teclas

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
    abrir_desafio
)

from src.sprites import (
    Sprite,
    sprites,
    pegar_sprite,
)

from src.npc import NPC

from src.camera import (
    camera,
    criar_tela
)    

from src.teclas import pressionado, teclas_pressionadas

from src.texto import Texto, texto_desafio

from src.personagem import Personagem

from src.desafios import Carta, caixaResposta

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

    jogador = Personagem(LARGURA_TELA // 2, ALTURA_TELA // 2)
    npc = NPC(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100, "john")

    pontos = 0

    carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")
    caixa_resposta = caixaResposta(LARGURA_TELA // 2 ,ALTURA_TELA - 20 , 300, 40)

    dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_TELA-100, LARGURA_TELA, 100)) 

    pontos = 0

    pista_encontrada = False
    objetivo_encontrado = False
    acao_errada = False
    tempo_esgotado = False

    desafio_aberto = False

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                teclas.teclas_pressionadas.add(evento.key)
            elif evento.type == pygame.KEYUP:
                teclas.teclas_pressionadas.remove(evento.key)

        # Desenhando o mapa na tela quando a camera é 0
        tela.fill(PRETO)
        mapa.desenhar_mapa(tela)
        jogador.atualizar()
        npc.atualizar()

        if verificar_colisao(jogador.hitbox["rect"], npc.hitbox["rect"]):
            npc.atualizar_dialogos(dialogos)
            if npc.indice_dialogo == -2:
                desafio_aberto = True
                npc.indice_dialogo = -3
        else: 
            delay = 1000

        jogador.desenhar(tela)
        npc.desenhar(tela)
        npc.desenhar_dialogos(tela, dialogos)

        #chamando desfaio
        if desafio_aberto:
        # Desenha a Carta
            carta.desenhar(tela)
            caixa_resposta.desenhar(tela)

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    rodando = False  

                caixa_resposta.atualizar(evento) 

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if caixa_resposta.validar("resposta_correta"):
                            objetivo_encontrado = True
                            desafio_aberto = False
                        else:
                            acao_errada = True
                        caixa_resposta.limpar()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:

                        ativo = caixa_resposta.caixa.collidepoint(evento.pos)  # ativa ao clicar na caixa
                        
                        delay += relogio.get_time()
                        if delay >= 300:
                            delay = 0
                            carta.virar()

                if pressionado(pygame.KEYDOWN):
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
        pygame.display.flip()
        
    pygame.quit()