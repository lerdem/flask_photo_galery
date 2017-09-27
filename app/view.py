from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os

from app import app, db
from forms import Create_album, Register_user, Upload_photo, Login
from models import User, Album, Photo
from config import Configuration
from log import logger


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


@app.route('/upload-photo', methods=['GET', 'POST'])
def upload_photo():
    form = Upload_photo()
    if request.method == 'POST':
        image = request.files['file']

        logger.debug(type(image))

        image_file_name = secure_filename(image.filename)
        path = os.path.join(Configuration.UPLOAD_FOLDER, image_file_name)

        logger.debug(path)

        image.save(path)

        logger.debug(image.save(path))

        return 'OK download file'
    return render_template('upload_photo.html', form=form)

if __name__ == '__main__':
    logger.info('test2222')