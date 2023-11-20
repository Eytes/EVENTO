from pymongo import MongoClient
from pymongo.collection import Collection


# uuidRepresentation='standard' (для поддержания кроссплатформенности)
__client = MongoClient('localhost', 27017, uuidRepresentation='standard')
__db = __client['EVENTO']

agents: Collection = __db['agents']
events: Collection = __db['events']
appointments: Collection = __db['appointments']
clients: Collection = __db['clients']
