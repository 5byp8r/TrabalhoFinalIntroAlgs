from src.dados import (
    carregar_ranking,
    carregar_recorde,
    salvar_ranking,
    salvar_recorde,
)


def test_salvar_e_carregar_recorde(tmp_path):
    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 150)

    assert caminho.read_text(encoding="utf-8") == "150"
    assert carregar_recorde(caminho) == 150


def test_carregar_recorde_inexistente_retorna_zero(tmp_path):
    caminho = tmp_path / "nao_existe.txt"

    assert carregar_recorde(caminho) == 0


def test_carregar_recorde_vazio_retorna_zero(tmp_path):
    caminho = tmp_path / "recorde.txt"
    caminho.write_text("", encoding="utf-8")

    assert carregar_recorde(caminho) == 0


def test_salvar_ranking_adiciona_linha(tmp_path):
    caminho = tmp_path / "ranking.txt"

    salvar_ranking(caminho, "Pedro", 200)

    assert caminho.read_text(encoding="utf-8") == "200 --- Pedro \n"


def test_carregar_ranking_retorna_conteudo(tmp_path):
    caminho = tmp_path / "ranking.txt"
    caminho.write_text("200 --- Pedro \n100 --- Ana \n", encoding="utf-8")

    assert carregar_ranking(caminho) == "200 --- Pedro \n100 --- Ana"


def test_carregar_ranking_inexistente_retorna_false(tmp_path):
    caminho = tmp_path / "nao_existe.txt"

    assert carregar_ranking(caminho) is False


def test_carregar_ranking_vazio_retorna_false(tmp_path):
    caminho = tmp_path / "ranking.txt"
    caminho.write_text("", encoding="utf-8")

    assert carregar_ranking(caminho) is False
