

MONGODB_URL = 'mongodb://localhost:27017'
MONGODB_DB = 'test'
MONGODB_COLLECTION = 'test'

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string using motor    MongoClient
def connect_mongo():
    from pymongo import MongoClient
    client = MongoClient(MONGODB_URL)
    return client

#create the database if it does not exist
def create_db(db_name):
    client = connect_mongo()
    db = client[db_name]
    return db

