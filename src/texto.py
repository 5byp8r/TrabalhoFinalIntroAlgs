import json
import pygame
from src.camera import camera

class Texto:
    def __init__(self, caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            self.textos = json.load(arquivo)
        self.font = pygame.font.Font(None, 64)
        self.color = (10, 10, 10)

    def desenhar(self, tela, bloco, indice):
        if indice >= 0:
            text = self.font.render(self.textos[bloco][indice], True, self.color)
            textpos = text.get_rect(centerx=800 / 2, y=15)
            tela.blit(text, textpos)

def texto_desafio():
    fonte = pygame.font.Font(None, 36)

    texto = ""
    ativo = False

    caixa = pygame.Rect(250, 500, 300, 40)

    return caixa