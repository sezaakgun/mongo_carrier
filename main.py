from json import loads
from pymongo import MongoClient

config = open('config.json', 'r').read()
data = loads(config)
print(data)

from_client = MongoClient(data['inputConnectionString'])
from_db = from_client[data['inputDb']]
from_coll = from_db[data['inputCollection']]
d = from_coll.find_one({},{'_id':0})
print(d)


target_client = MongoClient(data['outputConnectionString'])
target_db = target_client[data['outputDb']]
target_coll = target_db[data['outputCollection']]
target_coll.insert_one(d)