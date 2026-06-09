import json
import pygame

def pegaJSON(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def desenhar_texto(json, dialogo, indice): 
    if indice >= 0:
        font = pygame.font.Font(None, 64)
        text = font.render(json[dialogo][indice], True, (10, 10, 10))
        textpos = text.get_rect(centerx=800 / 2, y=10)
        return (text, textpos)