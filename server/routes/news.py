import datetime
import os
from flask import Blueprint, render_template, redirect, request
from server import database as database
from server import config
from server import files

baseURL = config.baseURL

news_blueprint = Blueprint('news', __name__,)


@news_blueprint.route('/', methods=['GET'])
def redirect_to_info():
    return redirect(baseURL+'infos')


@news_blueprint.route('/infos', methods=['GET'])
def route_to_last_news():
    slice_articles_index = 0
    article_limit = 6
    index_articles_precedents = slice_articles_index - article_limit
    index_articles_suivants = slice_articles_index + article_limit
    return render_template(
        'news.html',
        search_result=database.retrieve_news_by_chunck(0, 6),
        count_articles=database.count_news(),
        index_articles_precedents=index_articles_precedents,
        index_articles_suivants=index_articles_suivants,
        baseURL=baseURL
    )


@news_blueprint.route('/type=news&index=<index>', methods=['GET'])
def route_to_news_by_index(index):
    slice_articles_index = int(index)
    article_limit = 6
    index_articles_precedents = slice_articles_index - article_limit
    index_articles_suivants = slice_articles_index + article_limit
    return render_template(
        'news.html',
        search_result=database.retrieve_news_by_chunck(index, 6),
        count_articles=database.count_news(),
        index_articles_precedents=index_articles_precedents,
        index_articles_suivants=index_articles_suivants,
        baseURL=baseURL
    )
