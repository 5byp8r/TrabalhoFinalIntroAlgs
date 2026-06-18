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
    punicao_tempo
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

from src.camera import (
    camera,
    criar_tela
)    

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
    gem_hitbox = {"rect": gem_image.get_rect(topleft=(500 , 200))}
    gema = Sprite(gem_image, 500, 200, gem_hitbox)

    jogador_image =    pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    jogador_hitbox = {"rect": jogador_image.get_rect(topleft=(LARGURA_TELA // 2, ALTURA_TELA // 2))}
    jogador = Player(jogador_image, (LARGURA_TELA - jogador_image.get_width()) // 2, (ALTURA_TELA - jogador_image.get_height()) // 2, jogador_hitbox)

    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    pontos = 0

    pista_encontrada = False
    objetivo_encontrado = False
    acao_errada = False
    tempo_esgotado = False
    tempo_limite = FPS * 30
    frame_atual = 0

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
        jogador.update()

        
        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador.hitbox["rect"].x = limitar_valor(jogador.hitbox["rect"].x, 0, LARGURA_TELA - jogador.hitbox["rect"].width)
        jogador.hitbox["rect"].y = limitar_valor(jogador.hitbox["rect"].y, 0, ALTURA_TELA - jogador.hitbox["rect"].height)

        # Verificação de colisão com a Gema (antigo 'item')
        if verificar_colisao(jogador.hitbox["rect"], gema.hitbox["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a gema de lugar ao coletar
            gema.hitbox["rect"].x += 80
            gema.hitbox["rect"].y += 50

            # Se a gema sair da tela, volta para uma posição segura
            if gema.hitbox["rect"].x > LARGURA_TELA - gema.hitbox["rect"].width:
                gema.hitbox["rect"].x = 50
            if gema.hitbox["rect"].y > ALTURA_TELA - gema.hitbox["rect"].height:
                gema.hitbox["rect"].y = 50

        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador.hitbox["rect"], inimigo.hitbox["rect"]):
            vidas = tomar_dano(vidas, 1)

            # Afasta o inimigo ao colidir
            inimigo.hitbox["rect"].x += 80
            inimigo.hitbox["rect"].y += 50

            if inimigo.hitbox["rect"].x > LARGURA_TELA - inimigo.hitbox["rect"].width:
                inimigo.hitbox["rect"].x = 50
            if inimigo.hitbox["rect"].y > ALTURA_TELA - inimigo.hitbox["rect"].height:
                inimigo.hitbox["rect"].y = 50

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        for s in sprites:

            tela.blit(s.image, s.hitbox["rect"])
        
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