from .adicionar import adicionar_favorito
from .listar import listar_favoritos
from .remover import remover_favorito

def menu_favoritos():
    while True:
        print("Menu de Favoritos")
        print("1-Adicionar Favorito")
        print("2-Listar Favoritos")
        print("3-Remover Favorito")
        print("V-Voltar")
        
        sub = input("Digite a opção desejada: ")

        if sub == '1':
            adicionar_favorito()
        elif sub == '2':
            listar_favoritos()
        elif sub == '3':
            remover_favorito()
        elif sub.upper() == 'V':
            break
        else:
            print("Opção inválida. Tente novamente.")
