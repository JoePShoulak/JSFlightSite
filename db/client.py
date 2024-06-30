from .exceptions import ClientDoesNotExistError
from pymongo import MongoClient

db = MongoClient()

def get_client(id: int) -> dict:
    data = db.jsflight.clients.find_one({'id': id})

    if data is None:
        raise ClientDoesNotExistError(id)
    
    return data