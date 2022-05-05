from pymongo import MongoClient
import os

client = MongoClient(os.environ.get('MONGO_CONNECT_STR'))
db = client.get_database('Clef')
profile = db.get_collection('Profile')
sessions = db.get_collection('Sessions')
