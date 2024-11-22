from services.user_favorites import manage_favorites

def favorites_menu(redis_db, user):
    while True:
        print("-="*20)
        print("     Menu de Favoritos")
        print("-="*20)
        print("1. Gerenciar Favoritos")
        print("0. Sair")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if choice == 1:
            manage_favorites(redis_db, user)
        elif choice == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
