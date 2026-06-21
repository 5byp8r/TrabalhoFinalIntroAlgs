# Testes

Esta pasta contem os testes automatizados do projeto, feitos com `pytest`.

Os testes verificam as regras principais do jogo sem depender do loop completo do Pygame. Isso deixa a validacao mais rapida e mais confiavel, porque cada arquivo testa uma parte pequena do sistema.

## Como executar

Para rodar todos os testes:

```bash
python -m pytest
```

Para rodar com saida mais detalhada:

```bash
python -m pytest -v
```

Para rodar apenas um arquivo especifico:

```bash
python -m pytest tests/test_funcoes.py
```

## Resultado atual

Na ultima verificacao, o comando abaixo foi executado:

```bash
python -m pytest
```

Resultado:

```text
66 passed
```

## Arquivos de teste

### `test_logica.py`

Arquivo inicial de testes do projeto.

Cobre:

- colisao basica com borda do mapa;
- soma de pontos com `calcular_pontos`;
- derrota do jogador com `jogador_perdeu`;
- limitacao de valores com `limitar_valor`.

### `test_funcoes.py`

Testa as funcoes auxiliares de regra do jogo em `src/funcoes.py`.

Cobre:

- `calcular_pontos`: soma pontos corretamente;
- `tomar_dano`: reduz a vida atual;
- `jogador_perdeu`: identifica derrota com zero ou menos vidas;
- `limitar_valor`: mantem um valor dentro de um intervalo;
- `verificar_colisao`: detecta colisao entre dois `pygame.Rect`;
- `validar_resposta`: compara resposta inserida com resposta correta;
- `tempo_jogo`: verifica se o tempo limite foi atingido;
- `quantidade_vitimas`: verifica se uma nova vitima deve ser perdida;
- `punicao_tempo_jogo`: reduz pontos como punicao;
- `vitimas_perdidas`: verifica se todas as vitimas foram perdidas;
- `abrir_desafio`: confirma abertura de desafio.

### `test_dados.py`

Testa as funcoes de leitura e escrita de arquivos em `src/dados.py`.

Cobre:

- salvar recorde;
- carregar recorde salvo;
- retornar `0` quando o arquivo de recorde nao existe;
- retornar `0` quando o arquivo de recorde esta vazio;
- salvar ranking no formato esperado;
- carregar ranking existente;
- retornar `False` quando o ranking nao existe;
- retornar `False` quando o ranking esta vazio.

Esses testes usam `tmp_path`, que cria arquivos temporarios sem alterar os arquivos reais da pasta `data/`.

### `test_entradas.py`

Testa o modulo `src/entradas.py`, responsavel por registrar teclas e cliques.

Cobre:

- `adicionar_tecla`: registra tecla pressionada e clicada;
- `deletar_tecla`: remove a tecla das pressionadas;
- `pressionado`: retorna `True` ou `False` corretamente;
- `clicado`: retorna `True` ou `False` corretamente.

### `test_map.py`

Testa a colisao do mapa em `src/map.py`.

Cobre:

- colisao com tile solido;
- ausencia de colisao com tile sem colisao;
- ausencia de colisao quando o jogador esta fora do mapa;
- colisao em diferentes posicoes de borda.

Os testes usam uma classe fake de tile para evitar depender de imagens reais.

### `test_personagem.py`

Testa a classe base `Personagem`, em `src/personagem.py`.

Cobre:

- avanco de animacao apenas depois do contador atingir o limite;
- retorno ao primeiro frame depois do ultimo frame;
- sincronizacao da hitbox com `x` e `y`;
- reset da animacao quando o estado muda.

### `test_jogador.py`

Testa a classe `Jogador`, em `src/jogador.py`.

Cobre:

- movimento para direita;
- movimento para esquerda;
- corrida com `Shift`;
- estado `idle` quando nao ha movimento;
- ataque com `Z` e bloqueio durante ataque;
- retorno a posicao anterior quando ha colisao;
- atualizacao da camera seguindo o jogador.

Os testes usam um `MapaFake`, permitindo testar o jogador sem carregar o mapa completo.

### `test_npc.py`

Testa a classe `NPC`, em `src/npc.py`.

Cobre:

- NPC inicia com indice de dialogo `-1`;
- tecla espaco avanca o dialogo;
- ao passar do ultimo dialogo, o indice vira `-2`;
- dialogo finalizado nao avanca novamente.

### `test_desafios.py`

Testa componentes de desafio em `src/desafios.py`.

Cobre:

- `Carta.virar`: alterna entre frente e verso;
- `caixaTexto.limpar`: limpa o texto;
- clique dentro da caixa ativa o campo;
- clique fora da caixa desativa o campo;
- digitacao adiciona caracteres quando a caixa esta ativa;
- `Backspace` remove o ultimo caractere.

Alguns testes usam `monkeypatch` para substituir carregamento de imagens e evitar depender diretamente dos arquivos graficos.

### `test_botao.py`

Testa a classe `Botao`, em `src/botao.py`.

Cobre:

- clique dentro do botao retorna a acao configurada;
- clique fora do botao retorna `None`.

### `test_camera.py`

Testa `src/camera.py`.

Cobre:

- `criar_display` retorna o display criado;
- largura e altura da camera sao configuradas corretamente.

O teste usa `monkeypatch` para evitar abrir uma janela real durante o `pytest`.

## Tecnicas usadas

- `tmp_path`: cria arquivos temporarios para testar ranking e recorde.
- `monkeypatch`: substitui funcoes do Pygame em testes especificos.
- Classes fake: simulam mapa, tiles e textos sem carregar todos os assets reais.
- `pygame.Surface`: cria imagens simples em memoria para testar animacoes e objetos visuais.

## Boas praticas

- Criar testes para toda regra de pontuacao, vidas, tempo e condicoes de fim de jogo.
- Preferir funcoes pequenas e testaveis no modulo `src/funcoes.py`.
- Evitar testar diretamente o loop principal do Pygame quando a regra puder ser testada isoladamente.
- Usar arquivos temporarios para testar leitura e escrita de dados.
- Usar objetos fake ou `monkeypatch` quando o teste nao precisa carregar imagens reais ou abrir janela.

## Melhorias futuras

- Remover duplicacoes em `src/funcoes.py`.
- Separar mais regras de jogo da parte visual.
- Criar testes de integracao para `Jogo.atualizar` usando mocks/fakes.
- Criar testes adicionais para o menu inicial.
- Rodar `python -m pytest` antes de cada entrega.
