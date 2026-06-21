import pygame

camera = pygame.Rect(0,0,0,0)

def criar_display(ALTURA_DISPLAY, LARGURA_DISPLAY, TITULO_JOGO):
    pygame.display.set_caption(TITULO_JOGO)

    display = pygame.display.set_mode(( LARGURA_DISPLAY, ALTURA_DISPLAY))
    camera.width = LARGURA_DISPLAY
    camera.height =  ALTURA_DISPLAY

    return display