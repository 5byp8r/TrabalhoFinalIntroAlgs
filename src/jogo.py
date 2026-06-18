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
    abrir_desafio
)

from src.npc import NPC

from src.camera import (
    camera,
    criar_tela
)    

from src.texto import Texto, texto_desafio

from src.jogador import Jogador

from src.desafios import Carta, caixaResposta

from src.menu import main_menu

tipos_tile = [
    TipoTile("dirt", "assets/imagens/Tiles/GK_JC_Free_037.png", False),
    TipoTile("border", "assets/imagens/Tiles/GK_JC_Free_043.png", True),
    TipoTile("grass", "assets/imagens/Tiles/GK_JC_Free_047.png", False),
    TipoTile("path", "assets/imagens/Tiles/GK_JC_Free_041.png", False)
]

mapa = Map(MAPA, tipos_tile, tamanho_tile)

screen = None

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    
    tela = criar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_JOGO)
    screen = tela

    relogio = pygame.time.Clock()
    delay = 0
    rodando = True

    jogador = Jogador(LARGURA_TELA // 2, ALTURA_TELA // 2)
    npc = NPC("john", LARGURA_TELA // 2, ALTURA_TELA // 2 - 100)

    pontos = 0

    carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")
    caixa_resposta = caixaResposta(LARGURA_TELA // 2 ,ALTURA_TELA - 50 , 300, 40)

    dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_TELA-100, LARGURA_TELA, 100)) 

    pontos = 0

    pista_encontrada = False
    objetivo_encontrado = False
    acao_errada = False
    tempo_esgotado = False
    tempo_limite = FPS * 30
    frame_atual = 0

    desafio_aberto = False

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:

        main_menu()

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

        if verificar_colisao(jogador.hitbox["rect"], npc.hitbox["rect"]):
            npc.atualizar_dialogos(dialogos)
            if npc.indice_dialogo == -2:
                desafio_aberto = True
                npc.indice_dialogo = -3

        jogador.desenhar(tela)
        npc.desenhar(tela)
        npc.desenhar_dialogos(tela, dialogos)

        #chamando desfaio
        if desafio_aberto:
            caixa_resposta.atualizar() 

            if entradas.clicado(pygame.K_RETURN):
                if caixa_resposta.validar("resposta_correta"):
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

        frame_atual += 1 
        if frame_atual >= tempo_limite:
            tempo_esgotado = True
        pygame.display.flip()

    pygame.quit()