import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.details

articles_collection = database.get_collection("articles")

# helpers


def article_helper(article) -> dict:
    return {
        "id": str(article["id"]),
        "title": article["title"],
        "content": article["content"],
        "date": article["date"],
        "typeIsArticle": article["typeIsArticle"],
        "categorie": article["categorie"],
    }


# crud operations

# Retrieve specific articles in the database
async def retrieve_articles(key: str, value):
    slice_articles_index = 0
    article_limit = 6

    index_articles_precedents = slice_articles_index - article_limit
    index_articles_suivants = slice_articles_index + article_limit

    articles = []
    async for article in articles_collection.find({key: value}).sort('date', -1).skip(slice_articles_index).limit(6):
        articles.append(article_helper(article))
    count_articles = await articles_collection.count_documents({key:value})
    return articles, index_articles_suivants, index_articles_precedents, count_articles


# Add a new article into to the database
async def add_article(article_data: dict) -> dict:
    article = await articles_collection.insert_one(article_data)
    new_article = await articles_collection.find_one({"id": article.inserted_id})
    return article_helper(new_article)


# Retrieve an article with a matching ID
async def retrieve_article(id: str) -> dict:
    article = await articles_collection.find_one({"id": id})
    if article:
        return article_helper(article)


# Update an article with a matching ID
async def update_article(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    article = await articles_collection.find_one({"id": id})
    if article:
        updated_article = await articles_collection.update_one(
            {"id": id}, {"$set": data}
        )
        if updated_article:
            return True
        return False


# Delete an article from the database
async def delete_article(id: str):
    article = await articles_collection.find_one({"id": id})
    if article:
        await articles_collection.delete_one({"id": id})
        return True
