from pymongo import MongoClient

def upload_profile(user_id, profile_info):

    client = MongoClient('mongodb://localhost:27020')

    db = client.connections
    col = db['connections']

    col.update({'_id':user_id}, {"$set": profile_info}, upsert=True)

    return col

if __name__ == '__main__':
    col = upload_profile('id_1', {'add_stuff':'stuff'})    
    results = col.find({})
    print([x for x in results])
    col.delete_one({"_id":"id_1"})
    results = col.find({})
    print([x for x in results])