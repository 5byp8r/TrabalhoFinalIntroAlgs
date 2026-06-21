import pygame

from src.map import Map


class TipoTileFake:
    def __init__(self, colisao):
        self.colisao = colisao
        self.image = pygame.Surface((32, 32))


def criar_mapa_teste():
    tipos_tile = [
        TipoTileFake(True),
        TipoTileFake(False),
    ]
    tiles = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    return Map(tiles, tipos_tile, 32)


def test_tem_colisao_com_tile_solido():
    mapa = criar_mapa_teste()
    jogador = pygame.Rect(0, 0, 32, 32)

    assert mapa.tem_colisao(jogador) is True


def test_nao_tem_colisao_com_tile_sem_colisao():
    mapa = criar_mapa_teste()
    jogador = pygame.Rect(32, 32, 32, 32)

    assert mapa.tem_colisao(jogador) is False


def test_nao_tem_colisao_fora_do_mapa():
    mapa = criar_mapa_teste()
    jogador = pygame.Rect(200, 200, 32, 32)

    assert mapa.tem_colisao(jogador) is False


def test_tem_colisao_quando_retangulo_encosta_em_borda():
    mapa = criar_mapa_teste()
    jogador = pygame.Rect(64, 0, 32, 32)

    assert mapa.tem_colisao(jogador) is True
