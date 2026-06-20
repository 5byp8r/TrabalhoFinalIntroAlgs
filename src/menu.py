import pygame
from src import entradas

BRANCO = (255, 255, 255)
AZUL_TRANSLUCIDO = (0, 80, 200, 180)
AZUL_HOVER = (0, 140, 255, 220)
SOMBRA = (0, 0, 0)


class Button:
    def __init__(self, text, center_y, action, largura_tela):
        self.text = text
        self.action = action
        self.center_y = center_y

        self.width = 320
        self.height = 70

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (largura_tela // 2, center_y)

    def draw(self, win, fonte_botao):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)

        color = AZUL_HOVER if is_hover else AZUL_TRANSLUCIDO

        superficie_botao = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            superficie_botao,
            color,
            (0, 0, self.width, self.height),
            border_radius=16
        )

        win.blit(superficie_botao, self.rect)

        text_surf = fonte_botao.render(self.text, True, BRANCO)
        text_rect = text_surf.get_rect(center=self.rect.center)

        shadow = fonte_botao.render(self.text, True, SOMBRA)

        win.blit(shadow, (text_rect.x + 2, text_rect.y + 2))
        win.blit(text_surf, text_rect)

    def clicado(self):
        tecla_mouse = pygame.MOUSEBUTTONDOWN * 1

        if entradas.clicado(tecla_mouse):
            posicao_clique = entradas.teclas_clicadas[tecla_mouse]

            if self.rect.collidepoint(posicao_clique):
                return self.action

        return None

class Menu:
    def __init__(self, tela, largura_tela, altura_tela):
        self.tela = tela
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

        self.background = pygame.image.load("assets/imagens/botoes/background.png")
        self.background = pygame.transform.scale(self.background, (largura_tela, altura_tela))

        self.fonte_titulo = pygame.font.SysFont(None, 72)
        self.fonte_botao = pygame.font.SysFont(None, 36)

        self.titulo = self.fonte_titulo.render("DRECUT", True, BRANCO)
        self.shadow = self.fonte_titulo.render("DRECUT", True, SOMBRA)

        # sem vírgula no final -> objetos Button, não tuplas
        self.btn_iniciar = Button("Iniciar Jogo", 320, "Jogar", largura_tela)
        self.btn_sair = Button("Sair do jogo", 420, "Sair", largura_tela)
        self.botoes = [self.btn_iniciar, self.btn_sair]

    def mostrar_menu(self):
        """Desenha o menu e retorna a ação do botão clicado neste frame,
        ou None se nenhum botão foi clicado."""

        self.tela.blit(self.background, (0, 0))
        self.tela.blit(
            self.shadow,
            (self.largura_tela // 2 - self.titulo.get_width() // 2 + 3, 103)
        )
        self.tela.blit(
            self.titulo,
            (self.largura_tela // 2 - self.titulo.get_width() // 2, 100)
        )

        for btn in self.botoes:
            btn.draw(self.tela, self.fonte_botao)

        pygame.display.flip()
