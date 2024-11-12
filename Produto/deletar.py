from conexao import db
from bson.objectid import ObjectId

def delete_produto(produto_id):
    mycol = db.produto
    try:
        produto_id = ObjectId(produto_id)  
    except Exception as e:
        print("ID do produto inválido:", e)
        return

    myquery = {"_id": produto_id}
    resultado = mycol.delete_one(myquery)

    if resultado.deleted_count > 0:
        print(f"Produto com ID {produto_id} deletado com sucesso.")
    else:
        print("Produto não encontrado.")