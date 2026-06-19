from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(100), nullable=False)


class SearchHistory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_email = db.Column(db.String(100), nullable=False)

    product_name = db.Column(db.String(200), nullable=False)

    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())