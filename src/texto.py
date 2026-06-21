import json
import pygame
from src.config import (
    LARGURA_DISPLAY,
    ALTURA_DISPLAY,
    PRETO,
    CINZA,
)

class Texto:
    def __init__(self, caminho_arquivo, tamanho=64, cor=PRETO, fundo:pygame.Rect|None=None, cor_fundo=CINZA):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            self._textos = json.load(arquivo)
        self._fonte = pygame.font.Font(None, tamanho)
        self._cor = cor
        self._fundo = fundo
        self._cor_fundo = cor_fundo

    def setFundo(self, fundo, cor_fundo=CINZA):
        self._fundo = fundo
        self._cor_fundo = cor_fundo

    def desenhar(self, display:pygame.Surface, bloco, indice):
        if indice >= 0:
            texto = self._fonte.render(self._textos[bloco][indice], True, self._cor)

            # se não existe fundo, deseha o texto na posição centro baixo
            if self._fundo == None:
                posicao = texto.get_rect(centerx=LARGURA_DISPLAY / 2, y=ALTURA_DISPLAY-texto.get_height()-21)
            else:
                posicao = texto.get_rect(x=self._fundo.x + 10, centery=self._fundo.centery)
                superficie = pygame.Surface(self._fundo.size, pygame.SRCALPHA)
                superficie.fill(self._cor_fundo)
                display.blit(superficie, self._fundo.topleft)

            display.blit(texto, posicao)

def texto_desafio():
    fonte = pygame.font.Font(None, 36)

    texto = ""
    ativo = False

    caixa = pygame.Rect(250, 500, 300, 40)

    return caixa