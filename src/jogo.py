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

from src.jogador import Player

from src.camera import criar_tela

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
    rodando = True

    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    bat_hitbox = {"rect": bat_image.get_rect(topleft=(300, 400))}
    inimigo = Sprite(bat_image, 300, 400, bat_hitbox)

    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)
    gem_hitbox = {"rect": gem_image.get_rect(topleft=(500, 200))}
    gema = Sprite(gem_image, 500, 200, gem_hitbox)

    jogador_image =    pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    jogador_hitbox = {"rect": jogador_image.get_rect(topleft=(110, 120))}
    jogador = Player(jogador_image, 110, 120, jogador_hitbox)

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

        jogador.update()

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.fill(PRETO)

        mapa.desenhar_mapa(tela)
        for s in sprites:

            tela.blit(s.image, s.hitbox["rect"])

        pygame.display.flip()

        pygame.time.delay(1)

    pygame.quit()