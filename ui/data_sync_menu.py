from services.data_sync import sync_item_to_redis, sync_item_to_mongo

def data_sync_menu(redis_db, mongo_db):
    while True:
        print("-="*20)
        print("     Gerenciador MongoDB <-> Redis")
        print("-="*20)
        print("1. Sincronizar do MongoDB para o Redis")
        print("2. Sincronizar do Redis para o MongoDB")
        print("0. Voltar")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if choice == 1:
            collection_name = input("Digite o nome da coleção: ")
            item_id = input("Digite o ID do item para sincronizar do MongoDB para o Redis: ")
            sync_item_to_redis(redis_db, mongo_db, collection_name, item_id)
        elif choice == 2:
            collection_name = input("Digite o nome da coleção: ")
            item_id = input("Digite o ID do item para sincronizar do Redis para o MongoDB: ")
            sync_item_to_mongo(redis_db, mongo_db, collection_name, item_id)
        elif choice == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
