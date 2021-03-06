import datetime
from marshmallow import fields, Schema  # we will use these later

from . import db
from ..app import bcrypt
# from .blog_post import BlogPostSchema


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    # navigational property
    blogposts = db.relationship('BlogPostModel', backref='users', lazy=True)

    def __init__(self, data):
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = self._generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'

    def _generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode('utf-8')

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def delete(self):
        '''deletes row from db'''
        db.session.delete(self)
        db.session.commit()

    def save(self):
        '''saves current state of model to db'''
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        '''takes in data to modify model'''
        for key, item in data.items():
            if key == 'password':
                self.password = self._generate_hash(value)
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    blogposts = fields.Nested(BlogPostSchema, many=True)

