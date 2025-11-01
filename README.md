# Jogo de Batalha (Turn-based)

Descrição

Este é um pequeno jogo de batalha por turnos implementado em Python. O objetivo do projeto é demonstrar conceitos de programação orientada a objetos (OOP), design simples de entidades de jogo (personagens, herói, inimigo) e a lógica de combate em turnos que pode ser usada em um portfólio para mostrar habilidades de implementação, organização de código e extensibilidade.

Destaques para o portfólio

- Código claro e conciso em Python, organizado em classes.
- Uso de encapsulamento e herança: classes `Character`, `Hero` e `Enemy`.
- Mecânica de combate por turnos com ataque normal e ataque especial.
- Fácil de estender: adicionar novos inimigos, habilidades ou itens é direto.
- Ideal para demonstrar habilidades em design de sistemas simples e em testes manuais.

Tecnologias e dependências

- Linguagem: Python (recomendado 3.8+).
- Dependências: somente a biblioteca padrão (`random`). Não há dependências externas.

Arquivos

- `game.py` — arquivo principal que contém toda a lógica do jogo e a execução.

Design do código (visão geral)

- `Character` — classe base que encapsula nome, vida e nível e fornece métodos para ataque, receber dano e exibir detalhes.
- `Hero` — herança de `Character`, adiciona uma habilidade especial (`special_attack`) e detalhe extra.
- `Enemy` — herança de `Character`, adiciona um tipo/elemento do inimigo.
- `Game` — orquestrador que instancia herói e inimigo e gerencia a batalha por turnos.

Interação esperada

- O jogo mostra os detalhes dos personagens a cada turno.
- O jogador pressiona Enter para continuar e escolhe entre atacar normalmente (1) ou usar ataque especial (2).
- O inimigo atacará de volta enquanto tiver vida.

Exemplo rápido

1. Executar `python game.py`.
2. Pressione Enter quando solicitado para iniciar um ataque.
3. Digite `1` para um ataque normal ou `2` para ataque especial.
4. Repita até que um dos personagens perca toda a vida.

Possíveis melhorias (próximos passos)

- Separar o código em módulos (ex.: `entities.py`, `game.py`) para facilitar testes e manutenção.
- Adicionar um sistema de itens e cura.
- Implementar diferentes tipos de inimigos com comportamentos únicos.
- Adicionar persistência de progresso (salvar/ carregar) e menu inicial.
- Criar testes automatizados (unittest/pytest) para as regras de combate.

Como executar

Abra um terminal (bash no Windows funciona bem) na pasta do projeto e execute:

```bash
python game.py
```
