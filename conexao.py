
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jonas:1234@cluster0.4bkdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.MercadoLivre
