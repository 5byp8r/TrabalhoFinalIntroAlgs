# Textos

Esta pasta guarda textos carregados pelo jogo.

## Arquivos

- `npc.json`: diálogos do NPC `john`, usados durante a interação com o jogador.

## Formato

Os textos são organizados em JSON. Cada chave representa um bloco de diálogo, e o valor é uma lista de falas exibidas em sequência.

Exemplo:

```json
{
  "john_pista": [
    "Boa noite, detetive.",
    "Qual o seu nome?"
  ]
}
```

## Como é usado

A classe `Texto`, em `src/texto.py`, carrega o JSON e desenha a fala correspondente ao índice controlado pelo NPC em `src/npc.py`.
