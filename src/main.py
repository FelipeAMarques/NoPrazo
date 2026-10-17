"""TaskTracker — cadastro e visualização de tarefas pela linha de comando."""

import sys

PRIORIDADES_ACEITAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def configurar_terminal():
    """Garante leitura e escrita em UTF-8 no Windows."""
    for fluxo in (sys.stdout, sys.stdin):
        reconfigurar = getattr(fluxo, "reconfigure", None)
        if reconfigurar is None:
            continue
        try:
            reconfigurar(encoding="utf-8")
        except (OSError, ValueError):
            pass


def ler_titulo():
    """Pede o título até receber um texto que não seja vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar em branco ou conter apenas espaços.")


def ler_descricao():
    """Lê a descrição. O campo pode ficar vazio."""
    return input("Descrição: ").strip()


def ler_prioridade():
    """Aceita somente Alta, Média (ou Media) e Baixa."""
    while True:
        informada = input("Prioridade (Alta, Média ou Baixa): ").strip()
        prioridade = PRIORIDADES_ACEITAS.get(informada.casefold())
        if prioridade is not None:
            return prioridade
        print(
            'Erro: prioridade inválida. Use apenas "Alta", "Média" (ou "Media") ou "Baixa".'
        )


def ler_data_limite():
    """Registra a data limite em texto livre ou DD/MM/AAAA."""
    data = input("Data limite (DD/MM/AAAA ou texto livre): ").strip()
    if data:
        return data
    return "Não informada"


def cadastrar_tarefa(tarefas):
    """Monta uma tarefa válida e inclui na lista com status Pendente."""
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": ler_descricao(),
        "prioridade": ler_prioridade(),
        "data_limite": ler_data_limite(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f'\nTarefa cadastrada com sucesso: "{tarefa["titulo"]}" (status: Pendente).')


def visualizar_tarefas(tarefas):
    """Mostra a lista vazia ou todas as propriedades de cada tarefa."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descrição)"
        print(f"\nTarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {descricao}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")


def exibir_menu():
    print("\n========== TaskTracker ==========")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    configurar_terminal()
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("TaskTracker encerrado. Até a próxima.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
