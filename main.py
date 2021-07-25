from flask import Flask
from flask_talisman import Talisman

from server.routes.admin import admin_blueprint
from server.routes.article import article_blueprint
from server.routes.files import upload_blueprint
from server.routes.news import news_blueprint
from server.routes.rubrique import rubrique_blueprint
from server import config

app = Flask(__name__, static_folder='public')
talisman = Talisman(app, content_security_policy=[])

app.config['UPLOAD_FOLDER'] = '/public/img'
app.config['SESSION_COOKIE_NAME'] = 'userSession'
app.config['SECRET_KEY'] = config.secret

app.register_blueprint(admin_blueprint)
app.register_blueprint(article_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(news_blueprint)
app.register_blueprint(rubrique_blueprint)


if __name__ == '__main__':
    app.run()
