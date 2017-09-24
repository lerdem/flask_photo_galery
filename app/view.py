from flask import render_template, request, redirect, url_for
from app import app, db
from forms import Create_album, Register_user
from models import User, Album, Photo


@app.route('/')
def index():
    return 'Hello, this is photo galery'


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
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            age=form.age.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return 'Вы успешно зарегистрированы'  # redirect добавить
    # update_time через PUT дописать
    return render_template('register.html', form=form)