from flask import Blueprint, render_template

from server import database as database
from server import config

baseURL = config.baseURL
rubrique_blueprint = Blueprint('rubrique', __name__,)


@rubrique_blueprint.route('/type=rubrique&name=<categorie_name>&index=<index>', methods=['GET'])
def route_to_rubrique(categorie_name, index):
    slice_articles_index = int(index)
    article_limit = 6

    index_articles_precedents = slice_articles_index - article_limit
    index_articles_suivants = slice_articles_index + article_limit
    return render_template(
        'rubrique.html',
        search_result=database.retrieve_rubrique_by_chunck(categorie_name, index, article_limit),
        count_articles=database.count_articles('categorie', categorie_name),
        index_articles_precedents=index_articles_precedents,
        index_articles_suivants=index_articles_suivants,
        baseURL=baseURL,
        categorie_name=categorie_name
    )
