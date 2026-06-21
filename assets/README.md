# Assets

Esta pasta centraliza os recursos usados pelo jogo.

## Organização

- `imagens/`: sprites do jogador e NPC, tiles do mapa, telas de desafio e imagens do menu.
- `textos/`: diálogos e textos carregados pelo jogo.
- `fontes/`: pasta reservada para fontes customizadas.

## Uso atual

O jogo carrega imagens diretamente a partir de caminhos em `src/jogo.py`, `src/menu_inicial.py` e `src/map.py`. Os diálogos do NPC atual são lidos de `assets/textos/npc.json` pela classe `Texto`.

## Boas práticas

- Usar nomes descritivos e sem espaços.
- Manter os assets separados por tipo e personagem.
- Registrar a origem de recursos externos quando forem adicionados.
