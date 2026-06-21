import pygame

from src import entradas
from src.npc import NPC


class TextoFake:
    def __init__(self):
        self._textos = {"john_pista": ["oi", "pista"]}


def setup_function():
    entradas.teclas_clicadas.clear()
    entradas.teclas_pressionadas.clear()


def criar_animacoes():
    frame = pygame.Surface((128, 128))
    return {"idle": [frame, frame]}


def criar_npc():
    return NPC(
        nome="john",
        x=0,
        y=0,
        largura=50,
        altura=100,
        velocidade=0,
        velocidade_corrida=0,
        estado="idle",
        animacoes=criar_animacoes(),
        velocidade_animacao={"idle": 10},
    )


def test_npc_comeca_sem_dialogo():
    npc = criar_npc()

    assert npc.indice_dialogo == -1


def test_npc_avanca_dialogo_ao_clicar_espaco():
    npc = criar_npc()
    entradas.adicionar_tecla(pygame.K_SPACE)

    npc.atualizar_dialogos(TextoFake())

    assert npc.indice_dialogo == 0


def test_npc_marca_dialogo_finalizado_quando_passa_do_ultimo():
    npc = criar_npc()
    npc.indice_dialogo = 1
    entradas.adicionar_tecla(pygame.K_SPACE)

    npc.atualizar_dialogos(TextoFake())

    assert npc.indice_dialogo == -2


def test_npc_nao_avanca_quando_dialogo_ja_finalizou():
    npc = criar_npc()
    npc.indice_dialogo = -2
    entradas.adicionar_tecla(pygame.K_SPACE)

    npc.atualizar_dialogos(TextoFake())

    assert npc.indice_dialogo == -2
