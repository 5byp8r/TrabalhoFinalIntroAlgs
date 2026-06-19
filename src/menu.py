import pygame

BRANCO = (255, 255, 255)
AZUL_TRANSLUCIDO = (0, 80, 200, 180)
AZUL_HOVER = (0, 140, 255, 220)
SOMBRA = (0, 0, 0)


class Button:
    def __init__(self, text, center_y, action, largura_tela):
        self.text = text
        self.action = action
        self.center_y = center_y
        self.widht, self.height = 320, 70
        self.rect = pygame.Rect((0, 0, self.widht, self.height))
        self.rect.center = (largura_tela // 2, center_y)

    def draw(self, win, mouse_pos, fonte_botao):
        is_hover = self.rect.collidepoint(mouse_pos)
        color = AZUL_HOVER if is_hover else AZUL_TRANSLUCIDO
        superficie_botao = pygame.Surface((self.widht, self.height), pygame.SRCALPHA)
        pygame.draw.rect(superficie_botao, color, (0, 0, self.widht, self.height), border_radius=16)
        win.blit(superficie_botao, self.rect)

        text_surf = fonte_botao.render(self.text, True, BRANCO)
        text_rect = text_surf.get_rect(center=self.rect.center)

        shadow = fonte_botao.render(self.text, True, SOMBRA)
        win.blit(shadow, (text_rect.x + 2, text_rect.y + 2))
        win.blit(text_surf, text_rect)

    def clicado(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


def main_menu(tela, largura_tela, altura_tela):
    """Mostra o menu e fica nele até o jogador clicar em Jogar ou Sair.
    Retorna True para seguir pro jogo, False para fechar tudo."""

    background = pygame.image.load("assets/imagens/botoes/background.png")
    background = pygame.transform.scale(background, (largura_tela, altura_tela))

    fonte_titulo = pygame.font.SysFont(None, 72)
    fonte_botao = pygame.font.SysFont(None, 36)

    botoes = [
        Button("Iniciar Jogo", 320, "Jogar", largura_tela),
        Button("Sair do jogo", 420, "Sair", largura_tela),
    ]

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        tela.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        titulo = fonte_titulo.render("DRECUT", True, BRANCO)
        shadow = fonte_titulo.render("DRECUT", True, SOMBRA)
        tela.blit(shadow, (largura_tela // 2 - titulo.get_width() // 2 + 3, 103))
        tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, 100))

        for btn in botoes:
            btn.draw(tela, mouse_pos, fonte_botao)
            if btn.clicado(mouse_pos, mouse_pressed):
                if btn.action == "Jogar":
                    return True
                elif btn.action == "Sair":
                    return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.flip()