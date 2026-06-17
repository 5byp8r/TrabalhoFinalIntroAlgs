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

from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

from src.npc import NPC

from src.camera import (
    camera,
    criar_tela
)    

from src.teclas import pressionado

from src.texto import Texto, texto_desafio

from src.personagem import Personagem

from src.desafios import Carta

tipos_tile = [
    TipoTile("dirt", "assets/imagens/Tiles/GK_JC_Free_040.png", False),
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

    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    bat_hitbox = {"rect": bat_image.get_rect(topleft=(300, 400))}
    inimigo = Sprite(bat_image, 300, 400, bat_hitbox)

    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)
    gem_hitbox = {"rect": gem_image.get_rect(topleft=(500 , 200))}
    gema = Sprite(gem_image, 500, 200, gem_hitbox)

    jogador = Personagem(LARGURA_TELA // 2, ALTURA_TELA // 2)
    npc = NPC(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100, "john")

    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    carta = Carta(0, 0 , "assets/imagens/Desafios/1.png","assets/imagens/Desafios/2.png")

    dialogos = Texto("assets/textos/npc.json", tamanho=48, fundo=pygame.Rect(0, ALTURA_TELA-100, LARGURA_TELA, 100)) 

    pontos = 0

    pista_encontrada = False
    objetivo_encontrado = False
    acao_errada = False
    tempo_esgotado = False

    fonte = pygame.font.Font(None, 36)
    texto = ""
    ativo = False
    caixa = pygame.Rect(250, 500, 300, 40)

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
            delay += relogio.get_time()
            delay = npc.atualizar_dialogos(delay, dialogos)
            if npc.indice_dialogo == -2:
                desafio_aberto = True
        else: 
            delay = 9999

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador.hitbox["rect"].x = limitar_valor(jogador.hitbox["rect"].x, 0, LARGURA_TELA - jogador.hitbox["rect"].width)
        jogador.hitbox["rect"].y = limitar_valor(jogador.hitbox["rect"].y, 0, ALTURA_TELA - jogador.hitbox["rect"].height)

        jogador.desenhar(tela)
        npc.desenhar(tela)
        npc.desenhar_dialogos(tela, dialogos)

        #chamando desfaio
        if desafio_aberto:
            # Desenha a Carta
            carta.desenhar(tela)

            # Desenha a Caixa de resposta
            pygame.draw.rect(tela, (255, 255, 255), caixa, 2)
            texto_surface = fonte.render(texto, True, (255, 255, 255))
            tela.blit(texto_surface, (caixa.x + 5, caixa.y + 5))

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