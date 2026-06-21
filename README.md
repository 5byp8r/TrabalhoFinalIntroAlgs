# Drecut: Fragmentos da Verdade

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.
A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Davi Emanuel Moreira Sollar
- João Pedro Silva Dantas
- Pedro Henrique Silva Oliveira
- Vinícius Marx Galvão

## Objetivo do jogo

O jogador deve explorar o mapa, interagir com NPCs e resolver desafios para juntar informações da investigação. A partida termina quando o tempo se esgota, quando todas as vítimas são perdidas ou quando os enigmas disponíveis são encerrados.

## Estado atual

A versão atual possui:

- Menu inicial com botões para iniciar ou sair.
- Mapa em tiles com colisão nas bordas.
- Jogador animado, movimentação por teclado e câmera acompanhando o personagem.
- NPC animado com diálogo carregado de arquivo JSON.
- Tela de desafio com carta, campo de resposta e validação simples.
- Contadores de tempo total e tempo por enigma.
- Controle de vítimas vivas, recorde e ranking em arquivos de texto.
- Testes unitários para funções puras de lógica.

## Controles

- `W` ou `↑` (seta para cima): mover para cima.
- `S` ou `↓` (seta para baixo): mover para baixo.
- `A` ou `←` (seta para esquerda): mover para esquerda.
- `D` ou `→` (seta para direita): mover para direita.
- `Shift esquerdo`: correr.
- `Espaço`: avançar diálogos/interagir.
- `Enter`: confirmar nome ou resposta.
- `Mouse`: clicar nos botões, ativar campos de texto e virar a carta do desafio.
- `Esc`: fechar a tela de desafio quando ela estiver aberta.

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `requirements.txt`: dependências do projeto (`pygame-ce` e `pytest`).
- `src/`: código-fonte principal do jogo.
- `assets/`: imagens, textos, sons e fontes.
- `data/`: arquivos simples de persistência, como ranking e recorde.
- `docs/`: proposta e documentação de planejamento.
- `tests/`: testes automatizados.

## Como executar o jogo

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

## Observações

- A proposta original está em `docs/proposta.MD`.
- Os diálogos do NPC atual ficam em `assets/textos/npc.json`.
- O desafio implementado valida a resposta textual `teste`.
- O ranking e o recorde são salvos em `data/ranking.txt` e `data/recorde.txt`.
