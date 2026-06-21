import pygame

from src import entradas
from src.camera import camera
from src.jogador import Jogador


class MapaFake:
    def __init__(self, colide=False):
        self.colide = colide

    def tem_colisao(self, rect_jogador):
        return self.colide


def setup_function():
    entradas.teclas_clicadas.clear()
    entradas.teclas_pressionadas.clear()
    camera.x = 0
    camera.y = 0
    camera.width = 800
    camera.height = 576


def criar_animacoes():
    frame = pygame.Surface((128, 128))
    return {
        "idle": [frame, frame],
        "walk": [frame, frame],
        "run": [frame, frame],
        "attack1": [frame, frame],
        "attack2": [frame, frame],
        "attack3": [frame, frame],
        "dead": [frame, frame],
    }


def criar_jogador():
    return Jogador(
        x=100,
        y=100,
        largura=32,
        altura=64,
        velocidade=4,
        velocidade_corrida=10,
        estado="idle",
        animacoes=criar_animacoes(),
        velocidade_animacao={
            "idle": 10,
            "walk": 10,
            "run": 10,
            "attack1": 10,
            "attack2": 10,
            "attack3": 10,
            "dead": 10,
        },
    )


def test_jogador_move_para_direita():
    jogador = criar_jogador()
    entradas.adicionar_tecla(pygame.K_RIGHT)

    jogador.atualizar(MapaFake())

    assert jogador.x == 104
    assert jogador.estado == "walk"
    assert jogador.olhando_direita is True


def test_jogador_move_para_esquerda():
    jogador = criar_jogador()
    entradas.adicionar_tecla(pygame.K_LEFT)

    jogador.atualizar(MapaFake())

    assert jogador.x == 96
    assert jogador.estado == "walk"
    assert jogador.olhando_direita is False


def test_jogador_corre_com_shift():
    jogador = criar_jogador()
    entradas.adicionar_tecla(pygame.K_LSHIFT)
    entradas.adicionar_tecla(pygame.K_RIGHT)

    jogador.atualizar(MapaFake())

    assert jogador.x == 110
    assert jogador.estado == "run"


def test_jogador_parado_fica_idle():
    jogador = criar_jogador()

    jogador.atualizar(MapaFake())

    assert jogador.estado == "idle"


def test_jogador_ataca_com_z_e_fica_bloqueado():
    jogador = criar_jogador()
    entradas.adicionar_tecla(pygame.K_z)

    jogador.atualizar(MapaFake())

    assert jogador.estado == "attack1"
    assert jogador.bloqueado is True


def test_jogador_volta_posicao_quando_colide():
    jogador = criar_jogador()
    entradas.adicionar_tecla(pygame.K_RIGHT)

    jogador.atualizar(MapaFake(colide=True))

    assert jogador.x == 100
    assert jogador.y == 100


def test_camera_segue_jogador():
    jogador = criar_jogador()

    jogador.atualizar(MapaFake())

    assert camera.x == jogador.x - camera.width // 2 + 64
    assert camera.y == jogador.y - camera.height // 2 + 64
