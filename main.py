def criartarefa(lista):
    while(True):
        try:
            nome = input("Digite o nome da tarefa:")
            while(True):
                opc = input("Digite 0 - (não foi concluida) 1 - (concluida)\nopção:")
                if (opc == '1'):
                    concluida = True
                    break
                elif (opc == '0'):
                    concluida = False
                    break
                else:
                    print("opção invalida!")
                    continue
            return {"id": (len(lista)+1),"nome": nome,"concluida": concluida}
        except:
                print("erro ao cadastrar tarefa")
                continue
def mostrartarefas(lista):
     if not lista:
          return print("Lista vazia")
     else:
          for i in lista:
               print("id: {}\nNome da tarefa: {}\nConcluida:{}".format(i["id"],i["nome"],i["concluida"]))
     
     
listatarefas = []

while(True):

    print("======== Gerenciador de Tarefas =========")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opc = input()
    match opc:
            case '1':
                listatarefas.append(criartarefa(listatarefas))
                input("Tarefa adicionada com sucesso!\n Pressione algo para voltar para o menu...")

            case '2':
                mostrartarefas(listatarefas)
                input("digite algo para voltar para o menu...")

            case '3':
                break
         
            case _:
                print("Digite uma opção valida")
        

