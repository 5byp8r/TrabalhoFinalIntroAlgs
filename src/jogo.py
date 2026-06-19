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
    limitar_valor,
    verificar_colisao,
    vitimas_perdidas,
    tempo_jogo,
    tempo_por_enigma,
    punicao_tempo_jogo,
    punicao_tempo_enigma,
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

    tela = criar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_JOGO)
    fonte_timer = pygame.font.Font(None, 36)
    relogio = pygame.time.Clock()
    delay = 0
    rodando = True

    jogador = Personagem(LARGURA_TELA // 2, ALTURA_TELA // 2)
    npc = NPC(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100, "john")

    pontos = 0

    carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")
    caixa_resposta = caixaResposta(LARGURA_TELA // 2 ,ALTURA_TELA - 50 , 300, 40)

    dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_TELA-100, LARGURA_TELA, 100)) 

    pontos = 0

    vitimas = ["vitima_1", "vitima_2", "vitima_3", "vitima_4", "vitima_5", "vitima_6"]
    vitimas_vivas = len(vitimas)
    enigma_atual = 0
    frame_atual = 0
    frame_enigma = 0

    #pista_encontrada = False
    #objetivo_completo = False
    #tempo_esgotado = False
    #tempo_limite = FPS * 30
    #tempo_limite_enigma = FPS * 5
    #punicao_tempo_enigma = False
    #frame_atual = 0

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
                frame_enigma = 0
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
                if evento.type == pygame.KEYDOWN:
                    teclas.teclas_pressionadas.add(evento.key)
                elif evento.type == pygame.KEYUP:
                    teclas.teclas_pressionadas.remove(evento.key)
               
                caixa_resposta.atualizar(evento) 

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if caixa_resposta.validar("resposta_correta"):
                            enigma_atual += 1
                            frame_enigma = 0
                            desafio_aberto = False
                            caixa_resposta.limpar()
                        #else:
                         #   acao_errada = True
                        #caixa_resposta.limpar()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:

                        ativo = caixa_resposta.caixa.collidepoint(evento.pos)  # ativa ao clicar na caixa
                        
                        delay += relogio.get_time()
                        if delay >= 300:
                            delay = 0
                            carta.virar()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        desafio_aberto = False

        frame_atual += 1
        if desafio_aberto:
            frame_enigma += 1

        if tempo_por_enigma(frame_enigma, FPS, minutos=5):
            vitimas_vivas = punicao_tempo_enigma(vitimas_vivas)
            enigma_atual += 1
            frame_enigma = 0

        if tempo_jogo(frame_atual, FPS, minutos=30):
            pontos = punicao_tempo_jogo(pontos, 30)
            rodando = False

        if vitimas_perdidas(vitimas_vivas):
            rodando = False

        if enigma_atual >= len(vitimas):
            rodando = False

        segundos_totais = max(0, (FPS * 60 * 30 - frame_atual) // FPS)
        minutos_jogo = segundos_totais // 60
        segundos_jogo = segundos_totais % 60

        segundos_enigma = max(0, (FPS * 60 * 5 - frame_atual) // FPS)
        minutos_enigma = segundos_enigma // 60
        segundos_enigma_resto = segundos_enigma % 60

        texto_tempo_jogo = fonte_timer.render(
            f"Tempo total: {minutos_jogo:02d}:{segundos_jogo:02d}", True, BRANCO
        )
        texto_tempo_enigma = fonte_timer.render(
            f"Enigma: {minutos_enigma:02d}:{segundos_enigma_resto:02d}", True, BRANCO
        )

        tela.blit(texto_tempo_jogo, (10, 10))
        if desafio_aberto:
            tela.blit(texto_tempo_enigma, (10, 50))

        pygame.display.flip()
        
    pygame.quit()