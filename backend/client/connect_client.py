
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sgalera:test@cluster0.smcdbag.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Verificar la conexión a la base de datos
    client.admin.command('ismaster')
except ConnectionFailure:
    # Manejar una falla en la conexión
    raise Exception("No se pudo conectar a la base de datos MongoDB.")
