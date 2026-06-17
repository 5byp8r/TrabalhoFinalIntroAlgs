import pygame

from src.config import ALTURA_TELA, LARGURA_TELA

class Carta:
    def __init__(self, x, y, img_frente, img_verso):

        img_frente = pygame.image.load(img_frente).convert_alpha()
        img_verso = pygame.image.load(img_verso).convert_alpha()

        self.frente_image = pygame.transform.scale(img_frente,(LARGURA_TELA,ALTURA_TELA)) 
        self.verso_image = pygame.transform.scale(img_verso,(LARGURA_TELA,ALTURA_TELA)) 
        
        self.x = x
        self.y = y

        self.mostra_frente = True

    def desenhar(self, tela):
        if self.mostra_frente:
            tela.blit(self.frente_image, (self.x, self.y))
        else:
            tela.blit(self.verso_image, (self.x, self.y))

    def virar(self):
        self.mostra_frente = not self.mostra_frente

