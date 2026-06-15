import pygame

class Carta:
    def __init__(self, x, y, img_frente, img_verso):

        self.frente_image = pygame.image.load(img_frente).convert_alpha()
        self.verso_image = pygame.image.load(img_verso).convert_alpha()

        self.x = x
        self.y = y

        self.mostra_frente = True

    def desenhar(self, tela):
        if self.mostra_frente:
            tela.blit(self.frente_image, (self.x, self.y))
        else:
            tela.blit(self.verso_image, (self.x, self.y))

    def virar(self):
        self.mostrar_frente = not self.mostrar_frente

