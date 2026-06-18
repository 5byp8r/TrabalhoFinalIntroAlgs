import pygame, sys
from src.jogo import screen as SCREEN

def main_menu(): 
    pygame.display.set_caption("MENU")

    while True:
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("DRECUT", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image/load("assets/imagens/botoes/play.png"), pos=(640, 250))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

            pygame.display.update()

main_menu()