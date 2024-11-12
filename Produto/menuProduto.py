from .criar import create_produto
from .listar import read_produto
from .atualizar import update_produto
from .deletar import delete_produto

def menu_produtos():
    while True:
        print("Menu de Produtos")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")
        print("V-Voltar")
        
        sub = input("Digite a opção desejada: ")

        if sub == '1':
            create_produto()
        elif sub == '2':
            read_produto()
        elif sub == '3':
            produto_id = input("Qual produto deseja atualizar (ID)? ")
            update_produto(produto_id)
        elif sub == '4':
            produto_id = input("Qual produto deseja deletar (ID)? ")
            delete_produto(produto_id)
        elif sub.upper() == 'V':
            break
        else:
            print("Opção inválida. Tente novamente.")
