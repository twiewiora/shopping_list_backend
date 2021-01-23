import os

from flask import Flask
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
api = Api(app)

app.config.from_object("shopping.config." + os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('amount')
parser.add_argument('userId')
parser.add_argument('login')

from shopping.resources import ItemList, ItemCreate, Item, ItemChangeAmount, ItemChangeBuyStatus, CategoryList, \
    UserData, WakeUp

api.add_resource(ItemList, '/items/<user_id>')
api.add_resource(ItemCreate, '/item')
api.add_resource(Item, '/item/<item_id>')
api.add_resource(ItemChangeAmount, '/item/<item_id>/change-amount')
api.add_resource(ItemChangeBuyStatus, '/item/<item_id>/change-buy-status')
api.add_resource(CategoryList, '/category/all')
api.add_resource(UserData, '/user/<login>')
api.add_resource(WakeUp, '/wake-up')
