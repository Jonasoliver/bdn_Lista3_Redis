from Usuario.menuUsuario import menu_usuarios  
from Vendedor.menuVendedor import menu_vendedor
from Produto.menuProduto import menu_produtos
from Favorito.menuFavorito import menu_favoritos
def main():
    while True:
        print("1-CRUD Usuário")
        print("2-CRUD Vendedor")
        print("3-CRUD Produto")
        print("4-CRUD Favoritos")
        print("S-Sair")
        
        key = input("Digite a opção desejada: ")

        if key == '1':
            menu_usuarios()  
        elif key == '2':
            menu_vendedor()       
            
        elif key == '3':
            menu_produtos()       
           
        elif key == '4':
            menu_favoritos()
           
        elif key.upper() == 'S':
            print("Tchau Prof...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
