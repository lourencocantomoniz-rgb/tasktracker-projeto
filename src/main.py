"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)

Autor: Lourenço Angelice Bettencourt do Canto Moniz
Curso: Análise e Desenvolvimento de Sistemas - CEUB

Versão 1: menu principal, loop contínuo, cadastro e listagem básicos.
(As validações das regras de negócio entram no próximo commit.)
"""

# Lista central de tarefas (cada tarefa é um dicionário)
tarefas = []


def cadastrar_tarefa():
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = input("Título da tarefa: ")
    descricao = input("Descrição (opcional, pressione Enter para pular): ")
    prioridade = input("Prioridade (Alta / Média / Baixa): ")
    data_limite = input("Data limite (DD/MM/AAAA): ")

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)

    print("\nSucesso: Tarefa cadastrada com êxito!")


def visualizar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for tarefa in tarefas:
        print("-" * 50)
        print(f"ID:          {tarefa['id']}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao']}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status:      {tarefa['status']}")


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
    main()
