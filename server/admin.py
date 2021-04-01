from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.details


def validate_user(username, password):
    user_query = list(db.users.find({"$and": [{'username': username}, {'password': password}]}))
    if len(user_query) == 0:
        return False
    else:
        return True


def app_settings():
    settings_dict = {}
    settings = open("./server/config.py", "r")
    settings_array = settings.readlines()
    for element in settings_array:
        key = element.split('=')[0].rstrip('\n')
        value = element.split('=')[1].rstrip('\n')
        settings_dict[key] = value
    return settings_dict
