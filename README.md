# Nome do Jogo



Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.
A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Davi Emanuel Moreira Sollar
- Pedro Henrique Silva Oliveira
- Vinícius Marx Galvão
- João Pedro Silva Dantas

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> o jogo se baseia em exploração de plataforma, onde o jogadro e exlpora o mapa e interage com os npcs e eventos que ocorrem durante o jogo, perdendo vida caso interaja com algo nocivo. o jogo termina caso o jogador tenha passado por todos os eventos ou morra mais de 3 vezes.

## Objetivo do jogador

O jogador devera interagir e escolher entre os eventos para que consiga cumprir os desafios estabelecidos, evitando perder nos mesmos

## Regras do jogo

- O jogador se movimenta usando as setas do teclado.
- Cada item coletado aumenta a sua progressão.
- Colidir com um obstáculo reduz a quantidade de chances.
- A partida termina quando o jogador perde todas as chances ou quando o mesmo ganha os desafios.

## Controles

- W: mover para cima
- S: mover para baixo
- A: mover para esquerda
- D: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
