import pygame
from src.camera import camera
          
sprites = []
carregado = {} #SPRITES QUE JA FORAM CARREGADOS 

# CRIA UMA CLASSE MODELO PARA PEGAR OS SPRITES
class Sprite:
    def __init__(self, image, x , y, hitbox):
        if image in carregado: #SE O SPRITE ESTIVER CARREGAO ELE APENAS PEGA DO DICIONÁRIO
            self.image = carregado[image]
        else:
            self.image = image
            carregado[image] = self.image
        self.x = x
        self.y = y
        sprites.append(self)
        self.hitbox = hitbox
    
    def delete(self):
        sprites.remove(self)

    def criar_sprites(self, image, x , y, hitbox):
    # CRIA O HITBOX BASEANDO NA IMAGEM DO SPRITE 
    # 2. Criando a estrutura de Hitboxes usando Dicionários
        hitbox = {
            "rect": image.get_rect(topleft=(self.x - camera.x ,self.y - camera.y))
        }
        return hitbox
        


def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""
    
    # 1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade
    sheet = pygame.image.load(local_arquivo).convert()

    # 2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)
    image = pygame.Surface((width, height))
    
    # 3. Copia o pedaço da folha BMP para a nossa nova imagem
    image.blit(sheet, (0, 0), (x, y, width, height))
    
    # 4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
    # Pegamos a cor do pixel no canto superior esquerdo (0,0) do recorte, 
    # assumindo que o fundo do seu sprite começa ali.
    cor_do_fundo = image.get_at((0, 0))
    
    # Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar
    image.set_colorkey(cor_do_fundo)
    
    # 5. Aplica o redimensionamento, se houver
    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))
        
    return image
    
