from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os

from app import app, db
from forms import Create_album, Register_user, Upload_photo, Login
from models import User, Album, Photo
from config import My_config, Configuration


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-album', methods=['GET', 'POST'])
def create_album():
    form = Create_album()
    if request.method == 'POST' and form.validate():
        return 'Альбом создан'
        # redirect(url_for('index'))
        # разобрать как работает flash
    return render_template('create_album.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register_user()
    if request.method == 'POST' and form.validate():
        hash_password = generate_password_hash(form.password.data, method='sha256')
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            age=form.age.data,
            email=form.email.data,
            password=hash_password
        )
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрированы'  # redirect добавить
    # update_time через PUT дописать
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                return '<h1> OK </h1>'
    return render_template('login.html', form=form)


# это не работает!!!
@app.route('/upload-photo', methods=['GET', 'POST'])
def upload_photo():
    form = Upload_photo()
    if request.method == 'POST':
        print('-' * 80)
        image = request.files['file']
        image2 = 'uuuu'

        print(type(image), type(image2))
        print(image, image2)
        print('=' * 80)
        image_file_name = secure_filename(image.filename)
        path = os.path.join(Configuration.UPLOAD_FOLDER, image_file_name)
        print(path)
        image.save(path)
        return 'OK'

    # if request.method == 'POST':
    #     image = request.files['file']  # form.image.data
    #     image_file_name = secure_filename(image)
    #     image.save(
    #         os.path.join(
    #             My_config.BASE_DIR,
    #             My_config.UPLOAD_FOLDER,
    #             image_file_name
    #         )
    #     )
    #
    #
    #     return image.filename
    #
    #     #     'Фото загружено: <img src="{}">'.format(os.path.join(
    #     #         My_config.BASE_DIR,
    #     #         My_config.UPLOAD_FOLDER,
    #     #         image_file_name
    #     #     )
    #     # )
    return render_template('upload_photo.html', form=form)

if __name__ == '__main__':
    path = os.path.join(
        My_config.BASE_DIR,
        My_config.UPLOAD_FOLDER
    )
    print(path)