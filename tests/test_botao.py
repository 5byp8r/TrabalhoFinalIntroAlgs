import pygame

from src import entradas
from src.botao import Botao


def setup_function():
    entradas.teclas_clicadas.clear()
    entradas.teclas_pressionadas.clear()


def test_botao_clicado_retorna_acao_quando_clique_esta_dentro():
    botao = Botao("Jogar", 100, "acao_jogar", 800)
    entradas.adicionar_tecla(pygame.MOUSEBUTTONDOWN * 1, botao.rect.center)

    assert botao.clicado() == "acao_jogar"


def test_botao_clicado_retorna_none_quando_clique_esta_fora():
    botao = Botao("Jogar", 100, "acao_jogar", 800)
    entradas.adicionar_tecla(pygame.MOUSEBUTTONDOWN * 1, (0, 0))

    assert botao.clicado() is None
