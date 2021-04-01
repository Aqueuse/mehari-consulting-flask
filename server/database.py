import uuid
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.details


def retrieve_article(id):
    result = db.articles.find_one({'id': id}, {'_id': 0})
    return result


def retrieve_news_by_chunck(index, limit):
    result = list(
        db.articles.find({'typeIsArticle': True}, {'_id': 0}).
        sort('date', -1).
        skip(int(index)).
        limit(limit)
    )
    return result


def retrieve_rubrique_by_chunck(rubrique_name, index, limit):
    result = list(
        db.articles.find({'categorie': rubrique_name}, {'_id': 0}).
        sort('date', -1).
        skip(int(index)).
        limit(limit)
    )
    return result


def retrieve_titles_and_ids():
    result = list(db.articles.find({}, {'title': 1, 'id': 1, '_id': 0}).sort('date', -1))
    return result


def count_articles(key, value):
    return db.articles.count_documents({key: value})


def add_article(data):
    data['id'] = create_unique_id(data['title'])
    db.articles.insert_one(data)


def edit_article(id, data):
    db.articles.update_one(
        {'id': id},
        {'$set': data}
    )


def remove_article(id):
    db.articles.delete_one({'id': id})


def create_unique_id(complicated_title):
    key = "-" + uuid.uuid4().hex[:8]

    short_title = complicated_title.lower()
    array_title = short_title.split(" ")[:3]
    clean_title = []

    for word in array_title :
        for char in word :
            if char.isalnum():
                clean_title.append(char)
    return "".join(clean_title) + key
