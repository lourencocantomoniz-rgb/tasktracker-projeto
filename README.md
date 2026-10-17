# TaskTracker - Sistema de Gerenciamento de Tarefas

> **Bootcamp II** - Projeto Cumulativo de Desenvolvimento de Software
> **Fase 2 - Entrega Intermediária:** Versionamento com Git/GitHub e implementação em Python

## Sobre o Projeto

O **TaskTracker** é uma aplicação de linha de comando (CLI) para organizar e acompanhar tarefas do dia a dia. Ele resolve um problema comum de estudantes e profissionais: compromissos anotados em papéis soltos ou guardados só na memória, o que leva a esquecimento de prazos, dificuldade de priorizar e sobrecarga mental.

Com o TaskTracker o usuário pode:

- Cadastrar tarefas com título, descrição, prioridade e data limite;
- Visualizar todas as tarefas organizadas por prioridade (Alta, Média, Baixa);
- Acompanhar um resumo com o total de tarefas, pendentes e concluídas.

## Funcionalidades

| Opção do menu | O que faz |
|---|---|
| 1. Cadastrar nova tarefa | Pede título, descrição, prioridade e data limite, valida os dados e guarda a tarefa com status "Pendente" |
| 2. Visualizar tarefas cadastradas | Lista todas as tarefas (ID, título, descrição, prioridade, data limite e status) e mostra o resumo |
| 3. Sair da aplicação | Encerra o programa |

## Regras de Negócio

- **Título obrigatório:** o sistema não aceita título vazio ou só com espaços e pede para digitar de novo.
- **Prioridade validada:** só aceita `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas e minúsculas. Qualquer outro valor gera erro e a pergunta é repetida.
- **Data limite:** deve estar no formato `DD/MM/AAAA` e ser uma data que existe no calendário.
- **Status automático:** toda tarefa nova começa como `Pendente`.

## Tecnologias Utilizadas

- **Python 3** (sem bibliotecas externas, apenas a biblioteca padrão)
- **Git** para controle de versão
- **GitHub** para hospedagem do repositório remoto

## Estrutura do Repositório

```
tasktracker-projeto/
├── README.md                    # Documentação do projeto (este arquivo)
├── .gitignore                   # Arquivos e pastas ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico da Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação em Python
```

## Como Instalar e Executar

### Pré-requisitos

- Python 3.8 ou superior instalado ([python.org/downloads](https://www.python.org/downloads/))
- Git instalado ([git-scm.com](https://git-scm.com/))

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/lourencocantomoniz-rgb/tasktracker-projeto.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```
   > No Linux/macOS, use `python3 src/main.py`.

### Exemplo de uso

```
==================================================
        TASKTRACKER - MENU PRINCIPAL
==================================================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
==================================================
Escolha uma opção (1-3): 1

--- CADASTRAR NOVA TAREFA ---
Título da tarefa:
Erro: O título é obrigatório.
Título da tarefa: Estudar para a prova de Banco de Dados
Descrição (opcional, pressione Enter para pular): Revisar capítulos 3 e 4
Prioridade (Alta / Média / Baixa): urgente
Erro: Prioridade inválida. Digite apenas Alta, Média ou Baixa.
Prioridade (Alta / Média / Baixa): Alta
Data limite (DD/MM/AAAA): 25/10/2026

Sucesso: Tarefa cadastrada com êxito!
```

## Próximos Passos (Fase 3)

- Empacotar a aplicação e criar um `Dockerfile` para rodá-la em container;
- Adicionar testes automatizados;
- Fazer o deploy da aplicação.

## Autor

Desenvolvido por **Lourenço Angelice Bettencourt do Canto Moniz**
Curso de Análise e Desenvolvimento de Sistemas - CEUB
