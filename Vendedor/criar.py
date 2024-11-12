from conexao import db

def create_vendedor():
    mycol = db.vendedor
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    end = []

    while True:
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua": rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        if input("Deseja cadastrar um novo endereço (S/N)? ").upper() != 'S':
            break

    mydoc = {"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

if __name__ == "__main__":
    create_vendedor()
