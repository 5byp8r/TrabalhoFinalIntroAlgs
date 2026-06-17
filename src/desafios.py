import pygame

from src.config import (
    ALTURA_TELA,
    LARGURA_TELA,
    BRANCO,
    CINZA
)

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

        self.texto = ""

        self.x = x
        self.y = y
    
        self.fonte = pygame.font.Font(None, 36)
        self.caixa = pygame.Rect(x, y, largura, altura)
        self.ativo = False

    def atualizar(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.ativo = self.caixa.collidepoint(evento.pos)

        if evento.type == pygame.KEYDOWN and self.ativo:
            if evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            elif evento.key != pygame.K_RETURN:
                self.texto += evento.unicode

    def desenhar(self, tela):
        cor_borda = BRANCO if self.ativo else CINZA
        pygame.draw.rect(tela, cor_borda, self.caixa, 2)
        superficie = self.fonte.render(self.texto, True, BRANCO)
        tela.blit(superficie, (self.caixa.x + 8, self.caixa.y + 8))

    def validar(self, resposta_correta):
        return self.texto.strip().lower() == resposta_correta.strip().lower()

    def limpar(self):
        self.texto = ""