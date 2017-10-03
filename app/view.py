from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os

from app import app, db, login_manager
from forms import Create_album, Register_user, Upload_photo, Login
from models import User, Album, Photo
from config import Configuration

login_manager.login_view = 'login'
# https://flask-login.readthedocs.io/en/latest/#login-example

def chek_unique_email(email):
    # class user and None(False)
    _email_in_base = User.query.filter(User.email == email).first()
    print(_email_in_base, email)
    if bool(_email_in_base):
        return False
    else:
        return True
    # Через Flash добавить сообщение


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/create-album', methods=['GET', 'POST'])
@login_required
def create_album():
    form = Create_album()
    if request.method == 'POST' and form.validate():
        return 'Альбом создан для '
        # redirect(url_for('index'))
        # разобрать как работает flash
    return render_template('create_album.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register_user()
    if request.method == 'POST' and form.validate() and chek_unique_email(form.email.data):
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
        return redirect(url_for('login'))
    # update_time через PUT дописать
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)   # хрень непонятная
                return redirect(url_for('index'))
        return '<h1>ERROR LOGGIN</h1>'
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/upload-photo', methods=['GET', 'POST'])
@login_required
def upload_photo():
    form = Upload_photo()
    if request.method == 'POST':
        image = request.files['file']
        image_file_name = secure_filename(image.filename)
        path = os.path.join(Configuration.UPLOAD_FOLDER, image_file_name)
        image.save(path)
        return 'OK download file'
    return render_template('upload_photo.html', form=form)

if __name__ == '__main__':
    pass