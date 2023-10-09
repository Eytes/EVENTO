import pymongo
from pymongo.collection import Collection

__client = pymongo.MongoClient('localhost', 27017)
__db = __client['EVENTO']


agents: Collection = __db['agents']
events: Collection = __db['events']
appointments: Collection = __db['appointments']
clients: Collection = __db['clients']
