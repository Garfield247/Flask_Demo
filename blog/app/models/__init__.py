from .user import User
from .posts import Posts
from app.extensions import db


# 创建多对多的中间关联表，ORM自动维护
collections = db.Table('collections',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'))
)
