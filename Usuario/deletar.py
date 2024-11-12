from conexao import db

def delete_usuario(nome, sobrenome):
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome": sobrenome}
    mydoc = mycol.delete_one(myquery)
    if mydoc.deleted_count > 0:
        print(f"Usuário {nome} {sobrenome} deletado.")
    else:
        print("Usuário não encontrado.")

if __name__ == "__main__":
    nome = input("Nome do usuário a ser deletado: ")
    sobrenome = input("Sobrenome do usuário a ser deletado: ")
    delete_usuario(nome, sobrenome)
