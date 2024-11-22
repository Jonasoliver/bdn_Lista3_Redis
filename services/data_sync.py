import redis
from bson.json_util import dumps, loads

# Função para obter um item do MongoDB e armazená-lo no Redis
def sync_item_to_redis(redis_db, mongo_db, collection_name, item_id):
    redis_key = f"{collection_name}:{item_id}"
    item = redis_db.get(redis_key)
    
    if item:
        # Se o item estiver no Redis, basta retornar
        print(f"Item {item_id} encontrado no Redis.")
        return item.decode('utf-8')
    
    # Se não estiver no Redis, pegue do MongoDB
    collection = mongo_db[collection_name]
    item = collection.find_one({"_id": item_id})
    
    if item:
        # Se o item for encontrado no MongoDB, salve no Redis e retorne
        redis_db.setex(redis_key, 3600, dumps(item))  # 3600 segundos de expiração no Redis
        print(f"Item {item_id} encontrado no MongoDB e armazenado no Redis.")
        return dumps(item)
    
    print(f"Item {item_id} não encontrado no MongoDB.")
    return None

# Função para sincronizar dados do Redis de volta para o MongoDB
def sync_item_to_mongo(redis_db, mongo_db, collection_name, item_id):
    redis_key = f"{collection_name}:{item_id}"
    item = redis_db.get(redis_key)
    
    if item:
        # Se o item está no Redis, converta e insira ou atualize no MongoDB
        item_data = loads(item.decode('utf-8'))
        collection = mongo_db[collection_name]
        # Inserir ou atualizar no MongoDB
        collection.replace_one({"_id": item_data['_id']}, item_data, upsert=True)
        print(f"Item {item_id} sincronizado do Redis para o MongoDB.")
    else:
        print(f"Item {item_id} não encontrado no Redis para sincronizar.")
