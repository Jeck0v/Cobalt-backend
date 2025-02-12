from pymongo import MongoClient

server = "mongodb://localhost:27017/"
username = "cobaltDB"
password = ""
port = 27017

if server == "localhost":
    client = MongoClient("mongodb://mongo", username=username, password=password, port=port)

else:
    client = MongoClient(server, username=username, password=password, port=port)
