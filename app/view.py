from flask import render_template, request, flash
from app import app
from forms import Create_album


@app.route('/index')
def index():
    return 'Hello, this is photo galery'


@app.route('/index/create-album', methods=['GET', 'POST'])
def create_album():
    form = Create_album()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Все поля что-то там....')
            return render_template('create_album.html', form=form)
        else:
            return 'Данные успешно сохранены!'
    elif request.method == 'GET':
        return render_template('create_album.html', form=form)
