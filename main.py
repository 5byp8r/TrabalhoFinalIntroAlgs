from src.jogo import executar_jogo


if __name__ == "__main__":
    # Ponto de entrada da aplicação.
    executar_jogo()
# 
# ## 
#        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
#         jogador..hitbox["rect"].x = limitar_valor(jogador.hitbox["rect"].x, 0, LARGURA_TELA - jogador.hitbox["rect"].width)
#         jogador.hitbox["rect"].y = limitar_valor(jogador.hitbox["rect"].y, 0, ALTURA_TELA - jogador.hitbox["rect"].height)

#         # Verificação de colisão com a Gema (antigo 'item')
#         if verificar_colisao(jogador.hitbox["rect"], gema.hitbox["rect"]):
#             pontos = calcular_pontos(pontos, 10)

#             # Move a gema de lugar ao coletar
#             gema.hitbox["rect"].x += 80
#             gema.hitbox["rect"].y += 50

#             # Se a gema sair da tela, volta para uma posição segura
#             if gema.hitbox["rect"].x > LARGURA_TELA - gema.hitbox["rect"].width:
#                 gema.hitbox["rect"].x = 50
#             if gema.hitbox["rect"].y > ALTURA_TELA - gema.hitbox["rect"].height:
#                 gema.hitbox["rect"].y = 50

#         # Verificação de colisão com o Inimigo
#         if verificar_colisao(jogador.hitbox["rect"], inimigo.hitbox["rect"]):
#             vidas = tomar_dano(vidas, 1)

#             # Afasta o inimigo ao colidir
#             inimigo.hitbox["rect"].x += 80
#             inimigo.hitbox["rect"].y += 50

#             if inimigo.hitbox["rect"].x > LARGURA_TELA - inimigo.hitbox["rect"].width:
#                 inimigo.hitbox["rect"].x = 50
#             if inimigo.hitbox["rect"].y > ALTURA_TELA - inimigo.hitbox["rect"].height:
#                 inimigo.hitbox["rect"].y = 50

#         # Regras de fim de jogo e recorde
#         if jogador_perdeu(vidas):
#             rodando = False

#         if pontos > recorde:
#             recorde = pontos
#             salvar_recorde(CAMINHO_RECORDE, recorde)

#         pygame.display.set_caption(
#             f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
#         )
        
#     pontos = 0
#     vidas = 3
#     recorde = carregar_recorde(CAMINHO_RECORDE)
##############################################################
# import pygame
# from src.personagem import Personagem  # importa a classe do personagem

# pygame.init()
# tela = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# # cria o personagem no centro da tela
# personagem = Personagem(300, 300)

# rodando = True
# while rodando:
#     clock.tick(60)  # limita a 60 fps

#     # verifica se o jogador fechou a janela
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False

#     personagem.atualizar()  # processa movimento e animação

#     tela.fill((50, 50, 50))       # limpa a tela
#     personagem.desenhar(tela)     # desenha o personagem
#     pygame.display.flip()         # atualiza a tela

# pygame.quit()