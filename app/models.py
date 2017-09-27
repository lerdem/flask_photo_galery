from app import db
from datetime import datetime
from flask_login import UserMixin


"""
from sqlalchemy import create_engine
from config import Configuration

engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI,pool_recycle=280, echo=False)
connection = engine.connect()
"""


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)    # уникальность почты
    password = db.Column(db.String(80))
    created_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime)


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'id: {}, name: {}, email: {}'.format(
            self.id,
            self.first_name,
            self.email
    )

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))


    def __init__(self, *args, **kwargs):
        super(Album, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'id: {}, user_id: {}, title: {}'.format(
            self.id,
            self.from_user_id,
            self.title
        )

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    description = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.now())
    path_to_photo = db.Column(db.String(255))


    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)


    def __repr__(self):
        return 'id: {}, album_id: {}, name: {}, path: {}'.format(
            self.id,
            self.from_album_id,
            self.name,
            self.path_to_photo
        )





if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # u = User(first_name='Test1', email='sometest1@hhh.com', last_name='Test_last1')
    # db.session.add(u)
    # # a = Album(from_user_id=1, title='my_photo')
    # # db.session.add(a)
    # # ph = Photo(from_album_id=1, path_to_photo='/home/lerdem/uploads/user_id/album_id/name.gpeg')
    # # db.session.add(ph)
    # # db.session.add_all([])
    # db.session.commit()

    # a = [User.query.all(), Album.query.all(), Photo.query.all()]

    print(User.query.get(100))

