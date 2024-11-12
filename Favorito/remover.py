from conexao import db
from bson.objectid import ObjectId

def remover_favorito():
    cpf = input("Digite o CPF do usuário: ")
    produto_id = input("Digite o ID do produto a ser removido dos favoritos: ")

    try:
        produto_id = ObjectId(produto_id)  
    except Exception as e:
        print("ID do produto inválido:", e)
        return

    usuario = db.usuario.find_one({"cpf": cpf})
    if not usuario:
        print("Usuário não encontrado.")
        return

    resultado = db.usuario.update_one(
        {"cpf": cpf},
        {"$pull": {"favoritos": produto_id}}  
    )

    if resultado.modified_count > 0:
        print("Produto removido dos favoritos com sucesso.")
    else:
        print("Produto não encontrado nos favoritos.")
