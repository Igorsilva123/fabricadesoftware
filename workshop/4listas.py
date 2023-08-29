#decimo setimo

tasks = []

while True:
    print("\nFila de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Executar fila de tarefas")
    print("3. Sair")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        task_description = input("Digite a descrição da tarefa: ")
        tasks.append(task_description)
        print(f"Tarefa '{task_description}' adicionada à fila.")
    elif choice == '2':
        if tasks:
            task = tasks.pop(0)
            print(f"Executando: {task}")
        else:
            print("A fila de tarefas está vazia.")
    elif choice == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
