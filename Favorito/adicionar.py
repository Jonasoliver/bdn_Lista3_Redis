from conexao import db
from bson.objectid import ObjectId

def adicionar_favorito():
    cpf = input("Digite o CPF do usuário: ")
    produto_id = input("Digite o ID do produto a ser adicionado aos favoritos: ")

    try:
        produto_id = ObjectId(produto_id)  
    except Exception as e:
        print("ID do produto inválido:", e)
        return

    usuario = db.usuario.find_one({"cpf": cpf})
    if not usuario:
        print("Usuário não encontrado.")
        return

    db.usuario.update_one(
        {"cpf": cpf},
        {"$addToSet": {"favoritos": produto_id}}  
    )

    print("Produto adicionado aos favoritos com sucesso.")
