from conexao import db

def delete_vendedor(nome, sobrenome):
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome": sobrenome}
    mydoc = mycol.delete_one(myquery)
    if mydoc.deleted_count > 0:
        print(f"Vendedor {nome} {sobrenome} deletado.")
    else:
        print("Vendedor não encontrado.")

if __name__ == "__main__":
    nome = input("Nome do vendedor a ser deletado: ")
    sobrenome = input("Sobrenome do vendedor a ser deletado: ")
    delete_vendedor(nome, sobrenome)
