from conexao import db
from bson.objectid import ObjectId

def update_produto(produto_id):
    mycol = db.produto
    try:
        produto_id = ObjectId(produto_id)  
    except Exception as e:
        print("ID do produto inválido:", e)
        return

    myquery = {"_id": produto_id}
    produto = mycol.find_one(myquery)

    if not produto:
        print("Produto não encontrado.")
        return

    print("Dados do produto: ", produto)
    nome = input("Novo nome do produto (pressione Enter para manter): ")
    preco = input("Novo preço do produto (pressione Enter para manter): ")

    if nome:
        produto["nome"] = nome
    if preco:
        produto["preco"] = float(preco)

    newvalues = {"$set": produto}
    mycol.update_one(myquery, newvalues)

    print("Produto atualizado com sucesso.")
