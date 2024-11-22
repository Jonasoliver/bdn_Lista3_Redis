def manage_favorites(redis_db, user):
    while True:
        print("-="*20)
        print("    Gerenciador de Favoritos")
        print("-="*20)
        print("1. Adicionar favorito")
        print("2. Ver favoritos")
        print("3. Remover favorito")
        print("0. Voltar")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if choice == 1:
            favorite = input("Digite o item para adicionar aos favoritos: ")
            redis_db.sadd(f"favorites:{user['email']}", favorite)
            print(f"Item '{favorite}' adicionado aos favoritos.")
        elif choice == 2:
            favorites = redis_db.smembers(f"favorites:{user['email']}")
            print("Seus favoritos: ", favorites)
        elif choice == 3:
            favorite = input("Digite o item para remover dos favoritos: ")
            redis_db.srem(f"favorites:{user['email']}", favorite)
            print(f"Item '{favorite}' removido dos favoritos.")
        elif choice == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
