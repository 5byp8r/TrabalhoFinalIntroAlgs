import pygame
from src import entradas
from src.config import (
    BRANCO,
    AZUL_TRANSLUCIDO,
    AZUL_HOVER,
    PRETO
)

class Botao:
    def __init__(self, texto, centro_y, acao, largura_display):
        self.texto = texto
        self.acao = acao
        self.centro_y = centro_y

        self.largura = 320
        self.altura = 70

        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = (largura_display // 2, centro_y)

    def desenhar(self, display, fonte_botao):
        mouse_pos = pygame.mouse.get_pos()
        esta_emcima = self.rect.collidepoint(mouse_pos)

        cor = AZUL_HOVER if esta_emcima else AZUL_TRANSLUCIDO

        superficie_botao = pygame.Surface(
            (self.largura, self.altura),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            superficie_botao,
            cor,
            (0, 0, self.largura, self.altura),
            border_radius=16
        )

        display.blit(superficie_botao, self.rect)

        texto_surperficie = fonte_botao.render(self.texto, True, BRANCO)
        texto_rect = texto_surperficie.get_rect(center=self.rect.center)

        sombra = fonte_botao.render(self.texto, True, PRETO)

        display.blit(sombra, (texto_rect.x + 2, texto_rect.y + 2))
        display.blit(texto_surperficie, texto_rect)

    def clicado(self):
        tecla_mouse = pygame.MOUSEBUTTONDOWN * 1

        if entradas.clicado(tecla_mouse):
            posicao_clique = entradas.teclas_clicadas[tecla_mouse]

            if self.rect.collidepoint(posicao_clique):
                return self.acao

        return None