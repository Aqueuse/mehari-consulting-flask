import os
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, flash

from server.files import list_img_in_folder, get_img_count
from server.database import aggregate_img_by_article, find_unused_img, create_archive
from server import config

baseURL = config.baseURL
secret = config.secret

upload_blueprint = Blueprint('upload', __name__, )


@upload_blueprint.route('/upload', methods=['GET'])
def got_to_upload_first_index():
    return redirect(baseURL+'upload&index=0')


@upload_blueprint.route('/upload&index=<index>', methods=['GET', 'POST'])
def upload(index):
    if request.method == 'GET':
        if request.cookies.get('userID') == secret:
            return render_template(
                'uploadImg.html',
                img_files=aggregate_img_by_article()[int(index):int(index)+6],
                baseURL=baseURL,
                img_total=get_img_count('public/img'),
                index=index,
                img_unused=find_unused_img()
            )
        else:
            return redirect(baseURL)
    if request.method == 'POST':
        if request.cookies.get('userID') == secret:
            print(request.form.to_dict(flat=True))
            current_date = datetime.now()
            current_full_date = current_date.strftime("%S%M%H%d%m%Y")
            file = request.files['newImg']
            if file.filename == '':
                return render_template(
                    'uploadImg.html',
                    img_files=aggregate_img_by_article()[int(index):int(index) + 6],
                    baseURL=baseURL,
                    img_total=get_img_count('public/img'),
                    index=index,
                    img_unused=find_unused_img()
                )
            if file and check_allowed_file(file.filename):
                filename = current_full_date + ".jpg"
                file.save(os.path.join('public/img/', filename))
                # then recreate a new archive with archive folder+img folder
                create_archive()
                return render_template(
                    'uploadImg.html',
                    img_files=aggregate_img_by_article()[int(index):int(index) + 6],
                    baseURL=baseURL,
                    img_total=get_img_count('public/img'),
                    index=index,
                    img_unused=find_unused_img()
                )
        else:
            return redirect(baseURL)


def check_allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
