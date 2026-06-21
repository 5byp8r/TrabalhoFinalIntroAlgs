import pygame

from src.funcoes import (
    abrir_desafio,
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    punicao_tempo_jogo,
    quantidade_vitimas,
    tempo_jogo,
    tomar_dano,
    validar_resposta,
    verificar_colisao,
    vitimas_perdidas,
)


def test_calcular_pontos_soma_pontos():
    assert calcular_pontos(10, 5) == 15


def test_tomar_dano_reduz_vida():
    assert tomar_dano(100, 25) == 75


def test_jogador_perdeu_com_zero_vidas():
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vida_negativa():
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas_restantes():
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50


def test_verificar_colisao_quando_retangulos_se_sobrepoem():
    rect_1 = pygame.Rect(0, 0, 20, 20)
    rect_2 = pygame.Rect(10, 10, 20, 20)

    assert verificar_colisao(rect_1, rect_2) is True


def test_verificar_colisao_quando_retangulos_nao_se_sobrepoem():
    rect_1 = pygame.Rect(0, 0, 20, 20)
    rect_2 = pygame.Rect(30, 30, 20, 20)

    assert verificar_colisao(rect_1, rect_2) is False


def test_validar_resposta_correta():
    assert validar_resposta("teste", "teste") is True


def test_validar_resposta_errada():
    assert validar_resposta("outra", "teste") is False


def test_tempo_jogo_retorna_true_quando_passou_do_limite():
    assert tempo_jogo(30 * 60 * 1000, minutos=30) is True


def test_tempo_jogo_retorna_false_antes_do_limite():
    assert tempo_jogo((30 * 60 * 1000) - 1, minutos=30) is False


def test_quantidade_vitimas_retorna_true_quando_deve_perder_vitima():
    assert quantidade_vitimas(5 * 60 * 1000, 0, minutos=5) is True


def test_quantidade_vitimas_retorna_false_quando_ja_contabilizou_a_vitima():
    assert quantidade_vitimas(5 * 60 * 1000, 1, minutos=5) is False


def test_punicao_tempo_jogo_remove_pontos():
    assert punicao_tempo_jogo(100, 30) == 70


def test_vitimas_perdidas_com_zero_vitimas():
    assert vitimas_perdidas(0) is True


def test_vitimas_perdidas_com_vitimas_vivas():
    assert vitimas_perdidas(2) is False


def test_abrir_desafio_retorna_true():
    assert abrir_desafio(False) is True
