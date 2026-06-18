import pygame

from src import entradas
from src.config import (
    ALTURA_TELA,
    LARGURA_TELA,
    BRANCO,
    CINZA,
    PRETO
)
from src.entradas import clicado

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





class caixaResposta:
    def __init__(self, x, y, largura=300, altura=40):

        self.texto = "decifre"
        self.final = ""

        self.x = x
        self.y = y
    
        self.fonte = pygame.font.Font(None, 36)
        self.caixa = pygame.Rect(x, y, largura, altura)
        self.ativo = False

    def atualizar(self):
        if clicado(pygame.MOUSEBUTTONDOWN * 1):
            self.ativo = self.caixa.collidepoint(entradas.teclas_clicadas[pygame.MOUSEBUTTONDOWN * 1])

        if self.ativo:
            if clicado(pygame.K_BACKSPACE):
                self.texto = self.texto[:-1]
            elif not clicado(pygame.K_RETURN):
                for string in entradas.teclas_clicadas.values():
                    if isinstance(string, str): self.texto += string

    def desenhar(self, tela, delay = 0):
        surface_fundo = pygame.Surface((self.caixa.width, self.caixa.height))
        surface_fundo.set_alpha(180)        
        surface_fundo.fill(BRANCO)
        tela.blit(surface_fundo, (self.caixa.x, self.caixa.y))

        if delay >= 500:
            self.final = "|" if self.final == "" and self.ativo else ""
            delay = 0

        cor_borda = BRANCO if self.ativo else CINZA
        pygame.draw.rect(tela, cor_borda, self.caixa, 2)  # borda

        superficie = self.fonte.render(self.texto + self.final, True, PRETO)
        tela.blit(superficie, (self.caixa.x + 8, self.caixa.y + 8))

        return delay

    def limpar(self):
        self.texto = ""
