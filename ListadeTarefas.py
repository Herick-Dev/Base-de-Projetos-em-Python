def adicionar_tarefa(lista_tarefas, descricao):
    lista_tarefas.append({"descricao": descricao, "concluida": False})

def remover_tarefa(lista_tarefas, indice):
    del lista_tarefas[indice]

def marcar_concluida(lista_tarefas, indice):
    lista_tarefas[indice]["concluida"] = True

def exibir_tarefas(lista_tarefas):
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['descricao']} - {status}")

def main():
    lista_tarefas = []

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(lista_tarefas, descricao)
        elif escolha == "2":
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            remover_tarefa(lista_tarefas, indice)
        elif escolha == "3":
            indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            marcar_concluida(lista_tarefas, indice)
        elif escolha == "4":
            exibir_tarefas(lista_tarefas)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()