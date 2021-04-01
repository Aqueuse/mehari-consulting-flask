from flask import Blueprint, render_template, request, redirect, make_response
from server import database, config, admin

baseURL = config.baseURL
secret = config.secret

admin_blueprint = Blueprint('admin', __name__,)


@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if admin.validate_user(request.form['identifiant'], request.form['password']):
            response = make_response(redirect(baseURL+'admin'))
            response.set_cookie('userID', secret)
            return response
        else:
            return redirect(baseURL)


@admin_blueprint.route('/admin', methods=['GET'])
def load_admin_page():
    if request.cookies.get('userID') == secret:
        return render_template(
            'admin.html',
            search_result=database.retrieve_titles_and_ids(),
            baseURL=baseURL
        )
    else:
        return redirect(baseURL)


@admin_blueprint.route('/create', methods=['GET', 'POST'])
def create_article():
    if request.cookies.get('userID') == secret:
        if request.method == 'GET':
            return render_template('create_article.html')
        if request.method == 'POST':
            data = request.form.to_dict(flat=True)
            # we add the array of images associated with this article on the db
            data['image'] = request.form.to_dict(flat=False)['image']
            database.add_article(data)
            return redirect(baseURL+'type=article&id='+data['id'])
    else:
        return redirect(baseURL)


@admin_blueprint.route('/edit=<id>', methods=['GET', 'POST'])
def edit_article(id):
    if request.cookies.get('userID') == secret:
        if request.method == 'GET':
            return render_template(
                'edit_article.html',
                result=database.retrieve_article(id)
            )
        if request.method == 'POST':
            data = request.form.to_dict(flat=True)
            # we update the array of images associated with this article on the db
            data['image'] = request.form.to_dict(flat=False)['image']
            data['id'] = id
            database.edit_article(id, data)
            return render_template(
                'edit_article.html',
                result=database.retrieve_article(id)
            )
    else:
        return redirect(baseURL)


@admin_blueprint.route('/delete=<id>', methods=['GET'])
def remove_article(id):
    if request.cookies.get('userID') == secret:
        database.remove_article(id)
        return redirect(baseURL+'admin')
    else:
        return redirect(baseURL)
