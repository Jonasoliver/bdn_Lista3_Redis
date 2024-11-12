from .criar import create_usuario
from .listar import read_usuario
from .atualizar import update_usuario
from .deletar import delete_usuario

def menu_usuarios():
    while True:
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        print("V-Voltar")
        
        sub = input("Digite a opção desejada: ")

        if sub == '1':
            create_usuario()
        elif sub == '2':
            nome = input("Deseja buscar um usuário específico? ")
            read_usuario(nome if nome else None)
        elif sub == '3':
            nome = input("Qual usuário deseja atualizar? ")
            update_usuario(nome)
        elif sub == '4':
            nome = input("Nome do usuário a ser deletado: ")
            sobrenome = input("Sobrenome do usuário a ser deletado: ")
            delete_usuario(nome, sobrenome)
        elif sub.upper() == 'V':
            break
        else:
            print("Opção inválida. Tente novamente.")
