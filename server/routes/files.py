import os
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, flash

from server.files import list_img_in_folder
from server import config

baseURL = config.baseURL
secret = config.secret

upload_blueprint = Blueprint('upload', __name__, )


@upload_blueprint.route('/upload', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if request.cookies.get('userID') == secret:
            return render_template(
                'uploadImg.html',
                img_files=list_img_in_folder('public/img'),
                baseURL=baseURL
            )
        else:
            return redirect(baseURL)
    if request.method == 'POST':
        if request.cookies.get('userID') == secret:
            current_date = datetime.now()
            current_full_date = current_date.strftime("%S%M%H%d%m%Y")

            file = request.files['newImg']
            if file.filename == '':
                return render_template(
                    'uploadImg.html',
                    img_files=list_img_in_folder('public/img'),
                    baseURL=baseURL
                )
            if file and check_allowed_file(file.filename):
                filename = current_full_date + ".jpg"
                file.save(os.path.join('public/img/', filename))
                # then recreate a new archive with db+img folder
                return render_template(
                    'uploadImg.html',
                    img_files=list_img_in_folder('public/img'),
                    baseURL=baseURL
                )
        else:
            return redirect(baseURL)


def check_allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
