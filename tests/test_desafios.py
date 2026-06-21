import pygame

from src import entradas
from src.desafios import Carta, caixaTexto


def setup_function():
    pygame.font.init()
    entradas.teclas_clicadas.clear()
    entradas.teclas_pressionadas.clear()


def test_carta_virar_alterna_lado(monkeypatch):
    class ImagemFake:
        def convert_alpha(self):
            return pygame.Surface((10, 10))

    monkeypatch.setattr(pygame.image, "load", lambda caminho: ImagemFake())

    carta = Carta(0, 0, "frente.png", "verso.png")

    assert carta.mostra_frente is True
    carta.virar()
    assert carta.mostra_frente is False
    carta.virar()
    assert carta.mostra_frente is True


def test_caixa_texto_limpar_remove_texto():
    caixa = caixaTexto(0, 0)
    caixa.texto = "abc"

    caixa.limpar()

    assert caixa.texto == ""


def test_caixa_texto_clique_dentro_ativa_caixa():
    caixa = caixaTexto(0, 0, largura=100, altura=40)
    entradas.adicionar_tecla(pygame.MOUSEBUTTONDOWN * 1, (10, 10))

    caixa.atualizar()

    assert caixa.ativo is True


def test_caixa_texto_clique_fora_desativa_caixa():
    caixa = caixaTexto(0, 0, largura=100, altura=40)
    caixa.ativo = True
    entradas.adicionar_tecla(pygame.MOUSEBUTTONDOWN * 1, (200, 200))

    caixa.atualizar()

    assert caixa.ativo is False


def test_caixa_texto_adiciona_caractere_quando_ativa():
    caixa = caixaTexto(0, 0)
    caixa.ativo = True
    entradas.teclas_clicadas[pygame.K_a] = "a"

    caixa.atualizar()

    assert caixa.texto.endswith("a")


def test_caixa_texto_backspace_remove_ultimo_caractere():
    caixa = caixaTexto(0, 0)
    caixa.texto = "abc"
    caixa.ativo = True
    entradas.adicionar_tecla(pygame.K_BACKSPACE)

    caixa.atualizar()

    assert caixa.texto == "ab"

