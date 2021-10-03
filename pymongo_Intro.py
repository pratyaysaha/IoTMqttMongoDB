import pymongo as mongo

client=mongo.MongoClient("mongodb://admin:admin@192.168.0.58:1990/people")
db=client["people"]
col=db["person"]

new_dict={"name":"gllo"}

x=col.insert_one(new_dict)
