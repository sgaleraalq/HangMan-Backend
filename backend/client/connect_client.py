
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sgalera:test@cluster0.smcdbag.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
users_db_client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    users_db_client.admin.command('ping')
    
except Exception as e:
    raise Exception("Connection failed: {}".format(e))