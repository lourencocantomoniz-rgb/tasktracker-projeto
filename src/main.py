"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)

Autor: Lourenço Angelice Bettencourt do Canto Moniz
Curso: Análise e Desenvolvimento de Sistemas - CEUB

Este programa traduz para Python a "receita lógica" definida na Fase 1:
- Cadastro de tarefas com validação de título e prioridade;
- Visualização das tarefas cadastradas com resumo de desempenho;
- Menu contínuo até o usuário escolher sair.
"""

from datetime import datetime

# ---------------------------------------------------------------------------
# Dados do sistema
# ---------------------------------------------------------------------------

# Lista central de tarefas (cada tarefa é um dicionário)
tarefas = []

# Prioridades aceitas: a chave é o que o usuário digita (em minúsculas)
# e o valor é a forma padronizada que fica guardada na tarefa.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

# Ordem usada para exibir as tarefas (Alta primeiro, Baixa por último)
ORDEM_PRIORIDADE = {"Alta": 1, "Média": 2, "Baixa": 3}


# ---------------------------------------------------------------------------
# Funções de validação (Regras de Negócio)
# ---------------------------------------------------------------------------

def titulo_valido(titulo):
    """Regra 1: o título não pode ser vazio nem conter apenas espaços."""
    return titulo.strip() != ""


def normalizar_prioridade(prioridade):
    """Regra 2: aceita apenas Alta, Média (ou Media) e Baixa.

    Retorna a prioridade padronizada ("Alta", "Média" ou "Baixa")
    ou None se o valor digitado for inválido.
    """
    return PRIORIDADES_VALIDAS.get(prioridade.strip().lower())


def data_valida(data):
    """Verifica se a data está no formato DD/MM/AAAA e se existe no calendário."""
    try:
        datetime.strptime(data.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Funções de entrada de dados (repetem a pergunta até a resposta ser válida)
# ---------------------------------------------------------------------------

def solicitar_titulo():
    while True:
        titulo = input("Título da tarefa: ")
        if titulo_valido(titulo):
            return titulo.strip()
        print("Erro: O título é obrigatório.")


def solicitar_prioridade():
    while True:
        prioridade = input("Prioridade (Alta / Média / Baixa): ")
        prioridade_ok = normalizar_prioridade(prioridade)
        if prioridade_ok:
            return prioridade_ok
        print("Erro: Prioridade inválida. Digite apenas Alta, Média ou Baixa.")


def solicitar_data_limite():
    while True:
        data = input("Data limite (DD/MM/AAAA): ")
        if data_valida(data):
            return data.strip()
        print("Erro: Data inválida. Use o formato DD/MM/AAAA (ex: 25/10/2026).")


# ---------------------------------------------------------------------------
# Módulo de cadastro
# ---------------------------------------------------------------------------

def cadastrar_tarefa():
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = solicitar_titulo()
    descricao = input("Descrição (opcional, pressione Enter para pular): ").strip()
    prioridade = solicitar_prioridade()
    data_limite = solicitar_data_limite()

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # status inicial definido automaticamente
    }
    tarefas.append(tarefa)

    print("\nSucesso: Tarefa cadastrada com êxito!")


# ---------------------------------------------------------------------------
# Módulo de visualização
# ---------------------------------------------------------------------------

def exibir_resumo():
    total = len(tarefas)
    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")

    print("-" * 50)
    print(f"Total: {total} | Pendentes: {pendentes} | Concluídas: {concluidas}")
    print("-" * 50)


def visualizar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    # Exibe as tarefas ordenadas por prioridade (Alta -> Média -> Baixa)
    ordenadas = sorted(tarefas, key=lambda t: ORDEM_PRIORIDADE[t["prioridade"]])

    for tarefa in ordenadas:
        print("-" * 50)
        print(f"ID:          {tarefa['id']}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status:      {tarefa['status']}")

    exibir_resumo()


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------

def exibir_menu():
    print("\n" + "=" * 50)
    print("        TASKTRACKER - MENU PRINCIPAL")
    print("=" * 50)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 50)


def main():
    print("Bem-vindo ao TaskTracker!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nObrigado por usar o TaskTracker. Até logo!")
            break
        else:
            print("Erro: Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAplicação encerrada pelo usuário. Até logo!")
