import uuid
import os
import tarfile
from pymongo import MongoClient
from server.files import list_all_img_in_folder

client = MongoClient('mongodb://localhost:27017/')
db = client.details


def retrieve_article(id):
    result = db.articles.find_one({'id': id}, {'_id': 0})
    return result


def retrieve_all_articles():
    result = db.articles.find({}, {'_id': 0})
    return result


def retrieve_news_by_chunck(index, limit):
    result = list(
        db.articles.find({'typeIsArticle': {'$in' : ['true', True, 'True']}}, {'_id': 0}).
        sort('date', -1).
        skip(int(index)).
        limit(limit)
    )
    for element in result:
        element['content'] = remove_author_name(element['content'])
    return result


def retrieve_rubrique_by_chunck(rubrique_name, index, limit):
    result = list(
        db.articles.find({'categorie': rubrique_name}, {'_id': 0}).
        sort('date', -1).
        skip(int(index)).
        limit(limit)
    )
    for element in result:
        element['content'] = remove_author_name(element['content'])
    return result


def retrieve_titles_and_ids():
    result = list(db.articles.find({}, {'title': 1, 'id': 1, '_id': 0}).sort('date', -1))
    return result


def count_articles(key, value):
    return db.articles.count_documents({key: value})


def count_news():
    return db.articles.count_documents({'typeIsArticle': {'$in' : ['true', True, 'True']}})


def add_article(data):
    data['thumbail'] = data['image'][0]
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


def aggregate_img_by_article():
    result = list(db.articles.find({}, {'image': 1, '_id': 0}).sort('date', -1))
    flat_result = array_of_dict_to_array_flat(result)
    return flat_result


def array_of_dict_to_array_flat(array):
    image_list = []
    for element in array:
        if 'image' in dict(element):
            for value in (dict(element)['image']):
                image_list.append(value)
    return image_list


# compare img articles with img folder to find unused img
def find_unused_img():
    list_total = list_all_img_in_folder('public/img')
    list_used = aggregate_img_by_article()

    list_difference = []
    for item in list_total:
        if item not in list_used:
            list_difference.append(item)
    return list_difference


def populate_archive_folder():
    result = retrieve_all_articles()
    for element in result:
        file = open('archive/'+element['id']+'.txt', 'w')
        file.write(element['title']+'\n')
        file.write(element['date']+'\n')
        file.write(element['id']+'\n')
        file.write(str(element['typeIsArticle'])+'\n')
        file.write(element['thumbail']+'\n')
        file.write(element['categorie']+'\n')
        file.write(str(element['content']))
        file.close()


def create_archive():
    os.remove('public/img/archive.tgz')
    with tarfile.open('public/img/archive.tgz', 'x:gz') as tar:
        tar.add('archive', 'archive')
        tar.add('public/img', 'img')
    tar.close()


def remove_author_name(text):
    return text[:text.find("<p>")] + text[text.find("</p>") + len('<p>')+3:]
