
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


#Sistema de recompensa e punição fucnionará por tempo

def tempo_jogo(frame_atual, fps, minutos=30):
    """Essa função se refere ao tempo de 30 minutos para solucionar o objetivo final"""
    tempo_limite = fps * 60 * minutos
    return frame_atual >= tempo_limite
 
def tempo_por_enigma(frame_enigma, fps, minutos=5):
    """Essa função se refere ao tempo maximo de cada enigma. 5 Minutos. Se o jogador perder 5 minutos, uma vítima morre"""
    tempo_limite = fps * 60 * minutos 
    return frame_enigma >= tempo_limite

def punicao_tempo_jogo(pontos_atual, punicao_pontos):
    """Essa função se refere à punição por tempo perdido"""
    return pontos_atual - punicao_pontos

def punicao_tempo_enigma(vidas_atual):
    """Essa função se refere à punição por tempo perdido em cada função, acarretando na morte de uma mítima a cada enigma perdido"""
    return vidas_atual - 1

def vitimas_perdidas(vitimas_vivas):
    """Essa função indica se todas as vítimas morreram"""
    return vitimas_vivas <= 0

def abrir_desafio(desafio_aberto):
    return True