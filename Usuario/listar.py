from conexao import db

def read_usuario(nome=None):
    mycol = db.usuario
    if nome:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)
    else:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])

if __name__ == "__main__":
    nome = input("Deseja buscar um usuário específico? ")
    read_usuario(nome if nome else None)
