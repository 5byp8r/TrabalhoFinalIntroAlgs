import pygame
from src.teclas import pressionado
from src.sprites import Sprite

class Player(Sprite):
    def __init__(self, image, x, y, hitbox):
        super().__init__(image, x, y, hitbox)
        self.velocidade = 5

    def update(self):
        
        #COMANDOS WASD
        if pressionado(pygame.K_a):
            self.x -= self.velocidade
        if pressionado(pygame.K_d):
            self.x += self.velocidade
        if pressionado(pygame.K_w):
            self.y -= self.velocidade
        if pressionado(pygame.K_s):
            self.y += self.velocidade

        #ATUALIZAR O HITBOX
        self.hitbox["rect"].topleft = (self.x, self.y)
