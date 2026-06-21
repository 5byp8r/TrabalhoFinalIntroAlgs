from src import entradas


def setup_function():
    entradas.teclas_clicadas.clear()
    entradas.teclas_pressionadas.clear()


def test_adicionar_tecla_marca_como_pressionada_e_clicada():
    entradas.adicionar_tecla(10, "a")

    assert entradas.pressionado(10) is True
    assert entradas.clicado(10) is True
    assert entradas.teclas_pressionadas[10] == "a"
    assert entradas.teclas_clicadas[10] == "a"


def test_deletar_tecla_remove_apenas_das_pressionadas():
    entradas.adicionar_tecla(10, "a")
    entradas.deletar_tecla(10)

    assert entradas.pressionado(10) is False
    assert entradas.clicado(10) is True


def test_pressionado_retorna_false_para_tecla_nao_registrada():
    assert entradas.pressionado(999) is False


def test_clicado_retorna_false_para_tecla_nao_registrada():
    assert entradas.clicado(999) is False
