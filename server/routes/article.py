from flask import Blueprint, render_template
from server import database as database
from server import config

baseURL = config.baseURL

article_blueprint = Blueprint('article', __name__,)


@article_blueprint.route('/type=article&id=<id>', methods=['GET'])
def route_to_article(id):
    return render_template('article.html', result=database.retrieve_article(id), baseURL=baseURL)
