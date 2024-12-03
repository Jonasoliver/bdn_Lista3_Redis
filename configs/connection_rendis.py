import redis

def connection_rendis():
    try:
        r = redis.Redis(
        host='redis-15512.c114.us-east-1-4.ec2.redns.redis-cloud.com',
        port=15512,
        password='BwkX1rX6kCkxiLIaknvbOKjsrj9L4RVk')
        r.ping()
        print('Redis conectado!')
        return r 
    except redis.ConnectionError:
        print('Erro ao conectar ao Redis')
        return None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        return None
