from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connection_mongo():
    uri = "mongodb+srv://jonas:1234@cluster0.4bkdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')  
        print("Mongo conectado!")
        return client  
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None  