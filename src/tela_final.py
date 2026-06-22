import pygame

BRANCO = (255, 255, 255)
SOMBRA = (0, 0, 0)
VERDE = (0, 180, 80)
VERMELHO = (200, 30, 30)


def tela_vitoria(tela, largura_tela, altura_tela, pontos):
    #mostra a tela de vitória até o jogador fechar a janela ou apertar uma tecla.
    fonte_titulo = pygame.font.SysFont(None, 80)
    fonte_pontos = pygame.font.SysFont(None, 40)

    titulo = fonte_titulo.render("VOCÊ VENCEU!", True, VERDE)
    texto_pontos = fonte_pontos.render(f"tempo: {pontos}", True, BRANCO)

    clock = pygame.time.Clock()

    esperando = True
    while esperando:
        clock.tick(60)
        tela.fill((20, 20, 20))

        tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, altura_tela // 2 - 60))
        tela.blit(texto_pontos, (largura_tela // 2 - texto_pontos.get_width() // 2, altura_tela // 2 + 20))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
            if evento.type == pygame.KEYDOWN:
                esperando = False

        pygame.display.flip()


def tela_derrota(tela, largura_tela, altura_tela, pontos):
    #mostra a tela de derrota até o jogador fechar a janela ou apertar uma tecla.
    fonte_titulo = pygame.font.SysFont(None, 80)
    fonte_pontos = pygame.font.SysFont(None, 40)

    titulo = fonte_titulo.render("TEMPO ESGOTADO", True, VERMELHO)
    texto_pontos = fonte_pontos.render(f"tempo: {pontos}", True, BRANCO)

    clock = pygame.time.Clock()

    esperando = True
    while esperando:
        clock.tick(60)
        tela.fill((20, 20, 20))

        tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, altura_tela // 2 - 60))
        tela.blit(texto_pontos, (largura_tela // 2 - texto_pontos.get_width() // 2, altura_tela // 2 + 20))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
            if evento.type == pygame.KEYDOWN:
                esperando = False

        pygame.display.flip()