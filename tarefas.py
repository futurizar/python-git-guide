tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✓" if tarefa["concluida"] else "✗"
            print(f"{i}. [{status}] {tarefa['tarefa']}")

def marcar_concluida(numero):
    if 0 < numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[numero - 1]['tarefa']}' marcada como concluída!")
    else:
        print("Número inválido!")

while True:
    print("\n1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Sair")
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        num = int(input("Digite o número da tarefa a marcar: "))
        marcar_concluida(num)
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")