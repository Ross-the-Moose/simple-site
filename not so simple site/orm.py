from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
import hashlib

class the_user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(80), unique=False)
    reg_data = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    hon = db.Column(db.Integer, nullable=False)
    lem = db.Column(db.Integer, nullable=False)
    imb = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.user_id}{self.username}'

    def validate(self, password):
        return self.password == password

class category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.cat_id}{self.cat_name}'

class product(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'), nullable=False)
    prod_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80))
    amount_left = db.Column(db.Integer)
    price=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(80))
    #картинка

    def __repr__(self):
        return f'{self.prod_id}{self.prod_name}{self.price}'

class favorites(db.Model):
    fav_num = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('the_user.user_id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))

    def __repr__(self):
        return f'{self.user_id}{self.prod_id}'

class orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('the_user.user_id'))
    money = db.Column(db.Integer, nullable=False)
    if_payed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'{self.order_id}{self.user_id}'


class order_comp(db.Model):
    comp_num = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.order_id}{self.prod_id}'

class otziv(db.Model):
    ot_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    text = db.Column(db.String(80), nullable = False)