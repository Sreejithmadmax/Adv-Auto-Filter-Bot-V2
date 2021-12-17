# Added By [@paulwalker_tg]

import pymongo
from bot import DB_URI


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient["CHATS"]
user_col = database['USERS']

async def user_count():
    return user_col.estimated_document_count()

async def get_users():
    user_docs = user_col.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])   
    return user_ids
 
async def add_to_users(user_id: int):
    user_col.insert_one({'_id': user_id})
    return
   
async def del_from_users(user_id: int):
    user_col.delete_one({'_id': user_id})
    return

async def present_in_users(user_id : int):
    found = user_col.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False
