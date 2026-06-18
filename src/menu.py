from src.button import Button
from src.camera import (criar_tela)

import pygame, sys

from src.config import ALTURA_TELA, LARGURA_TELA, TITULO_JOGO
BG = pygame.image.load("assets/imagens/botoes/background.png")
tela = criar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_JOGO)


def main_menu(): 

    tela.blit(BG, (0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = pygame.font.Font(None, 100).render("DRECUT", True, "#FFFFFF")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    PLAY_BUTTON = Button(image=pygame.image.load("assets/imagens/botoes/play.png"), pos=(640, 250),text_input="PLAY",font=pygame.font.Font(None, 100), base_color="White", hovering_color="Green")

    tela.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                return True