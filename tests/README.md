# Testes

Esta pasta contém testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida funções puras de `src/funcoes.py`, incluindo soma de pontos, condição de derrota por vidas e limitação de valores.

## Como executar

```bash
python -m pytest
```

## Escopo atual

Os testes atuais cobrem apenas regras isoladas que não dependem de Pygame aberto. Funcionalidades visuais, loop principal, colisões reais no mapa, diálogos e desafios ainda não possuem testes automatizados.

## Próximos testes úteis

- Validação de respostas dos desafios.
- Punição por tempo de enigma.
- Punição por tempo total de jogo.
- Leitura e escrita de recorde/ranking em arquivos temporários.
