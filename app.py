from configs.redis_connection import redis_connection
from configs.mongo_connection import mongo_connection
from ui.favorites_menu import favorites_menu
from ui.shopping_menu import shopping_menu
from ui.data_sync_menu import data_sync_menu

def main():
    # Conectando ao Redis e MongoDB
    redis_db = redis_connection()
    mongo_db = mongo_connection()

    # Verificando se as conexões foram bem-sucedidas
    if redis_db is None or mongo_db is None:
        print("Erro ao conectar ao Redis ou MongoDB.")
        return

    # Exibindo o menu principal diretamente, sem a parte de login
    print("Bem-vindo ao sistema!")

    while True:
        print("-="*20)
        print("         Menu Principal")
        print("-="*20)
        print("1 - Favoritos")
        print("2 - Compras")
        print("3 - Sincronizar MongoDB <-> Redis")
        print("0 - Sair")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        # Ações baseadas na escolha do usuário
        if choice == 1:
            favorites_menu(redis_db)
        elif choice == 2:
            shopping_menu(redis_db)
        elif choice == 3:
            data_sync_menu(redis_db, mongo_db)
        elif choice == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
