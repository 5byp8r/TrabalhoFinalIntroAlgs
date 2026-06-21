import pygame
from src.botao import Botao
from src.config import BRANCO, PRETO

class MenuInicial:
    #Instancia variáveis do menu inicial
    def __init__(self, display, largura_display, altura_display):
        self.display = display
        self.largura_display = largura_display
        self.altura_display = altura_display

        self.background = pygame.image.load("assets/imagens/botoes/background.png")
        self.background = pygame.transform.scale(self.background, (largura_display, altura_display))

        self.fonte_titulo = pygame.font.SysFont(None, 72)
        self.fonte_botao = pygame.font.SysFont(None, 36)

        self.titulo = self.fonte_titulo.render("DRECUT", True, BRANCO)
        self.sombra = self.fonte_titulo.render("DRECUT", True, PRETO)

        # sem vírgula no final -> objetos Button, não tuplas
        self.btn_iniciar = Botao("Iniciar Jogo", 320, "Jogar", largura_display)
        self.btn_sair = Botao("Sair do jogo", 420, "Sair", largura_display)
        self.botoes = [self.btn_iniciar, self.btn_sair]

    #Atualiza o estado dos botões do menu inicial
    def atualizar(self):
        if self.btn_iniciar.clicado() == "Jogar":
            # Chama a função para trocar de tela e retorna falso

            # Import dentro da função para não dar erro de referência cruzada
            from src.executar_jogo import setTela
            from src.jogo import Jogo
            
            setTela(Jogo(self.display))
            return False

        if self.btn_sair.clicado() == "Sair":
            # Chama a função para encerrar o jogo e retorna falso

            # Import dentro da função para não dar erro de referência cruzada
            from src.executar_jogo import exitGame

            exitGame()
            return False

        #Retorna verdadeiro para desenhar a tela
        return True

    #Desenha os itens do menu inicial
    def desenhar(self):
        """Desenha o menu e retorna a ação do botão clicado neste frame,
        ou None se nenhum botão foi clicado."""

        self.display.blit(self.background, (0, 0))
        self.display.blit(
            self.sombra,
            (self.largura_display // 2 - self.titulo.get_width() // 2 + 3, 103)
        )
        self.display.blit(
            self.titulo,
            (self.largura_display // 2 - self.titulo.get_width() // 2, 100)
        )

        for btn in self.botoes:
            btn.desenhar(self.display, self.fonte_botao)

        pygame.display.flip()
