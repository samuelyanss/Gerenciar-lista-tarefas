
def criartarefa(id, nome, concluida = False):
    
    id = int(input("Digite o id da tarefa:"))
    nome = input("Digite o nome da tarefa:")

    opc = input("Digite \n0 - se a tarefa foi concluida \n1 - se ela ja foi concluida")

    if (opc == 1):
        concluida = True
    elif (opc == 0):
        concluida = False




listatarefas = []
print("======== Gerenciador de Tarefas =========")
print("1 - Adicionar tarefa")
print("2 - Listar tarefa")
print("3 - Sair")

opc = int(input())
match opc:

    case 1:
        print("caso 1")

    case 2:
        print("caso 2")

    case 3:
        print("caso 3")

    case _:
        print("caso desconhecido")
        

