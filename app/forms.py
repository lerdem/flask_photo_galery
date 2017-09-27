from flask_wtf import Form
from wtforms import StringField, validators, SubmitField, IntegerField, PasswordField, SelectField, FileField

from config import My_config


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
    # дописать валидацию на уникальность почты
    password = PasswordField(
        'Пароль',
        [
            validators.Length(min=8, max=50),
            validators.DataRequired('Введите пароль, поле не заполненно'),
            validators.EqualTo('confirm', message='Пароли не совпадают')
        ]

    )
    confirm = PasswordField('Повторите пароль')
    submit = Create_album.submit


class Login(Form):
    email = Register_user.email
    password = PasswordField('Пароль')
    submit = Create_album.submit


# пока не используестся
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in My_config.ALLOWED_EXTENSIONS


class Upload_photo(Form):
    image = FileField('Загрузите изображение')
    description = StringField(
        'Описание изображения',
        [
            validators.DataRequired('Пожалуйса введите описание'),
            validators.Length(max=128)
        ]
    )
    from_album_id = SelectField('Добавить в альбом', choices=[(1, 'dfsdfds'), (2, 'wwwww')])
    # Валидация по размеру фото
    submit = Create_album.submit
    # http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
    # https://flask - wtf.readthedocs.io/en/stable/form.html#validation

"""
class UploadForm(Form):
    image        = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
    description  = TextAreaField(u'Image Description')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)
        # path like 'app/temp/upload' нужно следить за '/'
"""