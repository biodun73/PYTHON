import pymongo
dbmongo=pymongo.MongoClient("mongodb://localhost:27017/")
mong = dbmongo['login']
mycol = dbmongo["customers"]
collist = mong.list_collection_names()
if "customers" in collist:
  print("The collection exists.")