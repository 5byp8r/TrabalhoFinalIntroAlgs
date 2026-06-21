# Imagens

Esta pasta contém os recursos visuais carregados pelo Pygame.

## Conteúdo atual

- `botoes/`: fundo e imagem de botão usados no menu inicial.
- `Desafios/`: imagens de frente e verso da carta do desafio.
- `personagem_principal/`: spritesheets de animação do jogador.
- `npc_1/`: spritesheets de animação do NPC atual.
- `Tiles/`: tiles usados para montar o mapa em `src/map.py`.

## Como é usado

- `src/jogo.py` carrega sprites do jogador, NPC, carta de desafio e tiles.
- `src/menu_inicial.py` carrega o fundo do menu.
- `src/personagem.py` recorta spritesheets em frames de animação.

## Referências

- `botoes/`: Elaboração própria
- `Desafios/`: Elaboração própria
- `personagem_principal/`: [Free Gangster Pixel Characters Pack by Free Game Assets (GUI, Sprite, Tilesets)](https://free-game-assets.itch.io/free-gangster-pixel-character-sprite-sheets-pack)
- `npc_1/`: [City Man Pixel Art Character Sprite Sheets](https://craftpix.net/freebies/city-man-pixel-art-character-sprite-sheets/)
- `Tiles/`: [The Japan Collection: Japanese City (Free Version) by GuttyKreum](https://guttykreum.itch.io/free-japanese-city-game-assets)

## Observações

- Os spritesheets de personagens são recortados com largura padrão de `128` pixels por frame.
- Os tiles são desenhados com tamanho configurado em `src/config.py`.
- Mantenha a organização por pasta para evitar caminhos quebrados no código.
