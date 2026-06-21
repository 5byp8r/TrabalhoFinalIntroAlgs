# Dados

Esta pasta guarda arquivos de persistência simples usados pelo jogo.

## Arquivos

- `recorde.txt`: maior pontuação registrada.
- `ranking.txt`: histórico de pontuações salvas no formato `pontuação --- nome`.

## Como é usado

O módulo `src/dados.py` lê e grava estes arquivos. Durante o jogo, `src/jogo.py` carrega o recorde no início, atualiza o recorde quando a pontuação supera o valor salvo e adiciona entradas ao ranking quando um desafio é finalizado.

## Observações

- Os arquivos são texto puro para facilitar leitura e depuração.
- Evite registrar dados pessoais reais dos jogadores.
- Caso um arquivo não exista ou esteja vazio, o código trata o recorde como `0` e o ranking como indisponível.
