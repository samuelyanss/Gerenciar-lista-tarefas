
def criartarefa():
    while(True):
        try:
            id = int(input("Digite o id da tarefa:"))
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
            return [id,nome,concluida]
        except:
                print("erro ao cadastrar tarefa")
                continue

listatarefas = []

while(True):

    print("======== Gerenciador de Tarefas =========")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opc = input()
    match opc:
            case '1':
                listatarefas.append(criartarefa())

            case '2':
                print(listatarefas)

            case '3':
                break
         
            case _:
                print("Digite uma opção valida")
        

