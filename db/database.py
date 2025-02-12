from pymongo import MongoClient

client = MongoClient(
    host="mongo",
    port=27017,
    username="cobaltdb",
    password="-)i8N~x4r9cVX8"
)

db = client.cobalt_db