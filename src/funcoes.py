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


def validar_resposta(resposta_inserida, resposta_correta):
    return resposta_inserida == resposta_correta


#Sistema de recompensa e punição fucnionará por tempo

def tempo_jogo(ticks_atual, minutos=30):
    """Essa função se refere ao tempo de 30 minutos para solucionar o objetivo final"""
    limite_ms = minutos * 60 * 1000
    return ticks_atual >= limite_ms
 
def quantidade_vitimas(ticks_atual, vitimas_perdidas_quantidade, minutos=5):
    """Essa função se refere a quantidade de vitimas perdidas a cada 5 Minutos. Se o jogador perder 5 minutos, uma vítima morre"""
    limite_ms = minutos * 60 * 1000
    vitimas = ticks_atual // limite_ms
    return vitimas > vitimas_perdidas_quantidade

def punicao_tempo_jogo(pontos_atual, punicao_pontos):
    """Essa função se refere à punição por tempo perdido"""
    return pontos_atual - punicao_pontos

def vitimas_perdidas(vitimas_vivas):
    """Essa função indica se todas as vítimas morreram"""
    return vitimas_vivas <= 0

def abrir_desafio(desafio_aberto):
    return True

def validar_resposta(resposta_inserida, resposta_correta):
    return resposta_inserida == resposta_correta
