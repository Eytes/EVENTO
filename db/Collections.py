from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


__client = AsyncIOMotorClient('localhost', 27017)
__db = __client['EVENTO']

agents: AsyncIOMotorCollection = __db['agents']
events: AsyncIOMotorCollection = __db['events']
appointments: AsyncIOMotorCollection = __db['appointments']
clients: AsyncIOMotorCollection = __db['clients']
