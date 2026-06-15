def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

def recompensa_pista(pontos_atual, pontos_pista):
    """Essa função da ao jogador pontos por coletar pistas espalhadas pelo mapa."""
    return pontos_atual + pontos_pista

def recompensa_objetivo(pontos_atual, pontos_objetivo):
    """Essa função dá ao jogador pontos após concluir objetivos."""
    return pontos_atual + pontos_objetivo

def punicao_erro(pontos_atual, punicao_ponto):
    """Essa função pune o jogador por erros ao tentarem completar o objetivo."""
    return pontos_atual - punicao_ponto

def punicao_tempo(pontos_atual, punicao_tempo):
    """Essa função pune o jogador por tempo esgotado."""
    return pontos_atual - punicao_tempo

def abrir_desafio(desafio_aberto):
    return True