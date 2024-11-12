from conexao import db

def read_vendedor(nome=None):
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
    nome = input("Deseja buscar um vendedor específico? ")
    read_vendedor(nome if nome else None)
