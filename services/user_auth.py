import bcrypt

# Função para autenticação de usuário (exemplo simples)
def login(redis_db, email, password):
    user = redis_db.hgetall(email)
    
    if user:
        stored_password = user.get("password")
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print(f"Login bem-sucedido para {email}!")
            return user
        else:
            print("Senha incorreta!")
            return None
    else:
        print("Usuário não encontrado!")
        return None

# Função para verificar se o usuário está logado
def user_logged(redis_db, email):
    return redis_db.exists(email)
