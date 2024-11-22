def shopping_menu(redis_db, user):
    while True:
        print("-="*20)
        print("    Gerenciador de Compras")
        print("-="*20)
        print("1. Adicionar compra")
        print("2. Ver compras")
        print("3. Remover compra")
        print("0. Voltar")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if choice == 1:
            purchase = input("Digite o item para adicionar à compra: ")
            redis_db.sadd(f"purchases:{user['email']}", purchase)
            print(f"Item '{purchase}' adicionado às compras.")
        elif choice == 2:
            purchases = redis_db.smembers(f"purchases:{user['email']}")
            print("Seus itens comprados: ", purchases)
        elif choice == 3:
            purchase = input("Digite o item para remover das compras: ")
            redis_db.srem(f"purchases:{user['email']}", purchase)
            print(f"Item '{purchase}' removido das compras.")
        elif choice == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
