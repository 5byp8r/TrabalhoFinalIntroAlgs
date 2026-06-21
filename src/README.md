# Código-fonte (`src`)

Esta pasta contém os módulos Python que implementam o jogo em Pygame.

## Módulos principais

- `executar_jogo.py`: inicializa o Pygame, cria a tela, processa eventos e troca entre menu e jogo.
- `jogo.py`: concentra o estado da partida, atualização, desenho, timers, NPC, desafio, vítimas, ranking e recorde.
- `menu_inicial.py`: implementa a tela inicial com botões de jogar e sair.
- `config.py`: reúne constantes de tela, FPS, cores, tamanho de tiles e caminhos de arquivos.
- `map.py`: define os tipos de tile, o mapa atual e a lógica de colisão com tiles.
- `camera.py`: cria o display e mantém a posição da câmera usada no desenho do mapa e personagens.

## Personagens e interface

- `personagem.py`: classe base de personagens animados e função para recortar frames de spritesheets.
- `jogador.py`: especializa o personagem principal com movimento, corrida, ataques, colisão e câmera.
- `npc.py`: especializa personagens NPC com nome, índice de diálogo e avanço de falas.
- `botao.py`: botão reutilizável do menu inicial.
- `desafios.py`: carta do desafio e caixa de texto interativa para nome/resposta.
- `texto.py`: carregamento e desenho de textos a partir de JSON.
- `entradas.py`: estado compartilhado de teclas e cliques por frame.

## Regras e dados

- `funcoes.py`: funções puras de pontuação, dano, limites, colisão, validação de respostas, timers e punições.
- `dados.py`: leitura e escrita de recorde e ranking em arquivos de texto.

## Fluxo atual

`main.py` chama `executar_jogo()`, que abre o `MenuInicial`. Ao clicar em "Jogar", a tela atual passa a ser `Jogo`. A classe `Jogo` carrega mapa, jogador, NPC, diálogos, desafio e dados persistentes, então atualiza e desenha a cena a cada frame.
