def criartarefa(lista):
    while(True):
        nome = input("Digite o nome da tarefa:")
        return {"id": (len(lista)+1),"nome": nome,"concluida": False}
def mostrartarefas(lista):
     if not lista:
          return print("Lista vazia")
     else:
          for i in lista:
               print("id: {}\nNome da tarefa: {}\nConcluida:{}".format(i["id"],i["nome"],i["concluida"]))
def concluirtarefa(lista):
    try:
        idtarefa = int(input("Digite o id da tarefa que você quer concluir: "))

        for tarefa in lista:
            if tarefa["id"] == idtarefa:
                tarefa["concluida"] = True
                print(f"Tarefa {idtarefa} concluída com sucesso!")
                return

        print(f"Nenhuma tarefa encontrada com o ID {idtarefa}.")

    except ValueError:
        print("Digite um ID válido!")
          
     
     
listatarefas = []

while(True):

    print("======== Gerenciador de Tarefas =========")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Sair")

    opc = input()
    match opc:
            case '1':
                listatarefas.append(criartarefa(listatarefas))
                input("Tarefa adicionada com sucesso!\n Pressione algo para voltar para o menu...")

            case '2':
                mostrartarefas(listatarefas)
                input("digite algo para voltar para o menu...")

            case '3':
                concluirtarefa(listatarefas)
                input("digite algo para voltar para o menu...")

            case '4':
                break
         
            case _:
                print("Digite uma opção valida")
        

