import pygame
from src.entradas import pressionado
from src.sprites import (
    sprites,
    carregado
)
from src.camera import camera

class Player:
    def __init__(self, image, x , y, hitbox):
        if image in carregado: #SE O SPRITE ESTIVER CARREGAO ELE APENAS PEGA DO DICIONÁRIO
            self.image = carregado[image]
        else:
            self.image = image
            carregado[image] = self.image
        self.x = x
        self.y = y
        sprites.append(self)
        self.hitbox = hitbox
        self.velocidade = 5

    def delete(self):
        sprites.remove(self)

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

        camera.x = self.x - camera.width // 2 + self.image.get_width() // 2
        camera.y = self.y - camera.height // 2 + self.image.get_height() // 2
