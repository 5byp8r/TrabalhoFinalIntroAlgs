def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))

def salvar_ranking(caminho_arquivo, nome, pontuacao):
    """Faz o ranqueamento da pontuação do jogador"""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f'{str(pontuacao)} --- {str(nome)} \n')

def carregar_ranking(caminho_arquivo):
    """Carrega o ranqueamento da pontuação dos jogadores"""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return False

        return conteudo

    except FileNotFoundError:
        return False

def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0