from conexao import db

def update_vendedor(nome):
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        print("Dados do usuário: ", mydoc)
        nome = input("Novo Nome (deixe vazio para manter): ")
        if nome:
            mydoc["nome"] = nome

        sobrenome = input("Novo Sobrenome (deixe vazio para manter): ")
        if sobrenome:
            mydoc["sobrenome"] = sobrenome

        cpf = input("Novo CPF (deixe vazio para manter): ")
        if cpf:
            mydoc["cpf"] = cpf

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print("Usuário atualizado.")
    else:
        print("Usuário não encontrado.")

if __name__ == "__main__":
    nome = input("Qual usuário deseja atualizar? ")
    update_vendedor(nome)
