from flask_wtf import Form
from wtforms import StringField, validators, SubmitField

# https://www.tutorialspoint.com/flask/flask_wtf.htm

class Create_album(Form):
    title = StringField('Название Вашего альбома', [validators.DataRequired(
        'Пожалуйса введите название альбома'
    )])

    description = StringField('Описание альбома', [validators.DataRequired(
        'Пожалуйста введите описание альбома'
    )])
    submit = SubmitField('Подтвердить')

# < form action = "http://localhost:5000/index/create-album" method = post > как это генерить автоматом?