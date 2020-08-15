from pymongo import MongoClient

def upload_profile(user_id, profile_info):

    # host = 'localhost'
    host = 'mongo'
    client = MongoClient(f'mongodb://{host}:27017')

    db = client.connections
    col = db['connections']

    col.update({'_id':user_id}, {"$set": profile_info}, upsert=True)
    # col.insert_one(dict(_id=user_id, **profile_info))

    return col

if __name__ == '__main__':
    col = upload_profile('id_1', {'add_stuff':'stuff'})    
    results = col.find({})
    print([x for x in results])
    col.delete_one({"_id":"id_1"})
    results = col.find({})
    print([x for x in results])