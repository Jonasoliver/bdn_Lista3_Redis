from conexao import db

def listar_favoritos():
    cpf = input("Digite o CPF do usuário: ")

    usuario = db.usuario.find_one({"cpf": cpf})
    if not usuario:
        print("Usuário não encontrado.")
        return

    print("Produtos favoritos:")
    for produto_id in usuario.get("favoritos", []):
        produto = db.produto.find_one({"_id": produto_id})
        if produto:
            print(f"ID: {produto['_id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
        else:
            print(f"Produto com ID {produto_id} não encontrado.")
