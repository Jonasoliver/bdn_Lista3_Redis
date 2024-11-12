from conexao import db

def read_produto():
    mycol = db.produto
    print("Produtos existentes: ")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x["_id"], x["nome"], x["preco"])
