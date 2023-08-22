from django.conf import settings
import pymongo

MONGO_DB_CONNECTION_STRING = "mongodb://localhost:27017"
MONGO_DB_NAME = "playground"

client = pymongo.MongoClient(MONGO_DB_CONNECTION_STRING)
db = client[MONGO_DB_NAME]