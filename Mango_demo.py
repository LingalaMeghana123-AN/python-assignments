from pymongo import MongoClient

# connection string
client = MongoClient("mongodb+srv://meghanalingala076_db_user:meghana123@cluster0.mnt0hjt.mongodb.net/?appName=Cluster0")

# connect database
db = client["mydb"]
collection = db["user"]

data = {
    "name": "Rahul",
    "age": 21,
    "branch": "CSE"
}

collection.insert_one(data)

print("Connected to MongoDB successfully!")