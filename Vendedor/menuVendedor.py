from .criar import create_vendedor
from .listar import read_vendedor
from .atualizar import update_vendedor
from .deletar import delete_vendedor

def menu_vendedor():
    while True:
        print("Menu do Vendedor")
        print("1-Create Vendedor")
        print("2-Read Vendedor")
        print("3-Update Vendedor")
        print("4-Delete Vendedor")
        print("V-Voltar")
        
        sub = input("Digite a opção desejada: ")

        if sub == '1':
            create_vendedor()
        elif sub == '2':
            nome = input("Deseja buscar um usuário específico? ")
            read_vendedor(nome if nome else None)
        elif sub == '3':
            nome = input("Qual usuário deseja atualizar? ")
            update_vendedor(nome)
        elif sub == '4':
            nome = input("Nome do usuário a ser deletado: ")
            sobrenome = input("Sobrenome do usuário a ser deletado: ")
            delete_vendedor(nome, sobrenome)
        elif sub.upper() == 'V':
            break
        else:
            print("Opção inválida. Tente novamente.")
