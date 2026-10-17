# TaskTracker

Sistema de linha de comando para cadastrar e visualizar tarefas, com validação de título e prioridade.

## Descrição

O TaskTracker concentra o controle de tarefas em um único lugar. Pelo terminal, o usuário cadastra o que precisa fazer e consulta a lista enquanto o programa está aberto.

Cada tarefa guarda:

- **Título** — obrigatório; entrada vazia ou só com espaços é recusada
- **Descrição** — detalhamento livre, pode ficar em branco
- **Prioridade** — somente `Alta`, `Média` (ou `Media`) e `Baixa`
- **Data limite** — texto livre ou no formato `DD/MM/AAAA`
- **Status** — definido automaticamente como `Pendente` no cadastro

As tarefas ficam apenas na memória. Ao encerrar a aplicação, a lista recomeça vazia.

## Tecnologias

- Python 3 (biblioteca padrão, sem dependências externas)
- Git e GitHub

## Instalação

1. Instale o [Python 3](https://www.python.org/downloads/) e confira no terminal:

```bash
python --version
```

2. Clone este repositório e entre na pasta do projeto.

Não é necessário criar ambiente virtual nem instalar pacotes.

## Execução

Na raiz do projeto:

```bash
python src/main.py
```

O menu oferece três opções:

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

Se ainda não houver tarefas, a listagem informa que não existem registros.

## Estrutura do repositório

```text
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

O planejamento lógico da Fase 1 está em `docs/planejamento_logico.pdf`.
