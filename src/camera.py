import pygame

camera = pygame.Rect(0,0,0,0)

def criar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_JOGO):
    pygame.display.set_caption(TITULO_JOGO)

    tela = pygame.display.set_mode(( LARGURA_TELA, ALTURA_TELA))
    camera.width = LARGURA_TELA
    camera.height =  ALTURA_TELA

    return tela