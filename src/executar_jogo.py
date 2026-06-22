import pygame

from src import entradas
from src.camera import criar_display
from src.config import ALTURA_DISPLAY, LARGURA_DISPLAY, TITULO_JOGO
from src.menu_inicial import MenuInicial
from src.tela_final import tela_derrota, tela_vitoria

#Variáveis globais para manipulação entre as funções
tela_atual = None
rodando = True

# Executa o loop principal do jogo e controla estado, colisões e pontuação.
def executar_jogo():
    pygame.init()

    # Força o uso das variáveis globais
    global tela_atual
    global rodando

    display = criar_display(ALTURA_DISPLAY, LARGURA_DISPLAY, TITULO_JOGO)
    tela_atual = MenuInicial(display, LARGURA_DISPLAY, ALTURA_DISPLAY)


    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        # Limpa as teclas clicadas por tick
        entradas.teclas_clicadas.clear()

        # Armazena as teclas clicadas e seu complementar
        # Teclado: constante da tecla e string do caracter clicado
        # Mouse: constante do evento do mouse vezes valor do botão clicado e posição do cursor
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                entradas.adicionar_tecla(evento.key, evento.unicode)
            if evento.type == pygame.KEYUP:
                entradas.deletar_tecla(evento.key)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                entradas.adicionar_tecla(evento.type * evento.button, evento.pos)
            if evento.type == pygame.MOUSEBUTTONUP:
                entradas.deletar_tecla((evento.type - 1) * evento.button)

        # Desenha a tela se o jogo não for fechado ou a tela não for alterada
        if tela_atual.atualizar():
            tela_atual.desenhar()

    pygame.quit()

# Atualiza a tela atual
def setTela(nova_tela):
    global tela_atual
    tela_atual = nova_tela

# Para o loop principal do jogo
def exitGame():
    global rodando
    rodando = False