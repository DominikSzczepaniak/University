from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = ""
client = MongoClient(uri, server_api=ServerApi('1'))
client.admin.command('ping')

library = client["library"]
authors = library["books"]

items = authors.find()

for item in items:
    print(item["author"])
