from flask_wtf import Form
from wtforms import StringField, validators, SubmitField, IntegerField, PasswordField


# https://www.tutorialspoint.com/flask/flask_wtf.htm

class Create_album(Form):
    title = StringField('Название Вашего альбома', [validators.DataRequired(
        'Пожалуйса введите название альбома'
    )])

    description = StringField('Описание альбома', [validators.DataRequired(
        'Пожалуйста введите описание альбома'
    )])
    submit = SubmitField('Отправить')


# < form action = "http://localhost:5000/index/create-album" method = post > как это генерить автоматом?
# {{ url_for name_veiw_func }}
# https://flask-wtf.readthedocs.io/en/stable/form.html#validation -> UPLOAD FILE
# http://flask.pocoo.org/docs/0.12/patterns/wtforms/
# use ngrok port -> for use site in internet


class Register_user(Form):
    first_name = StringField('Ваше Имя', [validators.DataRequired('Пожалуйса введите Ваше имя')])
    last_name = StringField('Фамилия', [validators.DataRequired('Пожалуйса введите, фамилию')])
    age = IntegerField(
        'Возраст',
        [
            validators.DataRequired('Пожалуйса введите, Ваш возраст'),
            validators.NumberRange(message='Введено не верно', min=5, max=150)
        ]
    )
    email = StringField(
        'email',
        [
            validators.DataRequired('Пожалуйса введите, Ваш email'),
            validators.Email('Некоректный адрес')
        ]
    )
    password = PasswordField(
        'Пароль',
        [
            validators.Length(min=8, max=25),
            validators.DataRequired('Введите пароль, поле не заполненно'),
            validators.EqualTo('confirm', message='Пароли не совпадают')
        ]

    )
    confirm = PasswordField('Повторите пароль')
    submit = SubmitField('Отправить')
