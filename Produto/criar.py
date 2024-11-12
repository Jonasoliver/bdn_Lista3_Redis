from conexao import db
from bson.objectid import ObjectId

def create_produto():
    mycol = db.produto
    print("\nInserindo um novo produto")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    vendedor_id = input("ID do vendedor: ")

    
    try:
        vendedor_id = ObjectId(vendedor_id)
    except Exception as e:
        print("ID do vendedor inválido:", e)
        return

    
    vendedor_col = db.vendedor
    vendedor = vendedor_col.find_one({"_id": vendedor_id})
    
    if not vendedor:
        print("Vendedor não encontrado.")
        return

    mydoc = {
        "nome": nome,
        "preco": preco,
        "vendedor_id": vendedor_id
    }
    
    x = mycol.insert_one(mydoc)
    
    
    vendedor_col.update_one(
        {"_id": vendedor_id},
        {"$push": {"produtos": x.inserted_id}}
    )

    print("Produto inserido com ID ", x.inserted_id)
