import pygame

from src.camera import camera, criar_display


def test_criar_display_configura_camera(monkeypatch):
    display_fake = pygame.Surface((800, 576))
    monkeypatch.setattr(pygame.display, "set_caption", lambda titulo: None)
    monkeypatch.setattr(pygame.display, "set_mode", lambda tamanho: display_fake)

    display = criar_display(576, 800, "Teste")

    assert display is display_fake
    assert camera.width == 800
    assert camera.height == 576
