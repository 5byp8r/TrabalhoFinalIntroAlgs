
teclas_clicadas = dict()
teclas_pressionadas = dict()

def adicionar_tecla(tecla, adicional = None):
    teclas_pressionadas[tecla] = adicional
    teclas_clicadas[tecla] = adicional

def deletar_tecla(tecla):
    del teclas_pressionadas[tecla]

def pressionado(tecla):
    return tecla in teclas_pressionadas.keys()

def clicado(tecla):
    return tecla in teclas_clicadas.keys()