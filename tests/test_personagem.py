import pygame

from src.personagem import Personagem


def criar_animacoes():
    return {
        "idle": [pygame.Surface((128, 128)), pygame.Surface((128, 128))],
        "walk": [pygame.Surface((128, 128)), pygame.Surface((128, 128))],
    }


def criar_personagem():
    return Personagem(
        x=10,
        y=20,
        largura=32,
        altura=64,
        velocidade=4,
        velocidade_corrida=8,
        estado="idle",
        animacoes=criar_animacoes(),
        velocidade_animacao={"idle": 2, "walk": 2},
    )


def test_avancar_animacao_so_troca_frame_apos_limite():
    personagem = criar_personagem()

    personagem.avancar_animacao()
    assert personagem.frame_atual == 0

    personagem.avancar_animacao()
    assert personagem.frame_atual == 1


def test_avancar_animacao_volta_para_primeiro_frame():
    personagem = criar_personagem()
    personagem.frame_atual = 1
    personagem.contador = 1

    personagem.avancar_animacao()

    assert personagem.frame_atual == 0


def test_atualizar_sincroniza_hitbox_com_posicao():
    personagem = criar_personagem()
    personagem.x = 50
    personagem.y = 60

    personagem.atualizar()

    assert personagem.hitbox["rect"].x == 50 + personagem.diferenca_hitbox_x
    assert personagem.hitbox["rect"].y == 60 + personagem.diferenca_hitbox_y


def test_atualizar_reseta_animacao_quando_estado_muda():
    personagem = criar_personagem()
    personagem.estado_anterior = "idle"
    personagem.estado = "walk"
    personagem.frame_atual = 1
    personagem.contador = 1

    personagem.atualizar()

    assert personagem.frame_atual == 0
    assert personagem.contador == 1
